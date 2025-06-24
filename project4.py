def get_reply(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I don't understand that. Try saying 'hello', 'how are you', or 'bye'."

# Chatbot loop
print("🤖 Chatbot is online. Type something (type 'bye' to exit).")

while True:
    user_message = input("You: ")
    response = get_reply(user_message)
    print("Bot:", response)
    
    if user_message.lower().strip() == "bye":
        break
