# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 7: Find First Divisible
# Find the first number between 1 and 100 that is divisible by both 7 and 9.

# **Sample Output:**
# ```
# The first number divisible by both 7 and 9 is: 63
# ```

# ---
print("Answer 7: Find First Divisible")

# n = 100

# for i in range(1,n+1):
#     if i % 7 == 0 and i % 9 == 0:
#         print(f"The first number divisible by both 7 and 9 is: {i}")
#         break
# print()

n = 1

while n <= 100:
    if n % 7 == 0 and n % 5 == 0:
        print(n)
        break
    n += 1
print()