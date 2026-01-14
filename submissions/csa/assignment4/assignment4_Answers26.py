# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 26: Floyd's Triangle
# Print Floyd's triangle (consecutive numbers arranged in rows).

# **Sample Input:**
# ```
# rows = 5
# ```

# **Sample Output:**
# ```
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# ```

# ---

print("Answer 26: Floyd's Triangle")

n = 5
n2 = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n2, end=" ")
        n2 += 1
    print()