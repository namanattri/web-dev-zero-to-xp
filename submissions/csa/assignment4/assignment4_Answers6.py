# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 6: Even Numbers in Range
# Print all even numbers between 1 and N.

# **Sample Input:**
# ```
# n = 20
# ```

# **Sample Output:**
# ```
# 2 4 6 8 10 12 14 16 18 20
# ```

# ---
print("Answer 6: Even Numbers in Range")

# n = 20
# for i in range(1,n+1):
#     if i % 2 != 0:
#         continue
#     print(i, end=" ")
# print()

n = 1
while n <= 20:
    if n % 2 == 0:
       print(n, end=' ')
    n += 1
print()       

    
