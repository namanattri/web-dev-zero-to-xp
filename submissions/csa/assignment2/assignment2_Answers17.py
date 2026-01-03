# # Assignment 2: Operators

# ## Question 17: Number Sign Checker
# Determine if a number is positive, negative, or zero using comparison operators.

# **Sample Input:**
# ```
# num = -15
# ```

# **Sample Output:**
# ```
# -15 is negative

print("Answer 17: Number Sign Checker")

num = -15

if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")