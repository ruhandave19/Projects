This project features a terminal based AI Chatbot created using Groq API, without using the SDK.

It allows the user to engage in a basic conversation with AI on their terminal, and the freedom to
end the conversation with a trigger word.

dotenv is used to ensure safety and privacy of the user by hiding the API key.

The code also accounts for possible errors with the use of 'Enum' module.

To run the code:
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

Example output:
```bash
Type 'Bye' to exit the conversation
User: Hello, my name is Ajay.                        
Assistant: Hello Ajay! It's nice to meet you. Is there something I can help you with or would you like to chat?
User: Not really.
Assistant: Sometimes it's nice just to say hello. If you change your mind or need anything in the future, feel free to reach out. Have a great day, Ajay!
User: Bye # "Bye" is the exit keyword, and the goodbye reply below is hardcoded to save tokens
Assistant: Goodbye. It was nice talking to you!
```