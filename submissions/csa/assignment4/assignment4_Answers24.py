# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 24: Hollow Square Pattern
# Print a hollow square pattern using stars.

# **Sample Input:**
# ```
# size = 5
# ```

# **Sample Output:**
# ```
# *****
# *   *
# *   *
# *   *
# *****
# ```

# ---

print("Answer 24: Hollow Square Pattern")

n = 5

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()