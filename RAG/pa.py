import sys, sqlite3
from api_config import ChatStatus, chat
from pipeline import text_extraction, chunked_text, store_data, embedding, retrieval

con = sqlite3.connect("chunks_queries.db")
cur = con.cursor()

pdf_path = sys.argv[1]

text, page_boundaries = text_extraction(pdf_path)

chunks, offsets = chunked_text(text)

chunk_data, ids = store_data(chunks, offsets, page_boundaries)

cur.execute("CREATE TABLE IF NOT EXISTS chunk_store(chunk_id TEXT PRIMARY KEY, chunk_text TEXT, start_page INTEGER, end_page INTEGER)")
cur.execute("DELETE FROM chunk_store")
cur.executemany("INSERT INTO chunk_store VALUES(?, ?, ?, ?)", chunk_data)
con.commit()

model, collection = embedding(chunks, ids, script="PA")

cur.execute("PRAGMA foreign_keys = ON") 
cur.execute("CREATE TABLE IF NOT EXISTS queries(query_id INTEGER PRIMARY KEY, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, query_text TEXT, reply TEXT)")
cur.execute("DELETE FROM queries")
cur.execute("CREATE TABLE IF NOT EXISTS query_chunks(query_id INTEGER, chunk_id TEXT, FOREIGN KEY (query_id) REFERENCES queries(query_id), FOREIGN KEY (chunk_id) REFERENCES chunk_store(chunk_id))")
cur.execute("DELETE FROM query_chunks")
con.commit()

print("Type 'Bye' to exit the conversation")
print("Assistant: Hi there! I've received your PDF and loaded it up.\nHow can I help you with the document today?")
while (True):
    messages = []
    query = input("User: ")
    if query=="Bye":
        print("Assistant: Goodbye. It was nice talking to you!")
        con.close()
        break
    results, context = retrieval(query, model, collection)
    prompt = f"""Answer the question based on the context below.
    If the answer is not in the context, say so.
    Context:
    {context}
    Question: {query}"""
    messages.append({"role":"user", "content":prompt})
    print("Assistant: ", end="")
    reply = chat(messages, llm_provider="GROQ", stream_status=True)
    if reply==ChatStatus.ERROR: 
        con.close()
        break
    cur.execute("INSERT INTO queries(query_text, reply) VALUES(?, ?)", (query, reply)) 
    current_loop_query_id = cur.lastrowid
    query_chunk_list = []
    for chunk_id in results["ids"][0]:
        query_chunk_list.append((current_loop_query_id, chunk_id))
    cur.executemany("INSERT INTO query_chunks(query_id, chunk_id) VALUES (?, ?)", query_chunk_list)
    con.commit()