# -----------------------------
# FUNCTION: Chatbot Response
# -----------------------------
def chatbot_response(user_input):
    user_input = user_input.lower().strip()  # Clean input

    # Lists for matching
    greetings = ["hello", "hi", "hey", "good morning", "good evening"]
    farewells = ["bye", "goodbye", "see you"]
    wellbeing = ["how are you", "how is it going", "how do you do"]
    thanks = ["thank you", "thanks", "thank u"]
    jokes = ["joke", "make me laugh"]

    # Greeting
    if user_input in greetings:
        return "Hi! How can I help you?"

    # Wellbeing
    elif user_input in wellbeing:
        return "I'm doing great 😊 How about you?"

    # Thanks
    elif user_input in thanks:
        return "You're welcome! 😊"

    # Farewell
    elif user_input in farewells:
        return "Goodbye! Have a nice day 👋"

    # Name
    elif "name" in user_input:
        return "I am a simple chatbot."

    # Time
    elif "time" in user_input:
        from datetime import datetime
        return f"Current time is {datetime.now().strftime('%H:%M:%S')}."

    # Date & Day
    elif "date" in user_input or "day" in user_input:
        from datetime import datetime
        return datetime.now().strftime("Today is %A, %d %B %Y.")

    # Calculator
    elif "add" in user_input:
        return "Addition example: add 5 and 3 → result is 8."
    elif "subtract" in user_input:
        return "Subtraction example: subtract 3 from 10 → result is 7."
    elif "multiply" in user_input:
        return "Multiplication example: 4 × 5 = 20."
    elif "divide" in user_input:
        return "Division example: 10 ÷ 2 = 5."

    # Jokes
    elif user_input in jokes:
        return "Why do programmers love Python? 🐍 Because it's easy to learn 😄"

    # Help
    elif "help" in user_input:
        return (
            "I can help with:\n"
            "- Greetings\n"
            "- Time & Date\n"
            "- Simple math\n"
            "- Jokes\n"
            "- General chat"
        )

    # Default response
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."


# -----------------------------
# MAIN PROGRAM LOOP
# -----------------------------
def start_chatbot():
    print("🤖 Welcome to the Python Chatbot!")
    print("How can I help you today?")
    print("Type 'exit' anytime to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() == "exit":
            print("Chatbot: Goodbye! Have a nice day 👋")
            break

        response = chatbot_response(user_input)
        print("Chatbot:", response)


# -----------------------------
# START THE CHATBOT
# -----------------------------
if __name__ == "__main__":
    start_chatbot()
