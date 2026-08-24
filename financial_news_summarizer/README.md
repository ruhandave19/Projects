# NSE Financial News Summariser

A terminal-based financial news tool with two modes: look up the latest news on any NSE-listed company, or get a synthesised daily report across all Nifty 50 constituents — grouped by sector, with analyst opinions kept separate from factual reporting.

## Features
- **Lookup mode** — search any NSE-listed company by name or ticker, get a synthesised summary of recent news mentioning it
- **NIFTY50 mode** — scans news for all fifty Nifty 50 constituents, groups results by sector, and generates a structured report with per-company summaries and sector-level pattern analysis
- Fuzzy matching (`thefuzz`) with a bidirectional name↔ticker lookup (`bidict`) — typos, partial names, and either name or ticker all resolve correctly
- Pulls live headlines from three RSS sources (LiveMint, Economic Times, Business Standard) — no news API, no rate limits, no key required
- Feed freshness checked before use — stale or malformed sources are automatically skipped
- Word-boundary regex matching prevents false positives (e.g. "BEL" no longer matches inside "believe")
- Corporate suffix normalisation ("Ltd", "Limited", "Co.", "Corporation") so company names match news text reliably
- Report/opinion distinction — analyst recommendations are structurally separated from factual reporting, never presented as confirmed fact
- Sector Outlook only generated when a sector has 2+ companies with news — enforced deterministically in Python, not left to the LLM to judge
- Graceful error handling for rate limits, invalid API keys, and server errors with exponential backoff retry
- API key protected using a `.env` file via `python-dotenv`
- Error states handled cleanly using Python's `Enum` module

## How to Run
1. Clone this repository
```bash
git clone https://github.com/ruhandave19/Projects.git
```
2. Create and activate a virtual environment
```bash
python -m venv .venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```
3. Navigate into the project root
```bash
cd Projects
cd financial_news_summariser
```
4. Install dependencies
```bash
pip install -r requirements.txt
```
5. Sign up at https://console.groq.com and create a free API key
6. Create a file named `.env` in the project root and add:
```
GROQ_API_KEY=your_key_here
```
7. Place `LISTED_COMPANIES_NSE.xlsx` (full NSE equity list) and `NIFTY50.xlsx` (Nifty 50 constituents with sector data, from niftyindices.com) in the project root
8. Run the script
```bash
py finns.py
```

## Example Output — Lookup Mode
```bash
This code offers two options: Lookup and NIFTY50
Type 'Lookup' or 'NIFTY50' to activate either mode.
Lookup
Enter ticker or company name (NSE listed): Aether Industries
Aether Industries was named among five breakout stocks recommended by Sumeet
Bagadia today, alongside Dilip Buildcon, Syrma SGS Technology, Steelcast, and
Vimta Labs...
```

## Example Output — NIFTY50 Mode
```bash
## Fast Moving Consumer Goods
### Hindustan Unilever
Hindustan Unilever was part of the Sensex since inception, reflecting India’s evolving economy. The company's market valuation increased along with Bharti Airtel, Bajaj Finance, Larsen & Toubro, Life Insurance Corporation of India (LIC), adding Rs 55,149.45 crore in market valuation collectively.
### ITC
ITC was also part of the Sensex since inception, reflecting India’s evolving economy.
### Sector Outlook
The Fast Moving Consumer Goods sector companies, such as Hindustan Unilever and ITC, have been part of the Sensex since inception, showing enduring relevance in the Indian market, but their recent performances have been vastly different.

## Telecommunication
### Bharti Airtel
Bharti Airtel's market valuation increased along with Bajaj Finance, Larsen & Toubro, Life Insurance Corporation of India (LIC), and Hindustan Unilever, adding Rs 55,149.45 crore in market valuation collectively.

## Construction
### Larsen & Toubro
Larsen & Toubro's market valuation increased along with Bharti Airtel, Bajaj Finance, Life Insurance Corporation of India (LIC), and Hindustan Unilever, adding Rs 55,149.45 crore in market valuation collectively.

## Analyst Recommendations
* Bharat Electronics: Recommended by Ganesh Dongre of Anand Rathi to buy.
* Reliance Industries: Part of the nine Sensex stocks that offer a potential upside of 20% to 41% over the next 12 months.
* Axis Bank: Among the nine Sensex stocks that offer a potential upside of 20% to 41% over the next 12 months.
* HDFC Bank: Leads the list of nine Sensex stocks that offer a potential upside of 20% to 41% over the next 12 months.
* NTPC: Among the nine Sensex stocks that offer a potential upside of 20% to 41% over the next 12 months.
```

## Known Limitations
- RSS feeds only surface a rolling window of recent articles, not historical depth — suited to "what's happening now," not backtesting or trend analysis over time
- Companies whose only news is an analyst recommendation still receive a (thin) per-company summary section rather than being excluded from the main report entirely
- Multiple Nifty 50 constituents mentioned within a single source article are currently treated as independent mentions, which can make one story appear to "support" a sector pattern across several unrelated sectors
- Business Standard's RSS feed occasionally blocks automated access even with a browser User-Agent set — the pipeline degrades gracefully and continues on the remaining two sources when this happens
- Company and sector reference data (NSE equity list, Nifty 50 constituents) is bundled 
as a static snapshot rather than fetched live — may drift from actual listings over time
- Model name is hardcoded (`openai/gpt-oss-120b`) — LLM providers periodically deprecate models 
with limited notice (Groq retired the originally-used `llama-3.3-70b-versatile` in August 2026), 
which can silently break the pipeline until the model string is manually updated

## Planned for v2.0
- Exclude companies whose only news is analyst opinion from the main per-company section entirely
- Detect and flag when multiple companies are drawn from the same source article, rather than treating each mention as independent
- Fetch NSE equity list and Nifty 50 constituents live at runtime (cached locally, refreshed 
every 7-14 days) instead of relying on static bundled snapshots
- Verify the configured LLM model is still available via Groq's `/models` endpoint at startup, 
and fail with a clear error message rather than a raw 404 if it has been deprecated