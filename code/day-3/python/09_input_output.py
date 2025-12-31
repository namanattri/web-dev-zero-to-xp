"""
Python Crash Course - Lesson 9: Input and Output
=================================================
Learn to interact with users and handle data
"""

import random

# BASIC OUTPUT
print("=== BASIC OUTPUT ===")
print("Hello, World!")
print("Python", "is", "awesome")  # Multiple arguments
print("Age:", 25)  # Mixed types
print()

# FORMATTED OUTPUT
print("=== FORMATTED OUTPUT ===")
name = "Alice"
age = 25
city = "New York"

# Method 1: f-strings (recommended)
print(f"Name: {name}, Age: {age}, City: {city}")

# Method 2: format()
print("Name: {}, Age: {}, City: {}".format(name, age, city))

# Method 3: % operator (old style)
print("Name: %s, Age: %d, City: %s" % (name, age, city))
print()

# OUTPUT FORMATTING
print("=== OUTPUT FORMATTING ===")
price = 19.99
quantity = 5
total = price * quantity

print(f"Price: ${price:.2f}")  # 2 decimal places
print(f"Quantity: {quantity}")
print(f"Total: ${total:.2f}")
print()

# PRINT WITH CUSTOM SEPARATOR AND END
print("=== CUSTOM SEPARATOR AND END ===")
print("apple", "banana", "orange", sep=", ")  # Custom separator
print("Loading", end="...")  # Custom end (no newline)
print(" Done!")
print()

# BASIC INPUT
print("=== BASIC INPUT ===")
name = input("Enter your name: ")
print(f"Hello, {name}!")
print()

# INPUT WITH TYPE CONVERSION
print("=== INPUT WITH TYPE CONVERSION ===")
age = int(input("Enter your age: "))  # Convert string to integer
print(f"You will be {age + 1} next year")
print()

# MULTIPLE INPUTS
print("=== MULTIPLE INPUTS ===")
numbers_str = input("Enter three numbers separated by spaces: ")
numbers = [int(x) for x in numbers_str.split()]
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers)}")
print()

# PRACTICAL EXAMPLES
print("=== PRACTICAL EXAMPLES ===")

# Example 1: Simple calculator
print("\n--- Simple Calculator ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2 if num2 != 0 else "Error: Division by zero"
else:
    result = "Invalid operation"

print(f"Result: {num1} {operation} {num2} = {result}")
print()

# Example 2: Temperature converter
print("\n--- Temperature Converter ---")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
print()

# Example 3: Shopping list
print("\n--- Shopping List ---")
shopping_list = []
print("Enter items (type 'done' to finish):")
while True:
    item = input("Item: ")
    if item.lower() == "done":
        break
    shopping_list.append(item)

print("\nYour shopping list:")
for i, item in enumerate(shopping_list, 1):
    print(f"{i}. {item}")
print()

# Example 4: Grade calculator
print("\n--- Grade Calculator ---")
scores_str = input("Enter scores separated by spaces: ")
scores = [int(x) for x in scores_str.split()]

average = sum(scores) / len(scores)
print(f"\nScores: {scores}")
print(f"Average: {average:.2f}")

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")
print()

# Example 5: Number guessing game
print("\n--- Number Guessing Game ---")
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 5

print("Guess the number between 1 and 100!")

while attempts < max_attempts:
    guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"Congratulations! You found it in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    
    if attempts >= max_attempts:
        print(f"Game over! The number was {secret_number}")
        break

