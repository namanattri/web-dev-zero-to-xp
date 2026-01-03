# Assignment 3: Control Flow (if/elif/else)

# Complete the following coding challenges to practice decision-making with control flow statements.

# ## Question 12: Discount Eligibility
# Apply discount based on multiple conditions:
# - Senior citizen (65+) OR student: 15% discount
# - Regular customer with loyalty card: 10% discount
# - New customer: No discount

# **Sample Input:**
# ```
# age = 70
# is_student = False
# has_loyalty_card = True
# ```

# **Sample Output:**
# ```
# Discount applied: 15% (Senior citizen)
# ```

print("Answer 12: Discount Eligibility")

age = 70
is_student = False
has_loyalty_card = True

if age >= 65:
    print("Discount applied: 15% (Senior citizen)")
elif is_student == True:
    print("Discount applied: 15% (Student)") 
elif age < 65 and has_loyalty_card == True :
    print("Discount applied: 10% (customer with loyalty card)") 
else:
    print("New customer: No discount")     