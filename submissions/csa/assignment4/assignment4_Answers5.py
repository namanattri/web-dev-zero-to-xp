# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 5: Factorial Calculator
# Calculate the factorial of a number using a loop.

# **Sample Input:**
# ```
# n = 5
# ```

# **Sample Output:**
# ```
# Factorial of 5 = 120
# ```

print("Answer 5: Factorial Calculator")

n = 5

fact = 1

for i in range(1,n+1):
    fact *= i
print(f"Factorial of {n} = {fact}")