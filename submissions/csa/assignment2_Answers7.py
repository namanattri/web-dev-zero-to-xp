# # Assignment 2: Operators

# ## Question 7: Leap Year Checker
# Determine if a year is a leap year using logical and comparison operators.
# Rules: Divisible by 4 AND (not divisible by 100 OR divisible by 400)

# **Sample Input:**
# ```
# year = 2024
# ```

# **Sample Output:**
# ```
# 2024 is a leap year: True

print("Answer 7: Leap Year Checker")

year = 2024

is_true = True

if year% 2 == 0 and year%100 != 0 or year%400 == 0:
    print(f"{year} is a leap year: {is_true}")
