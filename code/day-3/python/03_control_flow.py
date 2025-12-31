"""
Python Crash Course - Lesson 3: Control Flow (if/elif/else)
============================================================
Learn to make decisions in your code
"""

# BASIC IF STATEMENT
print("=== BASIC IF STATEMENT ===")
age = 18

if age >= 18:
    print("You are an adult")
print()

# IF-ELSE STATEMENT
print("=== IF-ELSE STATEMENT ===")
temperature = 25

if temperature > 30:
    print("It's hot outside!")
else:
    print("The weather is pleasant")
print()

# IF-ELIF-ELSE STATEMENT
# Use when you have multiple conditions to check
print("=== IF-ELIF-ELSE STATEMENT ===")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")
print()

# NESTED IF STATEMENTS
print("=== NESTED IF STATEMENTS ===")
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("You can enter the concert")
    else:
        print("You need a ticket to enter")
else:
    print("You must be 18 or older")
print()

# MULTIPLE CONDITIONS WITH LOGICAL OPERATORS
print("=== MULTIPLE CONDITIONS ===")
username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("Login successful!")
else:
    print("Invalid credentials")
print()

# PRACTICAL EXAMPLES
print("=== PRACTICAL EXAMPLES ===")

# Example 1: Check if a number is positive, negative, or zero
number = -5
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")
print()

# Example 2: Check if a year is a leap year
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
print()

# Example 3: Determine ticket price based on age
age = 12
if age < 3:
    price = 0
elif age <= 12:
    price = 10
elif age <= 65:
    price = 20
else:
    price = 15

print(f"Age: {age}, Ticket price: ${price}")
print()

# TERNARY OPERATOR (One-line if-else)
print("=== TERNARY OPERATOR ===")
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

