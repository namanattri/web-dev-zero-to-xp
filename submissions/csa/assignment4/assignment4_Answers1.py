# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ---

# ## Question 1: Multiplication Table
# Print the multiplication table for a given number from 1 to 10.

# **Sample Input:**
# ```
# number = 7
# ```

# **Sample Output:**
# ```
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# ...
# 7 x 10 = 70
# ```

print("Answer 1: AMultiplication Table")

"""For Loop"""
# number = 7
number = int(input("Which Table you want: -"))

for i in range(1,11):
    print(f"{number} * {i}  = {number*i}")

number = int(input("Which Table you want to: -"))

"""while Loop"""
i = 1

while i <= 10:
    print(f"{number} * {i}  = {number*i}")

    i += 1