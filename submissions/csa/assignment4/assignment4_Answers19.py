# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 19: Diamond Pattern
# Print a diamond pattern using nested loops.

# **Sample Input:**
# ```
# n = 3
# ```

# **Sample Output:**
# ```
#   *
#  ***
# *****
#  ***
#   *
# ```
# ---
print("Answer 19: Diamond Pattern")

n = 3

for i in range(1,n+1):
    for j in range(1,(n+1)-i):
        print(" ", end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    # for j in range(2,i+1):
    #     print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(1,(n+1)-i):
        print(" ", end=" ")
    for j in range(1,2*i):
        print("*",end=" ")       
    print()