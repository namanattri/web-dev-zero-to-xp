# # Assignment 3: Control Flow (if/elif/else)

# Complete the following coding challenges to practice decision-making with control flow statements.

# ---

# ## Question 1: Age Category
# Write a program that categorizes a person's age into: Child (0-12), Teen (13-19), Adult (20-59), Senior (60+).

# **Sample Input:**
# ```
# age = 25
# ```

# **Sample Output:**
# ```
# Age category: Adult
# 
print("Answer 1: Age Category")

age = 25

if age >= 0 and age <=12:
    print("Age category: Child")

if age > 12 and age <=19:
    print("Age category: Teen")

if age > 19 and age < 60:
    print("Age category: Adult")

if age >= 60:
    print("Age category: Senior")