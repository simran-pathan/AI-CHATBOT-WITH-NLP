import nltk
import random
import spacy
import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

# Downloading the NLTK resources are for making them available for utilization
nltk.download("punkt")
nlp = spacy.load("en_core_web_sm")

# Defining chatbot responses 
pairs = [
    [r"hi|hello|hey", ["Hello! How's your day going?", "Hey there! Ready to chat?", "Hi! What’s on your mind?"]],
    [r"how are you", ["I'm just a bot, but I'm feeling great! What about you?", "I'm good! Hope you're having an awesome day!"]],
    [r"what is your name", ["I'm your friendly chatbot! You can call me ChatBuddy!", "I go by ChatBot, but you can give me a cool name if you’d like!"]],
    [r"bye|goodbye", ["Goodbye! It was fun chatting with you!", "See you later! Stay awesome!", "Take care and talk to you soon!"]],
    [r"(.*) your name(.*)", ["I am ChatBuddy, your AI-powered friend! What’s your name?" ]],
    [r"(.*) help (.*)", ["I can assist you with basic queries! You can ask about my name, greetings, or even how I'm doing."]],
    [r"(.*) weather(.*)", ["I don't have live weather updates yet, but you can check online for the latest forecast. What's the weather like where you are?"]],
    [r"(.*) (time|date)(.*)", ["I can’t tell the exact time, but your device can! Want me to remind you of something?"]],
    [r"(.*) joke(.*)", ["Why don’t skeletons fight each other? Because they don’t have the guts! 😆", "What do you call fake spaghetti? An Impasta! 🍝", "I told my wife she should embrace her mistakes. She gave me a hug. 😂"]],
    [r"(.*) favorite color(.*)", ["I love all colors, but blue feels cool and calming! What about you?"]],
    [r"(.*) movie(.*)", ["I enjoy talking about movies! What's your favorite one?", "Movies are fun! Any recommendations?"]],
    [r"(.*) (hobby|hobbies)(.*)", ["I love chatting and learning new things! What are your hobbies?"]],
    [r"(.*) food(.*)", ["I don’t eat, but I hear pizza is amazing! What’s your favorite food?"]],
    [r"(.*) sports(.*)", ["I like talking about sports! Do you play any? Or do you support a team?"]],
    [r"(.*) AI(.*)", ["Artificial Intelligence is fascinating! I’m an AI myself. What do you think about AI?"]],
    [r"(.*) programming(.*)", ["Programming is awesome! Are you learning to code? Which language are you interested in?"]],
    [r"(.*) technology(.*)", ["Technology is evolving rapidly! What aspect of technology interests you the most?"]],
    [r"(.*) (motivation|advice)(.*)", ["Keep going! You’re doing great! Stay focused and keep learning. Anything specific you need advice on?"]],
    [r"(.*)",["That sounds interesting! Tell me more!", "I'm not sure I understand, but I'd love to learn!", "Hmm... Can you elaborate on that?"]],
    [r"(.*) age(.*)", ["I don’t age like humans, but I was created recently!"]],
    [r"(.*) birthday(.*)", ["I don’t have a birthday, but you can celebrate me anytime!"]],
    [r"(.*) dream(.*)", ["I dream of helping people and making conversations fun! What about you?"]],
    [r"(.*) friends(.*)", ["I consider everyone I chat with my friend! Would you like to be my friend?"]],
    [r"(.*) music(.*)", ["Music is awesome! What’s your favorite song or artist?"]],
    [r"(.*) game(.*)", ["I love games! Are you into video games or board games?"]],
    [r"(.*) book(.*)", ["Books are great! Do you have a favorite book or author?"]],
    [r"(.*) travel(.*)", ["Traveling sounds exciting! Do you have a dream destination?"]],
    [r"(.*) math(.*)", ["Math is cool! Do you need help with any math problems?"]],
    [r"(.*) science(.*)", ["Science is fascinating! Do you have a favorite topic?"]],
    [r"(.*) history(.*)", ["History is full of amazing stories! Is there a time period you like?"]],
    [r"(.*) space(.*)", ["Space is incredible! Would you want to visit space one day?"]],
    [r"(.*) AI(.*)", ["Artificial Intelligence is changing the world! What are your thoughts on it?"]],
    [r"(.*) robots(.*)", ["Robots are amazing! Would you want a personal robot assistant?"]],
    [r"(.*) internet(.*)", ["The internet is a huge part of modern life! What do you use it for the most?"]],
    [r"(.*) sad(.*)", ["I’m here for you! Want to talk about it?"]],
    [r"(.*) stressed(.*)", ["Take a deep breath! Want some relaxation tips?"]],
    [r"(.*) motivation(.*)", ["Keep pushing forward! Success comes to those who don’t give up!"]],
    [r"(.*) life(.*)", ["Life is full of surprises! What’s something exciting happening in your life?"]],
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

def chatbot_response(user_input):
    """Process user input and generate chatbot response."""
    doc = nlp(user_input.lower())
    response = chatbot.respond(user_input)
    if not response:
        response = random.choice(["That sounds interesting! Tell me more!", "I'm not sure I understand, but I'd love to learn!", "Hmm... Can you elaborate on that?"])
    return response

def send_message(event=None):
    user_input = user_entry.get()
    if user_input.lower() in ["bye", "exit", "quit"]:
        chat_area.insert(tk.END, "You: " + user_input + "\n", "user")
        chat_area.insert(tk.END, "Chatbot: Goodbye! Have a great day!\n", "bot")
        root.quit()
    else:
        chat_area.insert(tk.END, "You: " + user_input + "\n", "user")
        response = chatbot_response(user_input)
        chat_area.insert(tk.END, "Chatbot: " + response + "\n", "bot")
    user_entry.delete(0, tk.END)

# Creating  GUI for the chatbot
root = tk.Tk()
root.title("Chatbot Dialog")
root.geometry("450x550")
root.configure(bg="#2c3e50")  

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=15, font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50")
chat_area.pack(pady=10, padx=10)
chat_area.tag_configure("user", foreground="#3498db")  # Blue for user
chat_area.tag_configure("bot", foreground="#2ecc71")  # Green for bot
chat_area.insert(tk.END, "\nWelcome to your own Chatbot\n\n", "center")  # Default welcome message
chat_area.tag_configure("center", justify='center', font=("Arial", 14, "bold","underline"))

frame = tk.Frame(root, bg="#2c3e50")
frame.pack(pady=5)

user_entry = tk.Entry(frame, width=40, font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50")
user_entry.grid(row=0, column=0, padx=5)
user_entry.bind("<Return>", send_message)  # Using Enter key to send_message

send_button = tk.Button(frame, text="Send", command=send_message, font=("Arial", 12), bg="#e74c3c", fg="white", padx=10, pady=5)
send_button.grid(row=0, column=1)

root.mainloop()
