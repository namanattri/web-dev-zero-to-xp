# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 33: Butterfly Pattern
# Print a butterfly pattern using stars.

# **Sample Input:**
# ```
# rows = 5
# ```

# **Sample Output:**
# ```
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# ```

# ---

print("Answer 33: Butterfly Pattern")

n = 5

for i in range(n-1):
    for j in range(i+1):
        print("*", end=" ")
    for j in range(i,n-1):
        print(" ", end=" ")
    for j in range(i,n-1):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i,n):
        print("*", end=" ")
    for j in range(i):
        print(" ", end=" ")        
    for j in range(i):
        print(" ", end=" ")
    for j in range(i,n):
        print("*", end=" ")         
    print()



