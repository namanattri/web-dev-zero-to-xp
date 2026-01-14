# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 29: Right-Aligned Number Triangle
# Print a right-aligned triangle where each row shows numbers from 1 to row number.

# **Sample Input:**
# ```
# rows = 5
# ```

# **Sample Output:**
# ```
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5
# ```

# ---

print("Answer 29: Right-Aligned Number Triangle")

n = 5

for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i+1):
        print(j+1, end=" ")
    print()
