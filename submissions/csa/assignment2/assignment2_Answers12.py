# # Assignment 2: Operators

# ## Question 12: Divisibility Test
# Check if a number is divisible by both 3 and 5 using logical operators.

# **Sample Input:**
# ```
# number = 15
# ```

# **Sample Output:**
# ```
# 15 is divisible by 3: True
# 15 is divisible by 5: True
# 15 is divisible by both 3 and 5: True

print("Answer 10: Range Checker")

number = 15
is_true = True

if number%3 == 0:
    print(f"15 is divisible by 3: {is_true}")
if number%5 == 0:
    print(f"15 is divisible by 5: {is_true}")
if number%5 == 0 and number%3 == 0:
    print(f"15 is divisible by both 3 and 5: {is_true}")    