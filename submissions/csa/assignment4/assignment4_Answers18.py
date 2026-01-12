# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 18: GCD Calculator
# Find the Greatest Common Divisor (GCD) of two numbers using a while loop.

# **Sample Input:**
# ```
# a = 48
# b = 18
# ```

# **Sample Output:**
# ```
# GCD of 48 and 18 is: 6
# ```

# ---
print("Answer 18: GCD Calculator")

a = 48
b = 18

# c = min(a,b)
# print(c)
gcd = 1
for i in range(1,min(a,b)+1):
    if a % i == 0 and b % i == 0:
        gcd = i
print(f"GCD of {a} and {b} is: {gcd}")