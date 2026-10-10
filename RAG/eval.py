import sqlite3, json, time
from api_config import ChatStatus, chat
from pipeline import text_extraction, chunked_text, store_data, embedding, retrieval

con = sqlite3.connect("eval_queries.db")
cur = con.cursor()

pdf_path = "data/Ancient_Greece.pdf"

text, page_boundaries = text_extraction(pdf_path)

chunks, offsets = chunked_text(text)

chunk_data, ids = store_data(chunks, offsets, page_boundaries)

cur.execute("CREATE TABLE IF NOT EXISTS chunk_store(chunk_id TEXT PRIMARY KEY, chunk_text TEXT, start_page INTEGER, end_page INTEGER)")
cur.execute("DELETE FROM chunk_store")
cur.executemany("INSERT INTO chunk_store VALUES(?, ?, ?, ?)", chunk_data)
con.commit()

model, collection = embedding(chunks, ids, script="EVAL")

with open("eval_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    eval_questions = data["questions"]

cur.execute("CREATE TABLE IF NOT EXISTS eval_runs(question_id INTEGER PRIMARY KEY, page_check TEXT, question TEXT, chunk_text TEXT, expected_answer TEXT, api_response TEXT)")
cur.execute("DELETE FROM eval_runs")
con.commit()

for entry in eval_questions:
    query = entry["question"]
    results, context = retrieval(query, model, collection) 
    count = 0
    res = cur.execute("SELECT start_page, end_page FROM chunk_store WHERE chunk_id IN (?, ?, ?, ?, ?)", tuple(results["ids"][0])) 
    page_list = res.fetchall()  
    expected_page = entry["expected_page"]
    check = expected_page if isinstance(expected_page, list) else [expected_page]
    page_counts = {item: 0 for item in check}
    for t in page_list:
        for item in check:
            if item in t:
                page_counts[item] += 1
    page_check = ""
    for k,v in page_counts.items():
        page_check += f"Page number {k} was found in {v} chunks. "
    prompt = f"""Answer the question based on the context below.
    Context:
    {context}
    Question: {query}"""
    start = time.monotonic()
    response = chat(prompt, stream_status=False, llm_provider="GOOGLE")
    if response==ChatStatus.ERROR: 
        con.close()
        exit()
    cur.execute("INSERT INTO eval_runs(question_id, page_check, question, chunk_text, expected_answer, api_response) VALUES(?, ?, ?, ?, ?, ?)", (entry["id"], page_check, entry["question"], context, entry["expected_answer"], response))
    end = time.monotonic()
    elapsed_time = end - start
    if elapsed_time<5:
        time.sleep(5-elapsed_time)
con.commit()
con.close()