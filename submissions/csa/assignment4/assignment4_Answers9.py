# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 9: Digit Sum Calculator
# Calculate the sum of all digits in a number.

# **Sample Input:**
# ```
# number = 12345
# ```

# **Sample Output:**
# ```
# Sum of digits in 12345: 15
# ```

# ---
print("Answer 9: Digit Sum Calculator")

# number = 12345

# total = 0

# for i in str(number):
#     total += int(i)

# print(total)

number = 12345
total = 0

while number > 0:
    digit = number % 10
    total += digit
    number //= 10

print(total)
  