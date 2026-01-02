# # Assignment 2: Operators

# ## Question 13: Password Strength
# Check password strength based on length (at least 8 characters) and if it contains a number. Use logical operators.

# **Sample Input:**
# ```
# password = "secure123"
# has_number = True
# length = 9
# ```

# **Sample Output:**
# ```
# Password strength: Strong (length >= 8 AND contains number)

# print("Answer 13: Password Strength")

# password = "secure123"
# has_number = True
# length = 9

password = "secure123"

has_number = any(char.isdigit() for char in password)

length = (len(password))

if length >= 8 and has_number == True:
    print(f"Password strength: Strong (length >= 8 AND contains number")
    
# print(has_number) 
# print(length)