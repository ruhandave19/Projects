import requests, feedparser, re, os, time
from datetime import date, datetime, timedelta
from bidict import bidict
import pandas as pd
from thefuzz import process
from dotenv import load_dotenv
from enum import Enum, auto
from collections import defaultdict

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
base_url = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {"Authorization":f"Bearer {api_key}", "Content-Type":"application/json"}

class ChatStatus(Enum):
    ERROR = auto()

error_reason = {
    401: "Invalid API key. Check your key and try again.",
    429: "Rate limited. Too many requests or daily token limit hit.",
    500: "Server error on Groq's end.",
    503: "Groq service temporarily unavailable",
    404: "Model not found. Check if model name and base url are current."
}

def chat(messages, retries=3):
    for attempt in range(retries):
        r = requests.post(base_url, headers=HEADERS,
                        json={"model":"openai/gpt-oss-120b", "messages":messages})
        if r.status_code in (429, 500, 503):
            if attempt==retries-1:
                print("All retries failed. Please try again after some time.")
                return ChatStatus.ERROR
            reason = error_reason.get(r.status_code, "Unknown error")
            wait = 2**attempt
            print(f"Error {r.status_code} - {reason}\nWaiting {wait}s before retrying..")
            time.sleep(wait)
            continue
        elif not r.ok:
            reason = error_reason.get(r.status_code, "Unknown error")
            print(f"Error {r.status_code} - {reason}")
            return ChatStatus.ERROR
        else:
            return r.json()["choices"][0]["message"]["content"]

feeds = ["https://www.livemint.com/rss/markets",
         "https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms",
         "https://www.business-standard.com/rss/markets-106.rss"]

today = date.today()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

good_feeds = []

for feed in feeds:
    f = feedparser.parse(feed, request_headers=headers)
    try:
        if f.bozo:
            print(f"Something is wrong with this source: {feed}\nError: {f.bozo_exception}")
            continue
        if not f.entries:
            print(f"No entries returned for {feed}")
            continue
    except Exception as e:
        print(f"Something is wrong with this source: {feed}\nError: {e}")
        continue
    pubdate_str = f.entries[0].updated[5:16]
    pubdate = datetime.strptime(pubdate_str, "%d %b %Y").date()
    diff = today - pubdate
    if diff > timedelta(days=2): 
        print(f"Feed {feed} is outdated")
        continue
    good_feeds.append(f) 

if len(good_feeds) == 0:
    print("None of the feeds are up to date")
    exit()

news_items = []

for f in good_feeds:
    for entry in f.entries: 
        news_items.append({"title":entry.title,
                         **({"description":entry.description} if entry.description!=0 else {}),
                         "source":entry.link}) 

def find_comp(c, company_dict):

    if c in company_dict: 
        return c, company_dict[c]
    if c in company_dict.inverse:
        return company_dict.inverse[c], c
    
    all_searchable = list(company_dict.keys()) + list(company_dict.inverse.keys())
    best_match, score = process.extractOne(c, all_searchable)
    
    if score > 80:
        if best_match in company_dict:
            return company_dict[best_match], best_match
        else:
            return company_dict.inverse[best_match], best_match
    else:
        response = input(f"Did you mean {best_match}?  (y/n) ")
        if response=="y":
            return find_comp(best_match, company_dict)
        else:
            print(f"No match found for '{company}'. Exiting...")
            exit()

SUFFIXES = r'\s+(Limited|Ltd\.?|Corporation|Corp\.?|Co\.?|Company)\s*$'

def strip_suffix(name):
    prev = None
    while prev != name:
        prev = name
        name = re.sub(SUFFIXES, '', name, flags=re.IGNORECASE).strip()
    return name

def contains_term(text, term):
    pattern = r'\b' + re.escape(term.lower()) + r'\b'
    return bool(re.search(pattern, text.lower()))

def search_company(company_idents, snippets, mentions, mode):
    for snippet in snippets:
        if mode=="LOOKUP":
            if any(contains_term(v, x) for k, v in snippet.items() if k != "source" for x in company_idents): 
                mentions.append(snippet)
        elif mode=="NIFTY50":
            for company_name, ticker in company_idents.items():
                idents = [company_name, ticker]
                if any(contains_term(v, x) for k, v in snippet.items() if k != "source" for x in idents):
                    mentions.setdefault(company_name, []).append(snippet)
    return mentions

def summarize(mentions, system_prompt, user_prompt, mode, sectors): 
    if len(mentions)==0:
        print("No recent news found.")

    elif len(mentions)==1 and mode=="LOOKUP":
        m=mentions[0]
        print('\n'.join("{}: {}".format(k, v) for k, v in m.items()))

    elif mode=="LOOKUP":
        news = ""
        news = "\n\n".join(
        "\n".join(f"{k}: {v}" for k, v in m.items() if k != "source")
        for m in mentions)

        summary = chat([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt+f"\n\nSnippets:\n{news}"}])

        if summary == ChatStatus.ERROR:
            exit()
        else:
            print(summary)

    elif mode=="NIFTY50":
        sectors_grouped = defaultdict(list)
        for company_name in mentions:
            sector = sectors.get(company_name, "Unknown")
            sectors_grouped[sector].append(company_name)

        sector_blocks = []
        for sector, companies in sectors_grouped.items():
            company_blocks = []
            for company_name in companies:
                snippets = mentions[company_name]
                snippet_text = "\n".join(
                    "\n".join(f"{k}: {v}" for k, v in s.items() if k != "source")
                    for s in snippets
                )
                company_blocks.append(f"Company: {company_name}\n{snippet_text}")
            
            sector_text = "\n\n".join(company_blocks)
            if len(companies) >= 2:
                instruction = "[This sector has multiple companies — include a Sector Outlook after these entries.]"
            else:
                instruction = "[This sector has only one company — do NOT include a Sector Outlook for it.]"
            sector_blocks.append(f"Sector: {sector}\n{instruction}\n\n{sector_text}")

        news = "\n\n---\n\n".join(sector_blocks)

        summary = chat([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt+f"\n\nSnippets:\n{news}"}])

        if summary == ChatStatus.ERROR:
            exit()
        else:
            print(summary)
        


response = (input("This code offers two options: Lookup and NIFTY50\nLookup gives the option to search the latest any NSE listed company, while NIFTY50 provides latest snippets about NIFTY50 companies\nType 'Lookup' or 'NIFTY50' to activate either mode.\n")).upper()

if response=="LOOKUP":
    df = pd.read_excel('LISTED_COMPANIES_NSE.xlsx')

    companies_dict = bidict(pd.Series(df['SYMBOL'].values, index=df['NAME OF COMPANY']).to_dict())

    company = input("Enter ticker or company name (NSE listed): ").strip()

    identifier, ident = find_comp(company, companies_dict)

    identifier = strip_suffix(str(identifier))

    company_i = [identifier.lower(), str(ident).lower()]

    matches = []

    matches = search_company(company_i, news_items, matches, response)

    system_prompt_lookup = """You are a financial news analyst assistant. You will be given 
    one or more news snippets (title and description) about a single company. Write 
    ONE concise, flowing summary — 3-5 sentences, plain prose, no meta-commentary.

    Only mention whether something is a "report" or "analyst opinion" if it 
    materially changes how the reader should weigh the information — for example, 
    if a snippet is a stock recommendation, note who is recommending it. Otherwise, 
    just state what the snippets say. Do not explain your classification process, 
    do not repeatedly assert that something "is not" an opinion — simply write 
    the summary as if reporting the facts stated.

    If snippets conflict or add different angles, blend that into the prose 
    naturally rather than listing it as a separate point.

    Do not add outside information beyond what the snippets state. Write in plain 
    text only — no headers, no markdown."""

    user_prompt_lookup = f"Company: {ident} ({identifier})"

    summarize(matches, system_prompt_lookup, user_prompt_lookup, response, sectors={})

elif response=="NIFTY50":
    df = pd.read_excel('NIFTY50.xlsx')
    nifty50_idents = pd.Series(df['Symbol'].values, index=df['Company Name']).to_dict() 
    nifty50_idents = {strip_suffix(k): v for k, v in nifty50_idents.items()}
    matches = {}
    matches = search_company(nifty50_idents, news_items, matches, response)
    nifty50_sectors = pd.Series(df['Industry'].values, index=df['Company Name']).to_dict()
    nifty50_sectors = {strip_suffix(k): v for k, v in nifty50_sectors.items()}
    
    system_prompt_nifty50 = """You are a financial news analyst assistant producing a daily 
    Nifty 50 market report. You will be given news snippets grouped by sector, then 
    by company within each sector.

    For each company, write a concise summary of what the snippets report — focus 
    on factual reporting: earnings, price movement, announcements, regulatory 
    actions. Aim for 2-3 sentences; if there is very little information for a 
    company, a single sentence is fine — do not pad it out. Always preserve 
    specific numbers, percentages, dates, and figures exactly as stated in the 
    snippets — never round off, omit, or paraphrase away numerical details.

    After covering all companies in a sector, check the bracketed instruction 
    provided with that sector's data — it will explicitly tell you whether to 
    include a "Sector Outlook" note for that sector or to skip it entirely. 
    Follow that instruction exactly; do not add a Sector Outlook when told not to, 
    and do not omit one when told to include it.

    When a Sector Outlook is included, state plainly whether the companies in 
    that sector show a shared pattern (e.g. broadly positive earnings, a common 
    headwind, similar analyst sentiment) or whether their news is unrelated and 
    sector-independent. Do not force a pattern that isn't there — if the 
    companies' news has nothing in common, say so directly rather than inventing 
    a connective thread.
    
    Do NOT include analyst opinions, recommendations, or "buy/sell" pieces in the 
    per-company summaries at all — exclude them entirely from that section, even 
    briefly. Instead, collect every such opinion-based item, across every company, 
    into a single "Analyst Recommendations" section at the very end of the report. 
    For each item in that section, note the company, the recommending analyst or 
    source (if named), and the recommendation — kept short, a line or two per item. 
    This section covers all companies together, not broken out by sector.

    Format the output using markdown headers:
    - ## for each sector name
    - ### for each company name within it
    - ### Sector Outlook, after each sector's companies
    - A final ## Analyst Recommendations section at the very end, after all sectors

    Do not add outside information beyond what the snippets state. Do not repeat 
    disclaimers about what is or isn't an opinion within the per-company summaries 
    — that distinction is handled structurally, since opinion content is excluded 
    from those summaries entirely and placed only in the final section."""

    user_prompt_nifty50 = f"Today's date: {today.strftime('%d %B %Y')}\n\nGenerate the Nifty 50 report following the structure and rules above."

    summarize(matches, system_prompt_nifty50, user_prompt_nifty50, response, nifty50_sectors)

else:
    print("Response does not match either 'Lookup' or 'NIFTY50'")
    exit()