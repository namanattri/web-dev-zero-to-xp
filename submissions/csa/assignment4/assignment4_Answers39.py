# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 39: Sandglass Number Pattern
# Print a sandglass pattern using numbers.

# **Sample Input:**
# ```
# n = 5
# ```

# **Sample Output:**
# ```
# 1 2 3 4 5
#  2 3 4 5
#   3 4 5
#    4 5
#     5
#    4 5
#   3 4 5
#  2 3 4 5
# 1 2 3 4 5
# ```

# ---

print("Answer 39: Sandglass Number Pattern")

n = 5
p = 1
q = 5
for i in range(n-1):
    for j in range(i+1):
        print(" ", end="")
    for j in range(n-i):
        print(p + j, end=" ")
    p += 1
    print()
for i in range(n):
    for j in range(i,n):
        print(" ", end="")
    for j in range(i+1):
        print(q + j, end=" ")
    q -= 1
    print()