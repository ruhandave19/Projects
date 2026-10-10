import requests, json, time, random
from enum import Enum, auto
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import APIError

class ChatStatus(Enum):
    ERROR = auto()

error_reason = {
    401: "Invalid API key. Check your key and try again.",
    429: "Rate limited. Too many requests or daily token limit hit.",
    500: "Server error",
    503: "Service temporarily unavailable"
}
SYSTEM_INSTRUCTION = """
You are an expert Document Analysis AI. Your primary task is to read the provided PDF context and give direct, concise, and sufficient answers to the user's specific question.

Core Rules:
1. Primary Source: Base your answers strictly on the text extracted from the document.
2. Relevance & Brevity: Answer only what is asked. Omit any extra details, background context, or tangential information not directly required to address the question.
3. Accuracy: Do not introduce external facts or contradict the document content.
4. Boundaries: If a question is entirely outside the scope of the provided document, inform the user that the topic is not covered in the provided text.
"""

def error_handling(r, error_reason, attempt, llm_provider, retries):
    if llm_provider=="GROQ":
        status_code = r.status_code
    elif llm_provider=="GOOGLE":
        status_code = APIError.code
    if status_code in (429, 500, 503):
        if attempt==retries-1:
            print("\nAll retries failed. Please try again after some time.\n")
            return ChatStatus.ERROR
        reason = error_reason.get(status_code, "Unknown error")
        wait = 2**attempt
        print(f"\nError {status_code} - {reason}\nWaiting {wait}s before retrying..\n")
        time.sleep(wait)
        return True
    elif llm_provider=="GROQ" and (not r.ok):
        reason = error_reason.get(status_code, "Unknown error")
        print(f"\nError {status_code} - {reason}\n")
        return ChatStatus.ERROR

def chat(messages, stream_status, llm_provider, retries=2):
    load_dotenv()
    if llm_provider=="GROQ":
        api_key = os.getenv("GROQ_API_KEY")
        base_url = "https://api.groq.com/openai/v1/chat/completions"
        HEADERS = {"Authorization":f"Bearer {api_key}", "Content-Type":"application/json"}
        for attempt in range(retries):
            r = requests.post(base_url, headers=HEADERS,
                            json={"model":"openai/gpt-oss-120b", "messages":messages, "stream":stream_status},
                            stream=stream_status)
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
        for attempt in range(1, retries + 2):
            try: 
                r = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=messages,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                # temperature=0.1
            )
        )
                return r.text
            except APIError as e:
                print(f'Attempt {attempt}: Gemini call failed -> {e}')
                if attempt <= retries:
                    if e.code in (500, 503):
                        wait_time = min(5 * (2 ** (attempt - 1)), 30) 
                        wait_time += random.uniform(0, 2)
                        print(f'Waiting {wait_time:.1f} seconds before retrying...')
                        time.sleep(wait_time)
                else:
                    print(f"Error {e.code}: {e.message}")
                    return ChatStatus.ERROR
        print('GIVING UP: Gemini call failed after all retries')
        return ChatStatus.ERROR              