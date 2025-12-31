"""
Python Crash Course - Lesson 1: Variables and Data Types
=========================================================
Learn the fundamental building blocks of Python programming
"""

# VARIABLES
# Variables are containers for storing data values
# Python is dynamically typed - you don't need to declare the type

name = "Alice"  # String (text)
age = 25  # Integer (whole number)
height = 5.6  # Float (decimal number)
is_student = True  # Boolean (True or False)

print("=== VARIABLES ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")
print()

# BASIC DATA TYPES
# 1. Strings - Text data
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # String concatenation
print("=== STRINGS ===")
print(f"Full Name: {full_name}")
print(f"Length of name: {len(full_name)}")
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")
print()

# 2. Numbers - Integers and Floats
x = 10  # Integer
y = 3.14  # Float
print("=== NUMBERS ===")
print(f"Integer: {x}")
print(f"Float: {y}")
print(f"Type of x: {type(x)}")
print(f"Type of y: {type(y)}")
print()

# 3. Booleans - True or False
is_raining = False
is_sunny = True
print("=== BOOLEANS ===")
print(f"Is it raining? {is_raining}")
print(f"Is it sunny? {is_sunny}")
print()

# TYPE CONVERSION
# Converting between different data types
print("=== TYPE CONVERSION ===")
num_string = "100"
num_int = int(num_string)  # Convert string to integer
print(f"String '100' to integer: {num_int}")

price = 19.99
price_string = str(price)  # Convert float to string
print(f"Float 19.99 to string: '{price_string}'")

value = 42
value_float = float(value)  # Convert integer to float
print(f"Integer 42 to float: {value_float}")
print()

# MULTIPLE ASSIGNMENT
# Assign values to multiple variables in one line
a, b, c = 1, 2, 3
print("=== MULTIPLE ASSIGNMENT ===")
print(f"a = {a}, b = {b}, c = {c}")

# Assign the same value to multiple variables
x = y = z = 0
print(f"x = {x}, y = {y}, z = {z}")

