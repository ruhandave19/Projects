import sys, sqlite3, json
from api_config import ChatStatus, chat
from pipeline import text_extraction, chunked_text, store_data, embedding, retrieval

con = sqlite3.connect("eval_queries.db")
cur = con.cursor()

pdf_path = r"C:\Users\Ruhan\Documents\Nationalism in Europe.pdf"

text, page_boundaries = text_extraction(pdf_path)

chunks, offsets = chunked_text(text)

chunk_data, ids = store_data(chunks, offsets, page_boundaries)

cur.execute("CREATE TABLE IF NOT EXISTS chunk_store(chunk_id TEXT PRIMARY KEY, chunk_text TEXT, start_page INTEGER, end_page INTEGER)")
cur.execute("DELETE FROM chunk_store")
cur.executemany("INSERT INTO chunk_store VALUES(?, ?, ?, ?)", chunk_data)
con.commit()

model, collection = embedding(chunks, ids)

with open("eval_questions.json", "r") as f:
    eval_questions = json.load(f)

cur.execute("CREATE TABLE IF NOT EXISTS eval_runs(question_id INTEGER PRIMARY KEY, page_check TEXT, chunk_text TEXT, api_response TEXT)")
cur.execute("DELETE FROM eval_runs")
con.commit()

for entry in eval_questions:
    messages = []
    query = entry["question"]
    results, context = retrieval(query, model, collection) # take a look at the general structure of results
    count = 0
    # res = cur.execute("SELECT start_page, end_page FROM chunk_store WHERE chunk_id=id;")
    res = cur.execute("SELECT start_page, end_page FROM chunk_store WHERE chunk_id IN (?, ?, ?, ?, ?)", tuple(results["ids"][0])) # cannot insert variables into SQL as it is, have to use '?'. And it expects a tuple, not a list.
    page_list = res.fetchall()  # fetchall() always returns a list of tuples [(1,2,), (2,2,), ...]
    expected_page = entry["expected_page"]
    check = expected_page if isinstance(expected_page, list) else [expected_page]
    page_counts = {item: 0 for item in check}
    for t in page_list:
        for item in check:
            if item in t:
                page_counts[item] += 1
    page_check = ""
    for k,v in page_counts.items():
        page_check += "Page number {k} was found in {v} chunks. "
    prompt = f"""Answer the question based on the context below.
    If the answer is not in the context, say so.
    Context:
    {context}
    Question: {query}"""
    messages.append({"role":"user", "content":prompt})
    response = chat(messages, stream_status=False)
    if response==ChatStatus.ERROR: 
        con.close()
        exit()
    cur.execute("INSERT INTO eval_runs(question_id, page_check, chunk_text, api_response) VALUES(?, ?, ?, ?)", (entry["id"], page_check, context, response))
con.commit()
con.close()