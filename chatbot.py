import random
import time

responses = {

    "hello": [
        "Hello! 👋 I'm Nova, your AI assistant.",
        "Hi there! 😊",
        "Hey! Nice to meet you."
    ],

    "hi": [
        "Hi! 😊 How can I help you today?",
        "Hello there!",
        "Hey! What's up?"
    ],

    "hey": [
        "Hey hey! 👋",
        "Hello! How are you?"
    ],

    "good morning": [
        "Good morning! ☀️",
        "Morning! Hope you have a productive day."
    ],

    "good evening": [
        "Good evening! 🌙",
        "Hope your evening is going well."
    ],

    "how are you": [
        "I'm doing great! 😄",
        "All systems are running perfectly!",
        "Feeling awesome today!"
    ],

    "who are you": [
        "I am Nova, a Rule-Based AI Chatbot.",
        "I'm an AI chatbot created using Python."
    ],

    "what is your name": [
        "My name is Nova 🤖",
        "You can call me Nova!"
    ],

    "who made you": [
        "I was created by Mounika during the DecodeLabs Internship 🚀"
    ],

    "what is ai": [
        "AI stands for Artificial Intelligence. It enables machines to simulate human intelligence."
    ],

    "what is machine learning": [
        "Machine Learning is a branch of AI where systems learn from data."
    ],

    "what is python": [
        "Python is a popular programming language widely used in AI and data science. 🐍"
    ],

    "what is chatbot": [
        "A chatbot is a software program that simulates human conversation."
    ],

    "what is loop": [
        "A loop repeats a block of code multiple times."
    ],

    "what is dictionary": [
        "A dictionary stores data in key-value pairs."
    ],

    "what is function": [
        "A function is a reusable block of code."
    ],

    "what is decodelabs": [
        "DecodeLabs provides hands-on AI and development internships."
    ],

    "about this project": [
        "This project is a Rule-Based AI Chatbot using Python dictionary lookup."
    ],

    "ipo model": [
        "IPO means Input → Process → Output."
    ],

    "motivate me": [
        "Every expert was once a beginner. Keep learning and keep building! 💪",
        "Your AI journey starts with one small project at a time 🚀"
    ],

    "i am tired": [
        "Take a short break ☕ and come back stronger!"
    ],

    "i am stressed": [
        "Relax 🌿 Take things step by step. You are learning something valuable."
    ],

    "joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
        "Why did the AI go to therapy? Too many deep learning issues! 🤖"
    ],

    "tell me a fact": [
        "Python was named after Monty Python, not the snake! 🐍",
        "The term Artificial Intelligence was coined in 1956."
    ],

    "flip a coin": [
        "Heads 🪙",
        "Tails 🪙"
    ],

    "thanks": [
        "You're welcome! 😊",
        "Happy to help!"
    ],

    "thank you": [
        "You're very welcome! 💙"
    ],

    "help": [
        """
📋 Things you can ask me:

• hello / hi / hey
• how are you
• who are you
• what is ai
• what is python
• what is machine learning
• what is chatbot
• what is loop
• what is dictionary
• motivate me
• joke
• tell me a fact
• flip a coin
• thanks

Type 'exit' to close the chatbot.
        """
    ]
}

def get_response(user_input):

    result = responses.get(user_input)

    if result:
        return random.choice(result)

    return None


def nova_print(message):

    print("\nNova 🤖 :", end=" ")

    time.sleep(0.5)

    print(message)


print("\n" + "=" * 55)
print("        NOVA — Rule-Based AI Chatbot 🤖")
print("        DecodeLabs AI Internship | 2026")
print("=" * 55)

print("\nType 'help' to view commands.")
print("Type 'exit' to quit the chatbot.\n")


while True:

    raw_input_data = input("You 💬 : ")

    clean_input = raw_input_data.lower().strip()

    if clean_input == "":

        nova_print("Please type something!")

        continue

    if clean_input in ["exit", "quit", "stop", "close", "bye", "goodbye"]:

        nova_print("Goodbye! 👋 Keep learning and keep coding!")

        print("\n" + "=" * 55)

        break

    reply = get_response(clean_input)

    if reply:

        nova_print(reply)

    else:

        fallback_responses = [

            "I don't understand that yet. Try typing 'help'. 🤔",

            "Sorry, I am still learning that topic.",

            "That input is not in my knowledge base yet."
        ]

        nova_print(random.choice(fallback_responses)) 