# Terminal AI Chatbot

A terminal-based AI chatbot built using the Groq API with raw HTTP requests.

## Features
- Engage in a multi-turn conversation with an LLM directly from your terminal
- Type `Bye` to end the conversation gracefully
- API key protected using a `.env` file via `python-dotenv`
- Error states handled cleanly using Python's `Enum` module

## How to Run
```bash
#Clone this repository
git clone https://github.com/ruhandave19/Projects.git
#Create and activate a virtual environment
pythom -m venv .venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
#Navigate into the project root
cd Projects
cd ai_chatbot
#Install dependencies 
pip install -r requirements.txt
#Get a Groq API key
Sign up at https://console.groq.com and create a free API key
#Create the .env file
Create a file named `.env` in the project root and add:
GROQ_API_KEY=your_key_here
#Run the script
py ac.py
```

## Example Output
```bash
Type 'Bye' to exit the conversation
User: Hello, my name is Ajay.                        
Assistant: Hello Ajay! It's nice to meet you. Is there something I can help you with or would you like to chat?
User: Not really.
Assistant: Sometimes it's nice just to say hello. If you change your mind or need anything in the future, feel free to reach out. Have a great day, Ajay!
User: Bye # "Bye" is the exit keyword, and the goodbye reply below is hardcoded to save tokens
Assistant: Goodbye. It was nice talking to you!
```

## Changelog

### v2.0
- Added graceful error handling for rate limits, invalid API keys, and server errors
- Added exponential backoff retry for transient errors (429, 500, 503)
- Added streaming responses

### v1.0
- Initial release