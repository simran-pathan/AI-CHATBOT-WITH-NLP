# AI-CHATBOT-WITH-NLP
COMPANY: CODTECH IT SOLUTIONS

NAME: SIMRAN AYUBKHAN PATHAN

INTERN ID: CT08KSV

DOMAIN: PYTHON

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

*CODE EXPLANATION *: 

This Python script implements a chatbot with a graphical user interface (GUI) using NLTK, SpaCy, and Tkinter. It provides an interactive chatbot experience with predefined responses and a simple GUI.

1. Libraries Used
NLTK (Natural Language Toolkit): Provides NLP functions like tokenization and chatbot utilities.
SpaCy: Processes user input to improve response handling.
Tkinter: Builds the GUI for chatbot interaction.
Random: Generates varied responses for more natural conversation.

2. Chatbot Logic
The chatbot uses regular expressions (regex) to match user inputs to predefined responses (pairs list).
The Chat class from nltk.chat.util handles pattern-based responses.
If no matching response is found, a random fallback response is chosen.

3. GUI Implementation
The chatbot interface is built using Tkinter, featuring:
ScrolledText Widget: Displays conversation history.
Entry Widget: Takes user input.
Button & Enter Key: Triggers message sending.
Color-coded messages: User messages are blue, bot responses are green.

4. Key Features
Welcome message at startup.
Handles basic conversations like greetings, jokes, AI discussions, and general queries.
Exit command handling (bye, exit, quit) to gracefully close the application.
Tkinter GUI Styling: Uses custom colors and fonts for a user-friendly appearance.

5. Execution Flow
User inputs a message.
Chatbot matches it to a predefined pattern.
Response is displayed in the GUI.
Chat continues until the user exits.

*OUTPUT*:
