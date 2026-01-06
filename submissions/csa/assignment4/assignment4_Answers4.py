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

"""For Loop"""
# n = 5

# for i in range(1,n+1):
#     for j in range(i):
#         print("*" ,end=" ")
#     print()

# for i in range(rows):
#     for j in range(rows):
#         print('*', end=' ')
#     print()

"""while Loop"""
n = 5
row = 1
while row <= n:
    col = 1
    while col <= row:
        print("*", end=" ")
        col += 1
    print()
    row += 1

