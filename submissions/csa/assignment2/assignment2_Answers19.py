# # Assignment 2: Operators

# ## Question 19: Time Converter
# Convert minutes to hours and minutes using floor division and modulus.

# **Sample Input:**
# ```
# total_minutes = 135
# ```

# **Sample Output:**
# ```
# 135 minutes = 2 hours and 15 minutes

print("Answer 19: Time Converter")

total_minutes = 135

hour = total_minutes//60

minute = total_minutes%60

print(f"{total_minutes} minutes = {hour} hours and {minute} minutes")