# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 25: Number Triangle Pattern
# Print a triangle pattern where each row contains the row number repeated.

# **Sample Input:**
# ```
# rows = 5
# ```

# **Sample Output:**
# ```
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# ```

# ---

print("Answer 25: Number Triangle Pattern")


n = 5

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end=" ")    
    print()
