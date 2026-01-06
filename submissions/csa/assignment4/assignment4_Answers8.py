# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 8: Reverse a Number
# Reverse the digits of a number using a loop.

# **Sample Input:**
# ```
# number = 12345
# ```

# **Sample Output:**
# ```
# Reversed number: 54321
# ```

# ---
print("Answer 8: Reverse a Number")


n = 12345

for i in str(n)[::-1]: 
    print(i, end=' ')  


# n = 12345

# while n > 0:
#     print(n % 10, end=" ")
#     n //= 10    
