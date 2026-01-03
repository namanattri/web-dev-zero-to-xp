# # Assignment 2: Operators


# ## Question 11: BMI Calculator
# Calculate BMI (Body Mass Index) using the formula: BMI = weight / (height²)
# Classify the BMI: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (≥30)

# **Sample Input:**
# ```
# weight = 70  # kg
# height = 1.75  # meters
# ```

# **Sample Output:**
# ```
# BMI: 22.86
# Classification: Normal weight

print("Answer 11: BMI Calculator")

weight = 70  # kg
height = 1.75  # meters

bmi = weight/(height**2)
if bmi <= 18.5:
    print(f"BMI: {bmi:.2f}\nClassification: Underweight")
if bmi > 18.5 and bmi <= 24.9:
    print(f"BMI: {bmi:.2f}\nClassification: Normal")
if bmi > 24.9 and bmi <= 29.9:
    print(f"BMI: {bmi:.2f}\nClassification: Overweight")  
if bmi > 29.9:
    print("Classification: Obese")  
