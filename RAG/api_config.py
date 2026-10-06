import requests, json, time
from enum import Enum, auto
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

class ChatStatus(Enum):
    ERROR = auto()

error_reason = {
    401: "Invalid API key. Check your key and try again.",
    429: "Rate limited. Too many requests or daily token limit hit.",
    500: "Server error on Groq's end.",
    503: "Groq service temporarily unavailable"
}

SYSTEM_INSTRUCTION = """
You are an expert Document Analysis AI. Your primary task is to read the provided PDF context and give direct, accurate, and structured answers.

Core Rules:
1. Primary Source: Base your answers directly on the text extracted from the document.
2. Accuracy: Do not introduce external facts or contradict the document content.
3. Clarity: Structure your responses cleanly using bullet points or concise paragraphs where appropriate.
4. Boundaries: If a question is entirely outside the scope of the provided document, inform the user that the topic is not covered in the provided text.
"""

def error_handling(r, error_reason, attempt, retries):
    if r.status_code in (429, 500, 503):
        if attempt==retries-1:
            print("\nAll retries failed. Please try again after some time.\n")
            return ChatStatus.ERROR
        reason = error_reason.get(r.status_code, "Unknown error")
        wait = 2**attempt
        print(f"\nError {r.status_code} - {reason}\nWaiting {wait}s before retrying..\n")
        time.sleep(wait)
        return True
    elif not r.ok:
        reason = error_reason.get(r.status_code, "Unknown error")
        print(f"\nError {r.status_code} - {reason}\n")
        return ChatStatus.ERROR

def chat(messages, stream_status, llm_provider, retries=3):
    load_dotenv()
    if llm_provider=="GROQ":
        api_key = os.getenv("GROQ_API_KEY")
        base_url = "https://api.groq.com/openai/v1/chat/completions"
        HEADERS = {"Authorization":f"Bearer {api_key}", "Content-Type":"application/json"}
        for attempt in range(retries):
            r = requests.post(base_url, headers=HEADERS,
                            json={"model":"openai/gpt-oss-120b", "messages":messages, "stream":stream_status},
                            stream=stream_status)
            result = error_handling(r, error_reason, attempt, retries)
            if result is True:
                continue
            elif result == ChatStatus.ERROR:
                return ChatStatus.ERROR
            if stream_status:
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
            else:
                data = r.json()
                full_reply = data["choices"][0]["message"]["content"] 
            return full_reply
    elif llm_provider=="GOOGLE":
        client = genai.Client()
        for attempt in range(retries):
            response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=messages,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                # temperature=0.1
            )
        )
            result = error_handling(r, error_reason, attempt, retries)
            if result is True:
                continue
            elif result == ChatStatus.ERROR:
                return ChatStatus.ERROR
            return response.text