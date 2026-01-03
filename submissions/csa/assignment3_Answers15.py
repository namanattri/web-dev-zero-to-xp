# Assignment 3: Control Flow (if/elif/else)

# Complete the following coding challenges to practice decision-making with control flow statements.

# ## Question 15: Password Validator
# Check if a password meets requirements:
# - At least 8 characters long
# - If less than 8: "Too short"
# - If 8-12: "Medium strength"
# - If 13+: "Strong"

# **Sample Input:**
# ```
# password = "mypassword123"
# length = 13
# ```

# **Sample Output:**
# ```
# Password strength: Strong
# ```

print("Answer 15: Password Validator")

password = "mypassword123"
length = (len(password))

print("At least 8 characters long")

if length < 8:
    print("Password strength: Too short")

elif length >= 8 and length <= 12:
    print("Password strength: Medium strength")

elif length >= 13:
    print("Password strength: Strong")

