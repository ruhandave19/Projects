import sys, sqlite3
from api_config import ChatStatus, chat
from pipeline import text_extraction, chunked_text, store_data, embedding, retrieval

con = sqlite3.connect("chunks_queries.db")
cur = con.cursor()

pdf_path = sys.argv[1]

text, page_boundaries = text_extraction(pdf_path)

chunks, offsets = chunked_text(text)

# for chunk in chunks:
#     start_index = text.index(chunk)

# for i in range(len(chunks)):
#     chunk_data.append((id[i], chunks[i]))

# I wanted to do the above two in the same for loop, and enumerate returns (index, item) for a particular list

# for i, chunk_info in enumerate(zip(chunks, offsets)):
#     start_index = text.index(chunk)  -- this is incorrect and may not return proper start index for a chunk
#     start_p = find_page_no(page_boundaries, start_index)
#     end_index = text.index(chunk) + len(chunk) - 1
#     end_p = find_page_no(page_boundaries, end_index)
#     chunk_data.append((id[i], chunk, start_p, end_p))

chunk_data, ids = store_data(chunks, offsets, page_boundaries)

cur.execute("CREATE TABLE chunk_store(chunk_id TEXT PRIMARY KEY, chunk_text TEXT, start_page INTEGER, end_page INTEGER)")
cur.executemany("INSERT INTO chunk_store VALUES(?, ?, ?, ?)", chunk_data)
con.commit()

model, collection = embedding(chunks, ids)

cur.execute("PRAGMA foreign_keys = ON") # important otherwise foreign keys will not get recognized
cur.execute("CREATE TABLE queries(query_id INTEGER PRIMARY KEY, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, query_text TEXT, reply TEXT)")
cur.execute("CREATE TABLE query_chunks(query_id INTEGER, chunk_id TEXT, FOREIGN KEY (query_id) REFERENCES queries(query_id), FOREIGN KEY (chunk_id) REFERENCES chunk_store(chunk_id))") #need to delcare the column names separately even when using FOREIGN key, and FOREIGN key requires a separate declaration
con.commit()

print("Type 'Bye' to exit the conversation")
print("Assistant: Hi there! I've received your PDF and loaded it up.\nHow can I help you with the document today?")
while (True):
    messages = []
    query = input("User: ")
    if query=="Bye":
        print("Assistant: Goodbye. It was nice talking to you!")
        con.close() # it's important to do this on all the exit paths
        break
    results, context = retrieval(query, model, collection)
    prompt = f"""Answer the question based on the context below.
    If the answer is not in the context, say so.
    Context:
    {context}
    Question: {query}"""
    messages.append({"role":"user", "content":prompt})
    print("Assistant: ", end="")
    reply = chat(messages, stream_status=True)
    if reply==ChatStatus.ERROR: 
        con.close()
        break
    # cur.executemany("INSERT INTO queries (query, response) VALUES(?, ?)", query, reply)  -- executemany is for multiple rows, I only need to insert a single row here
    # cur.execute("INSERT INTO queries (query, response) VALUES(?, ?)", query, reply) - execute and executemany require only two arguments, one the SQL INSERT, and the other, a python object that bundles all the values to be inserted together
    cur.execute("INSERT INTO queries(query_text, reply) VALUES(?, ?)", (query, reply)) # it was better to INSERT both query and reply together, because assuming if Ctrl+C is pressed in middle of the loop, only the query being saved to the table doesnt make sense, it's nothing without the response
    current_loop_query_id = cur.lastrowid
    query_chunk_list = []
    for chunk_id in results["ids"][0]:
        query_chunk_list.append((current_loop_query_id, chunk_id))
    cur.executemany("INSERT INTO query_chunks(query_id, chunk_id) VALUES (?, ?)", query_chunk_list)
    con.commit()
    # if reply==ChatStatus.ERROR: -- need to check for error before inserting any values in the table
    #     break