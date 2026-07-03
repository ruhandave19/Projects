import requests, json, os, time
from dotenv import load_dotenv
from enum import Enum, auto

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
                        json={"model":"llama-3.3-70b-versatile", "messages":messages})
        reason = error_reason.get(r.status_code, "Unknown error")
        if r.status_code in (429, 500, 503):
            if attempt==retries-1:
                print("All retries failed. Please try again after some time.")
                return ChatStatus.ERROR
            wait = 2**attempt
            print(f"Error {r.status_code}: {reason}\nWaiting {wait}s before retrying..")
            time.sleep(wait)
            continue
        elif not r.ok:
            print(f"Error {r.status_code}: {reason}")
            return ChatStatus.ERROR
        return r.json()["choices"][0]["message"]["content"]

messages = []
print("Type 'Bye' to exit the conversation")

while (True):
    query = input("User: ")
    if query=="Bye":
        print("Assistant: Goodbye. It was nice talking to you!")
        break
    messages.append({"role":"user", "content":query})
    reply = chat(messages)
    if reply==ChatStatus.ERROR:
        break
    print("Assistant: ", reply)
    messages.append({"role":"assistant", "content":reply})