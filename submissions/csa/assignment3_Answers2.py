# Assignment 3: Control Flow (if/elif/else)

# Complete the following coding challenges to practice decision-making with control flow statements.


## Question 2: Grade Calculator
# Convert a numerical score to a letter grade:
# - A: 90-100
# - B: 80-89
# - C: 70-79
# - D: 60-69
# - F: Below 60

# **Sample Input:**
# ```
# score = 87
# ```

# **Sample Output:**
# ```
# Score: 87
# Grade: B
print("Answer 2: Grade Calculator")

score = 87

if score >= 90 and score <=100:
    print(f"Score: {score}\nGrade: A")

if score >= 80 and score < 90:
    print(f"Score: {score}\nGrade: B")

if score >= 70 and score < 80:
    print(f"Score: {score}\nGrade: C")

if score >= 60 and score < 70:
    print(f"Score: {score}\nGrade: D")

if score < 60:
    print(f"Score: {score}\nGrade: E")