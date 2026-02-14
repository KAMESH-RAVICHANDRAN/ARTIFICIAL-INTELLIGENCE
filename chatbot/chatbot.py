def chatbot():
    print("Chatbot: Hello! I am a simple chatbot 🤖")
    print("Chatbot: Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" or user_input == "hi":
            print("Chatbot: Hi there! How can I help you?")
        
        elif user_input == "how are you":
            print("Chatbot: I'm doing great! Thanks for asking 😊")
        
        elif user_input == "what is your name":
            print("Chatbot: My name is SimpleBot.")
        
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day 👋")
            break
        
        else:
            print("Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
