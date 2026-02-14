#  Simple Python Chatbot

##  Author

**Name:** Kamesh

---

#  Project Title

**Simple Rule-Based Chatbot using Python**

---

#  Project Description

This project is a simple chatbot developed using Python programming language.
The chatbot interacts with the user through the command line (terminal).

It responds to specific user inputs such as:

* "hi"
* "hello"
* "how are you"
* "what is your name"
* "bye"

If the user enters any other input, the chatbot displays a default response.

This chatbot is rule-based, meaning it works using predefined conditions (if-elif-else statements).

---

#  Objective of the Project

* To understand Python functions
* To learn about loops (while loop)
* To practice conditional statements
* To understand user input handling
* To build a simple interactive chatbot

---

#  Source Code

```python
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
```

---

#  Explanation of the Code (Step-by-Step)

## 1️⃣ Function Definition

```python
def chatbot():
```

* `def` is used to define a function.
* `chatbot()` is the function name.
* All chatbot logic is written inside this function.

---

## 2️⃣ Welcome Messages

```python
print("Chatbot: Hello! I am a simple chatbot 🤖")
print("Chatbot: Type 'bye' to exit.\n")
```

* `print()` displays output.
* `\n` creates a new line.

---

## 3️⃣ Infinite Loop

```python
while True:
```

* Creates an infinite loop.
* The chatbot runs continuously until the user types "bye".

---

## 4️⃣ Taking User Input

```python
user_input = input("You: ").lower()
```

* `input()` takes user input.
* `.lower()` converts input into lowercase.
* This helps avoid case sensitivity issues.

Example:
HI → hi
Hello → hello

---

## 5️⃣ Conditional Statements

### Greeting Condition

```python
if user_input == "hello" or user_input == "hi":
```

* Checks multiple conditions using `or`.

---

### Checking “How are you”

```python
elif user_input == "how are you":
```

* Executes only if previous condition is false.

---

### Exit Condition

```python
elif user_input == "bye":
    break
```

* `break` stops the loop.
* Program ends.

---

## 6️⃣ Default Condition

```python
else:
```

* If input does not match any condition.
* Displays default message.

---

## 🔄 Program Flow

1. Chatbot starts
2. Displays welcome message
3. Waits for user input
4. Checks conditions
5. Responds accordingly
6. Stops when user types "bye"

---

#  Sample Output

```
Chatbot: Hello! I am a simple chatbot 🤖
Chatbot: Type 'bye' to exit.

You: hi
Chatbot: Hi there! How can I help you?

You: what is your name
Chatbot: My name is SimpleBot.

You: bye
Chatbot: Goodbye! Have a nice day 👋
```

---

#  Type of Chatbot

✅ Rule-Based Chatbot
❌ Not AI-based
❌ Not Machine Learning

---

# 🚀 How to Run the Program

1. Install Python
2. Save file as `chatbot.py`
3. Open terminal
4. Run:

```
python chatbot.py
```

---

#  Short Presentation Script (You Can Say This in Class)

> "Good morning everyone.
> My project is a simple rule-based chatbot developed using Python.
> It uses a function, while loop, conditional statements, and user input handling.
> The chatbot responds based on predefined rules using if-elif-else conditions.
> The program runs continuously until the user types 'bye', where the break statement stops execution."

---

#  VIVA QUESTIONS AND ANSWERS

## 1️⃣ What is a chatbot?

A chatbot is a program that simulates conversation with users.

---

## 2️⃣ What type of chatbot is this?

This is a rule-based chatbot because it works using predefined conditions.

---

## 3️⃣ What is the use of while True?

It creates an infinite loop that keeps the chatbot running continuously.

---

## 4️⃣ Why did you use .lower()?

To convert user input into lowercase and avoid case sensitivity problems.

---

## 5️⃣ What is the use of break statement?

The break statement is used to stop the loop and exit the program.

---

## 6️⃣ What are conditional statements?

Conditional statements like if, elif, and else are used to make decisions in a program.

---

## 7️⃣ What is a function?

A function is a block of reusable code that performs a specific task.

---

## 8️⃣ How can you improve this chatbot?

* Add more responses
* Add time/date feature
* Connect to a database
* Add GUI using Tkinter
* Add AI using NLP

---

#  Concepts Used

* Python Functions
* While Loop
* Conditional Statements
* String Methods
* User Input

---

#  Conclusion

This project demonstrates basic Python programming concepts such as loops, conditions, and functions. It is a beginner-friendly chatbot that helps understand how conversation systems work.


