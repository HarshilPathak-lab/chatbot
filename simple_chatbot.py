
print("Hello! I'm ChatBot. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ").lower()

    if user_input in ['hi', 'hello', 'hey']:
        print("Bot: Hello there! How can I help you today?")
    elif 'your name' in user_input:
        print("Bot: I’m a simple Python chatbot created for an internship task!")
    elif 'how are you' in user_input:
        print("Bot: I’m doing great! Thanks for asking. How about you?")
    elif 'help' in user_input:
        print("Bot: I can chat with you or answer simple questions about myself.")
    elif 'bye' in user_input or user_input == 'exit':
        print("Bot: Goodbye! Have a great day. 👋")
        break
    else:
        print("Bot: Sorry, I didn’t understand that. Try asking something else.")

