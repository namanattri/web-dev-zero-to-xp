"""
Python Crash Course - Lesson 4: Loops (for and while)
======================================================
Learn to repeat actions efficiently
"""

# FOR LOOP - Iterate over a sequence
print("=== BASIC FOR LOOP ===")
# Loop through a range of numbers
for i in range(5):  # 0 to 4
    print(f"Count: {i}")
print()

# FOR LOOP WITH RANGE
print("=== FOR LOOP WITH RANGE ===")
# range(start, stop, step)
for i in range(1, 11):  # 1 to 10
    print(f"Number: {i}")
print()

# FOR LOOP WITH STEP
print("=== FOR LOOP WITH STEP ===")
# Print even numbers from 0 to 10
for i in range(0, 11, 2):
    print(f"Even number: {i}")
print()

# WHILE LOOP
# Repeats while a condition is true
print("=== WHILE LOOP ===")
count = 1 # initialize the counter
while count <= 5: # condition to repeat the loop
    print(f"Count: {count}")
    count += 1  # Important: update the counter! # increment the counter
print()

# BREAK STATEMENT
# Exit the loop prematurely
print("=== BREAK STATEMENT ===")
for i in range(1, 11):
    if i == 5:
        print("Breaking at 5")
        break
    print(f"Number: {i}")
print()

# CONTINUE STATEMENT
# Skip the rest of the current iteration
print("=== CONTINUE STATEMENT ===")
for i in range(1, 6):
    if i == 3:
        print("Skipping 3")
        continue
    print(f"Number: {i}")
print()

# NESTED LOOPS
print("=== NESTED LOOPS ===")
# Print a multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()  # Empty line after each row

# PRACTICAL EXAMPLES
print("=== PRACTICAL EXAMPLES ===")

# Example 1: Sum of numbers from 1 to 10
total = 0
for i in range(1, 11):
    total += i
print(f"Sum of 1 to 10: {total}")
print()

# Example 2: Countdown timer
print("Countdown:")
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off!")
print()

# Example 3: Find first number divisible by 7 and 5
for num in range(1, 101):
    if num % 7 == 0 and num % 5 == 0:
        print(f"First number divisible by both 7 and 5: {num}")
        break
print()

# Example 4: Print only odd numbers
print("Odd numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:  # If even, skip
        continue
    print(i, end=" ")
print("\n")

# Example 5: Factorial calculation
number = 5
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"Factorial of {number}: {factorial}")
print()

number = 5
factorial = 1
while number > 0:
    factorial *= number
    number -= 1
print(f"Factorial of {number}: {factorial}")
print()

# Example 6: Pattern printing
print("Pattern:")
for i in range(1, 6):
    print("*" * i)
print()

# Example 7: While loop with sentinel value
print("Enter 'quit' to exit")
# Simulating user input with a list for demonstration
messages = ["Hello", "World", "quit"]
index = 0
while index < len(messages):
    message = messages[index]
    if message == "quit":
        print("Exiting...")
        break
    print(f"Message: {message}")
    index += 1

