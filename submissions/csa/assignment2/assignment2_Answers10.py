# # Assignment 2: Operators

# ## Question 10: Range Checker
# Check if a number is within a specific range (inclusive) using logical operators.

# **Sample Input:**
# ```
# number = 45
# min_val = 1
# max_val = 100
# ```

# **Sample Output:**
# ```
# 45 is within range [1, 100]: True

print("Answer 10: Range Checker")

number = 45
min_val = 1
max_val = 100
is_true = True

if number >= min_val and number <= max_val:
    print(f"{number} is within range [{min_val}, {max_val}]: {is_true}")