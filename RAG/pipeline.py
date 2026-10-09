import pymupdf, chromadb
from chromadb.errors import NotFoundError
from sentence_transformers import SentenceTransformer

def text_extraction(pdf_add):
    pdf = pymupdf.open(pdf_add)
    text = ""
    page_boundaries = []
    for page in pdf:
        start_offset = len(text)
        text += page.get_text()
        end_offset = len(text)-1
        page_boundaries.append((page.number+1, start_offset, end_offset))
    return text, page_boundaries

def chunked_text(text, chunk_size=500, overlap=50):
    chunks = []
    offsets = []
    start = 0
    end = chunk_size
    while start < len(text):
        while True:
            if text[end-1] in ("!", "?", "."):
                break
            end -= 1
            if end == start:
                end = start + chunk_size
                break
        chunks.append(text[start:end])
        offsets.append((start,end)) 
        start += chunk_size - overlap
        anchor = start
        while start<len(text):
            if text[start-2] in ("!", "?", "."):
                break
            start -= 1
            if start <= anchor - 100:
                start = anchor
                break
        if (start + chunk_size) >= len(text):
            end = len(text)
            continue
        end = start + chunk_size
    return chunks, offsets


def find_page_no(boundaries, index):
    for boundary in boundaries:
        if boundary[1]<=index<=boundary[2]:
            return boundary[0]


def store_data(segments, spans, boundaries):
    ids = [f"id{i}" for i in range(len(segments))]
    chunk_data = []
    for i, chunk_info in enumerate(zip(segments, spans)):
        start_index = chunk_info[1][0]
        start_p = find_page_no(boundaries, start_index)
        end_index = chunk_info[1][1]
        end_p = find_page_no(boundaries, end_index)
        chunk_data.append((ids[i], chunk_info[0], start_p, end_p))  
    return chunk_data, ids


def embedding(segments, ids, script):
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    embedding = model.encode(segments)

    persist_dir = "./chroma_data"
    client = chromadb.PersistentClient(path=persist_dir)
    
    try:
        if script=="PA":
            client.delete_collection("pdf_text")
            collection = client.create_collection("pdf_text")
        elif script=="EVAL":
            client.delete_collection("eval_text")
            collection = client.create_collection("eval_text")

    except NotFoundError:
        if script=="PA":
            collection = client.create_collection("pdf_text")
        elif script=="EVAL":
            collection = client.create_collection("eval_text")

    collection.add(
        documents=segments,
        embeddings=[e.tolist() for e in embedding],
        ids=ids
    )
    return model, collection


def retrieval(prompt, model, collection):
    query_embedding = [model.encode(prompt)]
    results = collection.query(
    query_embeddings=query_embedding,
    n_results=5
    )
    retrived_chunks = results["documents"][0]
    context = "\n\n".join(retrived_chunks)
    return results, context