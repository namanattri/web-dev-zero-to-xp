"""
Python Crash Course - Lesson 9: Input and Output
=================================================
Learn to interact with users and handle data
"""

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

# BASIC INPUT (COMMENTED OUT - FOR DEMONSTRATION)
print("=== BASIC INPUT (DEMONSTRATION) ===")
# When you run this interactively, uncomment these lines:
# name = input("Enter your name: ")
# print(f"Hello, {name}!")

# For demonstration, we'll simulate input
print("# Simulated: name = input('Enter your name: ')")
print("# User enters: Alice")
name = "Alice"  # Simulated input
print(f"Hello, {name}!")
print()

# INPUT WITH TYPE CONVERSION
print("=== INPUT WITH TYPE CONVERSION ===")
# Simulated demonstration
print("# age = input('Enter your age: ')")
print("# User enters: 25")
age_str = "25"  # Simulated input
age = int(age_str)  # Convert string to integer
print(f"You will be {age + 1} next year")
print()

# MULTIPLE INPUTS
print("=== MULTIPLE INPUTS ===")
# Simulated demonstration
print("# Enter three numbers separated by spaces:")
print("# User enters: 10 20 30")
numbers_str = "10 20 30"  # Simulated input
numbers = [int(x) for x in numbers_str.split()]
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers)}")
print()

# PRACTICAL EXAMPLES
print("=== PRACTICAL EXAMPLES ===")

# Example 1: Simple calculator (simulated)
print("\n--- Simple Calculator ---")
print("# num1 = input('Enter first number: ')")
print("# User enters: 10")
num1 = 10

print("# num2 = input('Enter second number: ')")
print("# User enters: 5")
num2 = 5

print("# operation = input('Enter operation (+, -, *, /): ')")
print("# User enters: +")
operation = "+"

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

# Example 2: Temperature converter (simulated)
print("\n--- Temperature Converter ---")
print("# celsius = input('Enter temperature in Celsius: ')")
print("# User enters: 25")
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
print()

# Example 3: Shopping list (simulated)
print("\n--- Shopping List ---")
shopping_list = []
print("# Enter items (type 'done' to finish):")
# Simulated items
items = ["milk", "bread", "eggs", "done"]
for item in items:
    print(f"# User enters: {item}")
    if item.lower() == "done":
        break
    shopping_list.append(item)

print("\nYour shopping list:")
for i, item in enumerate(shopping_list, 1):
    print(f"{i}. {item}")
print()

# Example 4: Grade calculator (simulated)
print("\n--- Grade Calculator ---")
print("# Enter scores separated by spaces:")
print("# User enters: 85 90 78 92 88")
scores_str = "85 90 78 92 88"
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

# Example 5: Number guessing game (simulated)
print("\n--- Number Guessing Game ---")
secret_number = 42
attempts = 0
max_attempts = 5

print(f"Guess the number between 1 and 100!")
# Simulated guesses
guesses = [50, 40, 45, 42]

for guess in guesses:
    attempts += 1
    print(f"# Attempt {attempts}: User enters: {guess}")
    
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

print("\n" + "="*50)
print("NOTE: To run these examples interactively,")
print("uncomment the input() statements and run the script!")
print("="*50)

