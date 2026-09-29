print("Chatbot: Hello! Type 'bye' to exit the chat.")

while True:
    user_input = input("You: ").lower().strip()

    if "hello" in user_input or "hi" in user_input:
        response = "Hi!"
    elif "how are you" in user_input:
        response = "I'm fine, thanks!"
    elif "bye" in user_input or "goodbye" in user_input:
        response = "Goodbye!"
    else:
        response = "I'm sorry, I don't understand that."

    print(f"Chatbot: {response}")

    if "bye" in user_input
