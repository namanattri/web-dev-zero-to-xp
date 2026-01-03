# Assignment 3: Control Flow (if/elif/else)

# Complete the following coding challenges to practice decision-making with control flow statements.

# ## Question 11: Nested Decision - College Admission
# Check college admission eligibility:
# - Must have GPA >= 3.0
# - If GPA >= 3.5, check if SAT >= 1200 (Accepted)
# - If GPA 3.0-3.5, check if SAT >= 1300 (Accepted)
# - Otherwise: Not accepted

# **Sample Input:**
# ```
# gpa = 3.6
# sat = 1250
# ```

# **Sample Output:**
# ```
# Admission decision: Accepted
# ```

print("Answer 11: Nested Decision - College Admission")

gpa = 3.6
sat = 1250

if gpa >= 3.0 and sat >= 1300:
    print("Admission decision: Accepted") 
elif gpa >= 3.5 and sat >= 1200:
    print("Admission decision: Accepted")
else: 
    print("Admission decision: Not accepted")        