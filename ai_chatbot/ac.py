import requests, json, os
from dotenv import load_dotenv
from enum import Enum, auto

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
base_url = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {"Authorization":f"Bearer {api_key}", "Content-Type":"application/json"}

class ChatStatus(Enum):
    ERROR = auto()

def chat(messages):
    r = requests.post(base_url, headers=HEADERS,
                      json={"model":"llama-3.3-70b-versatile", "messages":messages})
    if not r.ok:
        print(f"Something went wrong: Error {r.status_code}")
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