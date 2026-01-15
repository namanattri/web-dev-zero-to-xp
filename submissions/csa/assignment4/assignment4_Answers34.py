# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 34: Hollow Pyramid
# Print a hollow pyramid pattern.

# **Sample Input:**
# ```
# rows = 5
# ```

# **Sample Output:**
# ```
#     *
#    * *
#   *   *
#  *     *
# *********
# ```

# ---

print("Answer 34: Hollow Pyramid")

n = 5

for i in range(n):
    for j in range(i,n-1):
        print(" ", end=" ")
    for j in range(i):
        if j == 0 or i== n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(i+1):
        if i == j or i == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")    
    
    print()




