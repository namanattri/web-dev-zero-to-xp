# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 4: Pattern Printing - Stars
# Print a right-angled triangle pattern using stars.

# **Sample Input:**
# ```
# rows = 5
# ```

# **Sample Output:**
# ```
# *
# **
# ***
# ****
# *****
# ```

print("Answer 4: Pattern Printing - Stars")

rows = 5

for i in range(1,rows+1):
    for j in range(i):
        print("*" ,end=" ")
    print()

# for i in range(rows):
#     for j in range(rows):
#         print('*', end=' ')
#     print()