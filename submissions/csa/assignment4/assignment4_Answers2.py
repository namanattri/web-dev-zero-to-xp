# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ---
# ## Question 2: Sum of First N Numbers
# Calculate the sum of first N natural numbers using a loop.

# **Sample Input:**
# ```
# n = 10
# ```

# **Sample Output:**
# ```
# Sum of first 10 numbers: 55
# ```
print("Answer 2: Sum of First N Numbers")

"""For Loop"""
# n = 10
# total = 0

# for i in range(1,n+1):
#     total += i
# print(f"Sum of first {n} numbers: {total}")

"""while Loop"""
n = 10
total = 0
sum = 1

while sum <= n:
    total += sum
    sum += 1   
print(f"Sum of first 10 numbers: {total}")
  
     



