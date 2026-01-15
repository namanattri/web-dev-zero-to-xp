# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 36: Reverse Number Triangle
# Print a triangle where each row shows numbers in reverse order.

# **Sample Input:**
# ```
# rows = 5
# ```

# **Sample Output:**
# ```
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# ```

# ---

print("Answer 36: Reverse Number Triangle")

n = 5

for i in range(1,n+1):
    for j in range(i):
        print(i, end=" ")
        i -= 1
    print()

