# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 12: Number Pyramid
# Print a number pyramid pattern.

# **Sample Input:**
# ```
# rows = 4
# ```

# **Sample Output:**
# ```
# 1
# 1 2
# 1 2 3
# 1 2 3 4

print("Answer 12: Number Pyramid")

n = 4


# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=' ')
#     print()
        
for i in range(1,n+1):
    for j in range(1,n+1):
        if j <= i:
            print(j, end=' ')
        else:
            print(' ', end=' ')
    print()