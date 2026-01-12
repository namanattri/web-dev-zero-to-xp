# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 23: Inverted Pyramid Pattern
# Print an inverted centered pyramid pattern using stars.

# **Sample Input:**
# ```
# rows = 5
# ```

# **Sample Output:**
# ```
# *********
#  *******
#   *****
#    ***
#     *
# ```

# ---

print("Answer 23: Inverted Pyramid Pattern")

n = 5

for i in range(1,n+1):
    for j in range(2,i+1):
        print(" ", end=" ")
    for j in range(1,(n+2)-i):
        print("*", end=" ")
    for j in range(2,(n+2)-i):
        print("*", end=" ")        
    print()

