The projects in this repository are:

(1) Project 1: fibonacci_printer (C)

This takes input from the user and prints fibonacci series upto the position inputted by the user. 

(2) Project 2: unit_converter (C)

This gives options to the user to select which set of conversion (from one unit to another) is to be carried out. 
The user is kept on being given options until a particular input is given to terminate.

(3) Project 3: password_security_toolkit (Python)

Consists of 3 projects:

(a) Password Strength Analyzer: This takes a password input from the user and returns a score (WEAK/MODERATE/STRONG/VERY STRONG)

(b) Password Generator: This generates a password of length 30 with atleast one uppercase letter, one lowercase letter, one character and one digit.

(c) Demo: This allows the user to make a custom password (ie, with custom length, type of characters to be used) with the generator which then uses the analyzer to give a rating to the generated password.

(4) Project 4: 4_bit_adder_subtractor (Python)

This demonstrates the logic behind a 4 bit adder subtractor eith the help of user input.

(5) Project 5: iris_classifier (Python)

Consists of 2 projects:

(a) Iris accuracy: Showcases the accuracy at which iris dataset can be predicted

(b) Iris predict: Predicts the species based on user input measurements.

(6) Project 6: port_scanner (Python)

Allows users to scan ports on their system

(7) Project 7: ai_chatbot (Python)

A terminal-based chatbot built using the Groq API with raw HTTP requests, 
streaming responses, and graceful error handling.

(8) Project 8: RAG (Python), v2.0 [previously pdf_answering]

Consists of 2 parts that share one retrieval pipeline:

(a) PDF Answering (pa.py): A terminal-based PDF question-answering script using a RAG pipeline: sentence boundary chunking with page tracking, local embeddings via sentence-transformers, ChromaDB for vector storage, and an LLM for answer synthesis over raw HTTP requests with streaming and retry logic. A SQLite database logs the chunks (with their pages), every question and answer, and the chunks retrieved for each answer.

(b) Evaluation (evals.py): Runs 20 fixed questions with known answers and expected pages against an openly licensed OpenStax chapter. It checks automatically whether retrieval found the right pages, logs each run to SQLite for manual answer grading, and paces its Gemini API calls to stay within free-tier limits.

(9) Project 9: financial_news_summarizer (Python)

A terminal tool that scans NSE/Nifty 50 news via RSS and 
LLM synthesis, distinguishing factual reporting from analyst opinion across per-company 
and sector-wide views.