responses = {
    "greeting": "Hello! How can I help you?",
    "name": "I am a Student Assistant Chatbot.",
    "help": "I can answer some basic student-related questions.",
    "study": "Try studying in focused sessions with short breaks.",
    "thanks": "You're welcome!",
    "goodbye": "Goodbye! Have a great day!"
}

print("🤖 Student Assistant Chatbot")
print("Hello! I am your Student Assistant Chatbot.")
print("Type 'bye', 'exit', or 'quit' to end the conversation.")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hello", "hi", "hii", "hey"]:
        print(responses["greeting"])

    elif user_input in ["what is your name", "who are you"]:
        print(responses["name"])

    elif user_input in ["can you help me", "help", "i need help"]:
        print(responses["help"])

    elif user_input in ["how can i study effectively", "how should i study", "study tips"]:
        print(responses["study"])

    elif user_input in ["thank you", "thanks", "thankyou"]:
        print(responses["thanks"])

    elif user_input in ["bye", "exit", "quit"]:
        print(responses["goodbye"])
        break

    else:
        print("Sorry, I don't understand that yet.")