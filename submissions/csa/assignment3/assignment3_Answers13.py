# Assignment 3: Control Flow (if/elif/else)

# Complete the following coding challenges to practice decision-making with control flow statements.

# ## Question 13: BMI Category
# Calculate BMI and categorize: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (30+).

# **Sample Input:**
# ```
# weight = 70  # kg
# height = 1.75  # meters
# ```

# **Sample Output:**
# ```
# BMI: 22.86
# Category: Normal weight
# ```

print("Answer 13: BMI Category")

weight = 70  # kg
height = 1.75  # meters

bmi = weight/(height**2)
if bmi <= 18.5:
    print(f"BMI: {bmi:.2f}\nCategory: Underweight")
if bmi > 18.5 and bmi <= 24.9:
    print(f"BMI: {bmi:.2f}\nCategory: Normal weight")
if bmi > 24.9 and bmi <= 29.9:
    print(f"BMI: {bmi:.2f}\nCategory: Overweight")  
if bmi > 29.9:
    print("Category: Obese")  