# Assignment 3: Control Flow (if/elif/else)

# Complete the following coding challenges to practice decision-making with control flow statements.

# ## Question 5: Ticket Pricing
# Calculate movie ticket price based on age:
# - Under 3: Free
# - 3-12: $10
# - 13-64: $20
# - 65+: $15

# **Sample Input:**
# ```
# age = 8
# ```

# **Sample Output:**
# ```
# Ticket price for age 8: $10
# ```

print("Answer 5: Ticket Pricing")

age = 8

if age <= 3:
    print(f"Ticket price for age  {age}: Free")

if age > 3 and age <= 12:
    print(f"Ticket price for age  {age}: $10")

if age >= 13 and age <= 64:
    print(f"Ticket price for age  {age}: $20")

if age >= 65:
    print(f"Ticket price for age  {age}: $15")

