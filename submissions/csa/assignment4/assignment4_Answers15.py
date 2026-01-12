# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 15: Nested Loop - Multiplication Grid
# Print a multiplication grid from 1 to 5.

# **Sample Output:**
# ```
# 1  2  3  4  5
# 2  4  6  8  10
# 3  6  9  12 15
# 4  8  12 16 20
# 5  10 15 20 25

# ---
print("Answer 15: Nested Loop - Multiplication Grid")

n = 5

for i in range(1,n+1):
    for j in range(1,n+1):
        print(j*i,end="  ")
    print()