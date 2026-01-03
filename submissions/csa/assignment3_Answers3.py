# Assignment 3: Control Flow (if/elif/else)

# Complete the following coding challenges to practice decision-making with control flow statements.

# ## Question 3: Login System
# Create a simple login system that checks username and password. Print appropriate messages for success or different failure reasons.

# **Sample Input:**
# ```
# username = "admin"
# password = "12345"
# correct_user = "admin"
# correct_pass = "admin123"
# ```

# **Sample Output:**
# ```
# Incorrect password
# ```

print("Answer 3: Login System")

username = "admin"
password = "12345"

if username == "admin" and password == "admin123":
    print("Login successful")
elif username == "admin" and password != "admin123":
    print("Incorrect password")
elif username != "admin" and password == "admin123":
    print("Incorrect username")    
else:
    print("Incorrect credential")

