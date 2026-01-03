# Assignment 3: Control Flow (if/elif/else)

# Complete the following coding challenges to practice decision-making with control flow statements.

# ## Question 7: Number Comparison
# Compare two numbers and print which is larger, or if they're equal.

# **Sample Input:**
# ```
# num1 = 45
# num2 = 38
# ```

# **Sample Output:**
# ```
# 45 is greater than 38
# ```

print("Answer 7: Number Comparison")

num1 = 45
num2 = 38

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}") 
else:
    print("Both are equal")  