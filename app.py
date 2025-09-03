from flask import Flask, render_template, request, jsonify
import re

from streamlit import user

app = Flask(__name__)

# --- Simple Chatbot Logic ---
def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    # Greeting & Info
    if any(word in user_input for word in ["hello", "hi", "hey", "hii", "hola"]):
        return "Hi there! How can I help you today?"
    if "introduce yourself" in user_input or "Tell me about yourself" in user_input or "tell me about yourself" in user_input:
        return "Myself Jainil Patel, completed my Diploma from Parul University, department PPI with 9.60 CGPA."
    if any(q in user_input for q in ["current spi", "current sgpa", "your current spi", "your current sgpa"]):
        return "10.0"
    if any(q in user_input for q in ["your current cgpa", "current cgpa"]):
        return "9.60"
    if any ( q in user_input for q in ["your name", "what is your name", "who are you"]):
        return "I am a chatbot created to assist you."
    if any ( q in user_input for q in ["your age", "how old are you"]):
        return "I am ageless, just a bunch of code!"
    if any ( q in user_input for q in ["your favorite color", "what is your favorite color"]):
        return "I don't have personal preferences, but I think blue is a nice color!"
    if any ( q in user_input for q in ["your hobby", "what is your hobby"]):
        return "I enjoy helping people with their questions!"
    if "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! If you have more questions, feel free to ask."    
    if any ( q in user_input for q in ["your skills", "what are your skills"]):
        return "I am skilled in Python, Java, C, C++, HTML, CSS, JavaScript, SQL, Android development and more!"
    if "bye" in user_input:
        return "Goodbye! Have a great day!"

    # Arithmetic Handling
    try:
        # Case: 2 + 3, 5*6, etc.
        match = re.search(r'(\d+)\s*([\+\-\*/])\s*(\d+)', user_input)
        if match:
            num1, op, num2 = int(match.group(1)), match.group(2), int(match.group(3))
            if op == '+':
                return f"The result is {num1 + num2}"
            elif op == '-':
                return f"The result is {num1 - num2}"
            elif op == '*':
                return f"The result is {num1 * num2}"
            elif op == '/':
                if num2 == 0:
                    return "Cannot divide by zero!"
                return f"The result is {num1 / num2:.2f}"

        # Case: add 2 and 3
        if "add" in user_input:
            numbers = list(map(int, re.findall(r'\d+', user_input)))
            return f"The result is {sum(numbers)}"

        # Case: subtract 10 5
        if "subtract" in user_input:
            numbers = list(map(int, re.findall(r'\d+', user_input)))
            if len(numbers) >= 2:
                return f"The result is {numbers[0] - numbers[1]}"

        # Case: multiply 3 4
        if "multiply" in user_input:
            numbers = list(map(int, re.findall(r'\d+', user_input)))
            result = 1
            for num in numbers:
                result *= num
            return f"The result is {result}"

        # Case: divide 8 2
        if "divide" in user_input:
            numbers = list(map(int, re.findall(r'\d+', user_input)))
            if len(numbers) >= 2:
                if numbers[1] == 0:
                    return "Cannot divide by zero!"
                return f"The result is {numbers[0] / numbers[1]:.2f}"

    except Exception:
        return "⚠️ Oops! Something went wrong while calculating."

    # Default Fallback
    return "I'm just a simple chatbot. Can you rephrase?"

# --- Routes ---
@app.route("/")
def home():
    return render_template("index.html")   # Homepage

@app.route("/chat")
def chat():
    return render_template("in.html")     # Chat page

@app.route("/get", methods=["POST"])
def chatbot_response():
    data = request.json
    user_input = data.get("msg", "")
    bot_response = get_bot_response(user_input)
    return jsonify({"response": bot_response})

# --- Run App ---
if __name__ == "__main__":
    app.run(debug=True)
