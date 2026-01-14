# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 28: Hollow Diamond Pattern
# Print a hollow diamond pattern using stars.

# **Sample Input:**
# ```
# n = 5
# ```

# **Sample Output:**
# ```
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *
# ```

# ---

print("Answer 28: Hollow Diamond Pattern")

n = 5

for i in range(n-1):
    for j in range(i,n-1):
        print(" ", end=" ")
    for j in range(i):
        if (j == 0):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(i+1):
        if (j == i):
            print("*", end=" ")
        else:
            print(" ", end=" ")  
    print()
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(i,n):
        if (j == i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(i,n):
        if (j == n-2):
            print("*", end=" ")
        else:
            print(" ", end=" ") 
        
    print()    