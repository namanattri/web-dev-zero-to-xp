# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 37: X Pattern
# Print an X pattern using stars in a square grid.

# **Sample Input:**
# ```
# size = 7
# ```

# **Sample Output:**
# ```
# *     *
#  *   *
#   * *
#    *
#   * *
#  *   *
# *     *
# ```

# ---

print("Answer 37: X Pattern")

n = 7

# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(i,n-1):
#         if j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ") 
#     for j in range(i,n):
#         if j== n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")               
#     print()
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(i,n-1):
#         if j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ") 
#     for j in range(i,n):
#         if j== n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")               
#     print()

for i in range(n):
    for j in range(n):
        if (j == i or j+i == n-1 ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()