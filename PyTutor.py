# Introduction to Python Data Types
# This script will guide you through the most common data types in Python.
# Let's get started!

print("=" * 40)
print("🎓 Welcome to the Python Data Types Tutorial!")
print("=" * 40)
print("In this tutorial, we'll walk through the most common Python data types. Buckle up!")
input("\nHit Enter whenever you're ready to roll...\n")

# Integer
print("👉 Starting with: Integers (int)")
print("Integers are just whole numbers. Nothing fancy — like 7, -42, or 2024.")
num_apples = 7
print(f"We've got an integer here: num_apples = {num_apples}")
print("Python gives us the type like this:", type(num_apples))
input("Cool? Press Enter to see the next one...\n")

# Float
print("👉 Moving on to: Floats (float)")
print("Floats are numbers with decimal parts, like 3.14 or -0.01. Think of measurements.")
pi_approx = 3.14
print(f"Here's a float value: pi_approx = {pi_approx}")
print("What type is it? Let's ask Python:", type(pi_approx))
input("Onward! Press Enter...\n")

# String
print("👉 Now comes: Strings (str)")
print("Strings are text – single letters, full sentences, emojis, you name it.")
greeting_msg = "Hey there!"
print(f"For example: greeting_msg = '{greeting_msg}'")
print("And yes, type is:", type(greeting_msg))
input("Press Enter to keep going...\n")

# Boolean
print("👉 Booleans (bool) are next")
print("Booleans are either True or False. Binary stuff – kinda like light switches.")
is_raining = False
print(f"So like: is_raining = {is_raining}")
print("Type-wise:", type(is_raining))
input("Boolean logic is everywhere. Hit Enter...\n")

# List
print("👉 Let's explore: Lists (list)")
print("Lists can store several items, and you can change them later.")
shopping_list = ["eggs", "milk", "bread"]
print(f"Example: shopping_list = {shopping_list}")
print("Yup, type is:", type(shopping_list))
input("Lists are pretty useful. Next up...\n")

# Tuple
print("👉 Tuples (tuple), coming in hot!")
print("Tuples are like lists, but you *can't* change them once they're made.")
colors = ("red", "green", "blue")
print(f"Tuple sample: colors = {colors}")
print("Python identifies it as:", type(colors))
input("Immutable means no edits. Press Enter...\n")

# Set
print("👉 Time for Sets (set)")
print("Sets are like bags — no order, no duplicates.")
unique_nums = {1, 2, 2, 3, 4}
print(f"See the duplicates disappear: unique_nums = {unique_nums}")
print("And yeah, it's a:", type(unique_nums))
input("Okay, sets are cool. Moving on...\n")

# Dictionary
print("👉 Say hello to: Dictionaries (dict)")
print("Dictionaries hold key-value pairs. Think of them like a mini database.")
user_profile = {"username": "coder123", "level": 5}
print(f"Here's one: user_profile = {user_profile}")
print("Its type? No surprises here:", type(user_profile))
input("Dictionaries are super handy. Almost done...\n")

# NoneType
print("👉 Finally: NoneType (None)")
print("None represents the absence of a value. Not zero, not empty — just... nothing.")
not_set_yet = None
print(f"Look here: not_set_yet = {not_set_yet}")
print("Type check gives:", type(not_set_yet))
input("Alright, that wraps it up! Press Enter for a summary...\n")

# Summary
print("\n🎉 You made it! Here's a quick recap of the Python data types we covered:")
print("""
🔢 int       - Whole numbers (e.g., 5, -3)
🔣 float     - Decimal numbers (e.g., 2.71)
📝 str       - Text data (e.g., "Python")
✅ bool      - True or False
📦 list      - Mutable list of items
📦 tuple     - Immutable sequence
🧺 set       - Unique unordered values
🗂️ dict      - Key-value mappings
🚫 NoneType  - Means 'nothing here'
""")
print("✅ Remember: use `type(variable)` to check what kind of data you're dealing with.")
input("\nPress Enter to take a quick quiz and see what you remember!\n")

# Mini Quiz
score = 0
print("🧠 Python Data Types Quiz - Let's Go!\n")

q1 = input("Q1: Which data type would you use to store a person's age? ")
if q1.strip().lower() == "int":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Oops! It's `int` for whole numbers like age.")

q2 = input("\nQ2: What type would 'Hello, world!' be? ")
if q2.strip().lower() == "str":
    print("✅ Yep, that's a string.")
    score += 1
else:
    print("❌ Nope. That's a `str` (short for string).")

q3 = input("\nQ3: Which type is used for True/False values? ")
if q3.strip().lower() == "bool":
    print("✅ Nice one!")
    score += 1
else:
    print("❌ That would be a `bool`.")

q4 = input("\nQ4: What's the type of this: [1, 2, 3, 4]? ")
if q4.strip().lower() == "list":
    print("✅ You got it.")
    score += 1
else:
    print("❌ It's a list — square brackets are the giveaway!")

q5 = input("\nQ5: Which type does not allow duplicate items? ")
if q5.strip().lower() == "set":
    print("✅ Right on!")
    score += 1
else:
    print("❌ That’s a `set`. It only keeps unique values.")

# Final score
print("\n📊 Quiz Complete!")
print(f"You scored {score} out of 5.")
if score == 5:
    print("🌟 Perfect score! You're a Python pro!")
elif score >= 3:
    print("👍 Nice job! You're getting the hang of it.")
else:
    print("📚 No worries — just revisit the sections and try again!")

print("\nThanks again for learning Python with me. See you next time! 🐍")
