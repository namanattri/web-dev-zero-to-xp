# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 35: Number Pyramid (Centered)
# Print a centered number pyramid where numbers increase and then decrease.

# **Sample Input:**
# ```
# rows = 5
# ```

# **Sample Output:**
# ```
#     1
#    121
#   12321
#  1234321
# 123454321
# ```


# ---

print("Answer 35: Number Pyramid (Centered)")

n = 5

for i in range(n):
    p = 1
    
    for j in range(i,n-1):
        print(" ", end=" ")
    for j in range(i):
        print(p, end=" ")
        p += 1
    for j in range(i+1):
        print(p, end=" ")
        p -= 1   
    
    print()




