# PDF Q&A Terminal Script

A terminal-based PDF question-answering script that lets you query any PDF in natural language, built using a RAG (Retrieval-Augmented Generation) pipeline with raw HTTP requests.

## Features
- Point the script at any PDF of your choice via the command line
- Sentence boundary chunking implemented from scratch — no LangChain or LlamaIndex
- Embeddings generated locally using `sentence-transformers`, no additional API key needed
- Embeddings stored and retrieved using ChromaDB, running as a local file with no server needed
- Each query is stateless — only the retrieved context and current question are passed to the LLM
- Graceful error handling for rate limits, invalid API keys, and server errors with exponential backoff retry
- Streaming responses at readable speeds
- API key protected using a `.env` file via `python-dotenv`
- Error states handled cleanly using Python's `Enum` module
- Type `Bye` to exit the conversation gracefully — response is hardcoded to save API tokens

## How to Run
1. Clone this repository
```bash
git clone https://github.com/ruhandave19/Projects.git
```
2. Create and activate a virtual environment
```bash
pythom -m venv .venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```
3. Navigate into the project root
```bash
cd Projects
cd pdf_answering
```
4. Install dependencies 
```bash
pip install -r requirements.txt
```
5. Sign up at https://console.groq.com and create a free API key
6. Create a file named `.env` in the project root and add:
GROQ_API_KEY=your_key_here
7. Run the script with a pdf of your choice
```bash
py pa.py path/to/your/document.pdf
```

## Example Output
```bash
Type 'Bye' to exit the conversation
Assistant: Hi there! I've received your PDF and loaded it up.
How can I help you with the document today?    
User: What is the main topic of this document?
Assistant: Based on the provided context, the document discusses...
User: Bye
Assistant: Goodbye. It was nice talking to you!
```

## Known Limitations
- Chunking is sentence boundary based — retrieval quality may suffer on complex or implicit questions
- Semantic chunking and improved retrieval planned for v2.0