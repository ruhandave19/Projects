import pymupdf, chromadb, requests, json, sys, os, time
from sentence_transformers import SentenceTransformer
from chromadb.config import Settings
from dotenv import load_dotenv
from enum import Enum, auto

pdf_path = sys.argv[1]
pdf = pymupdf.open(pdf_path)

text = ""

for page in pdf:
    text += page.get_text()

def chunked_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    end = 500
    while start < len(text):
        while True:
            if text[end-1] in ("!", "?", "."):
                break
            end -= 1
        chunks.append(text[start:end])
        start += chunk_size - overlap
        while start<len(text):
            if text[start-2] in ("!", "?", "."):
                break
            start -= 1
        if (start + chunk_size) >= len(text):
            end = len(text)
            continue
        end = start + chunk_size
    return chunks

chunks = chunked_text(text)

ids = [f"id{i}" for i in range(len(chunks))]

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

embedding = model.encode(chunks)

persist_dir = "./chroma_data"
client = chromadb.PersistentClient(path=persist_dir)

collection = client.get_or_create_collection("pdf_text")

collection.add(
    documents=chunks,
    embeddings=[e.tolist() for e in embedding],
    ids=ids
)

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
    503: "Groq service temporarily unavailable"
}

def chat(messages, retries=3):
    for attempt in range(retries):
        r = requests.post(base_url, headers=HEADERS,
                        json={"model":"llama-3.3-70b-versatile", "messages":messages, "stream":True},
                        stream=True)
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
        full_reply = ""
        for line in r.iter_lines():
            if not line:
                continue
            line = line.decode("utf-8")
            if line.startswith("data: "):
                data = line[6:]
                if data == "[DONE]":
                    print()
                    break
            try:
                chunk = json.loads(data)
                delta = chunk["choices"][0]["delta"].get("content", "")
                time.sleep(0.03)
                print(delta, end="", flush=True)
                full_reply += delta
            except:
                pass
        return full_reply


print("Type 'Bye' to exit the conversation")
print("Assistant: Hi there! I've received your PDF and loaded it up.\nHow can I help you with the document today?")
while (True):
    messages = []
    query = input("User: ")
    if query=="Bye":
        print("Assistant: Goodbye. It was nice talking to you!")
        break
    query_embedding = [model.encode(query)]
    results = collection.query(
    query_embeddings=[e.tolist() for e in query_embedding],
    n_results=5
    )
    retrived_chunks = results["documents"][0]
    context = "\n\n".join(retrived_chunks)
    prompt = f"""Answer the question based on the context below.
    If the answer is not in the context, say so.
    Context:
    {context}
    Question: {query}"""
    messages.append({"role":"user", "content":prompt})
    print("Assistant: ", end="")
    reply = chat(messages)
    if reply==ChatStatus.ERROR:
        break