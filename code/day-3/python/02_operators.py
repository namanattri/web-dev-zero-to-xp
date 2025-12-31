"""
Python Crash Course - Lesson 2: Operators
==========================================
Learn to perform operations on data
"""

# ARITHMETIC OPERATORS
print("=== ARITHMETIC OPERATORS ===")
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")  # Returns float
print(f"Floor Division (a // b): {a // b}")  # Returns integer
print(f"Modulus (a % b): {a % b}")  # Remainder
print(f"Exponentiation (a ** b): {a ** b}")  # Power
print()

# COMPARISON OPERATORS
# Used to compare two values, returns True or False
print("=== COMPARISON OPERATORS ===")
x = 5
y = 10

print(f"x = {x}, y = {y}")
print(f"x == y (Equal to): {x == y}")
print(f"x != y (Not equal to): {x != y}")
print(f"x > y (Greater than): {x > y}")
print(f"x < y (Less than): {x < y}")
print(f"x >= y (Greater than or equal to): {x >= y}")
print(f"x <= y (Less than or equal to): {x <= y}")
print()

# LOGICAL OPERATORS
# Used to combine conditional statements
print("=== LOGICAL OPERATORS ===")
age = 20
has_license = True

print(f"age = {age}, has_license = {has_license}")
print(f"age >= 18 and has_license: {age >= 18 and has_license}")
print(f"age < 18 or has_license: {age < 18 or has_license}")
print(f"not has_license: {not has_license}")
print()

# ASSIGNMENT OPERATORS
print("=== ASSIGNMENT OPERATORS ===")
count = 5
print(f"Initial count: {count}")

count += 3  # Same as: count = count + 3
print(f"After count += 3: {count}")

count -= 2  # Same as: count = count - 2
print(f"After count -= 2: {count}")

count *= 2  # Same as: count = count * 2
print(f"After count *= 2: {count}")

count //= 3  # Same as: count = count // 3
print(f"After count //= 3: {count}")
print()

# PRACTICAL EXAMPLES
print("=== PRACTICAL EXAMPLES ===")

# Calculate area of a rectangle
length = 10
width = 5
area = length * width
print(f"Rectangle area (length={length}, width={width}): {area}")

# Check if a number is even or odd
number = 17
is_even = (number % 2 == 0)
print(f"Is {number} even? {is_even}")

# Calculate average
score1 = 85
score2 = 90
score3 = 78
average = (score1 + score2 + score3) / 3
print(f"Average score: {average:.2f}")

