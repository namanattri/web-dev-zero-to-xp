# # Assignment 2: Operators

# ## Question 8: Grade Boundary Checker
# Check if a score falls within grade boundaries using comparison operators.

# **Sample Input:**
# ```
# score = 85
# ```

# **Sample Output:**
# ```
# Score 85 is between 80 and 90: True
# Grade: B

print("Answer 8: Grade Boundary Checker")

score = 85
is_true = True


if score >= 80 and score <= 90:
    print(f"Score 85 is between 80 and 90: {is_true}\nGrade: B") 