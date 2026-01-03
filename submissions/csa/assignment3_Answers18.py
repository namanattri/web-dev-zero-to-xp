# Assignment 3: Control Flow (if/elif/else)

# Complete the following coding challenges to practice decision-making with control flow statements.

# ## Question 18: Number Sign and Magnitude
# Check if a number is positive/negative/zero AND small (<10), medium (10-100), or large (>100).

# **Sample Input:**
# ```
# num = 75
# ```

# **Sample Output:**
# ```
# 75 is positive and medium
# ```

print("Answer 18: Number Sign and Magnitude")

num = 75

if num > 0 and num <=10:
    print(f"{num} is positive and small")
elif num > 10 and num <=100:
    print(f"{num} is positive and medium")
elif num > 100:
    print(f"{num} is positive and large")
elif num < 0 and num >= -10:
    print(f"{num} is negative and small")
elif num < -10 and num >= -100:
    print(f"{num} is negative and medium")
elif num <= -100:
    print(f"{num} is negative and Large") 
else:
    print(f"{num} is zero")                       