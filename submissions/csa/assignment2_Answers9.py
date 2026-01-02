# # Assignment 2: Operators

# ## Question 9: Compound Assignment
# Start with a number and use all compound assignment operators (+=, -=, *=, /=, //=, %=, **=) one by one. Print after each operation.

# **Sample Input:**
# ```
# num = 100
# ```

# **Sample Output:**
# ```
# Initial: 100
# After += 50: 150
# After -= 30: 120
# After *= 2: 240
# After /= 4: 60.0
# After //= 7: 8.0
# After %= 3: 2.0
# After **= 3: 8.0

print("Answer 9: Compound Assignment")

num = 100

print(f"Initial: {num}")

num += 50

print(f"After += 50: {num}")

num -= 30

print(f"After -= 30: {num}")

num *= 2

print(f"After *= 2: {num}")

num /= 4

print(f"After /= 4: {num}")

num //= 7

print(f"After //= 7: {num}")

num %= 3

print(f"After %= 3: {num}")

num **= 3

print(f"After **= 3: {num}")

