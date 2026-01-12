# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 20: Armstrong Number Checker
# Check if a number is an Armstrong number (sum of cubes of digits equals the number).

# **Sample Input:**
# ```
# number = 153
# ```

# **Sample Output:**
# ```
# 153 is an Armstrong number
# (1³ + 5³ + 3³ = 1 + 125 + 27 = 153)
# ```

# --
print("Answer 20: Armstrong Number Checker")

num1 = 153

temp = num1

num2 = len(str(num1))

sum1 = 0

while num1 != 0:
    sum2 = num1 % 10
    sum1 = sum1 +(sum2 ** num2)
    num1 = num1 // 10
if temp == sum1:
    print(temp," is an Armstrong number")
else:
    print(temp," is not an Armstrong number")

