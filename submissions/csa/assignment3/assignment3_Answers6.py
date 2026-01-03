# Assignment 3: Control Flow (if/elif/else)

# Complete the following coding challenges to practice decision-making with control flow statements.

# ## Question 6: Triangle Type Classifier
# Given three sides of a triangle, classify it as Equilateral (all sides equal), Isosceles (two sides equal), or Scalene (all sides different).

# **Sample Input:**
# ```
# side1 = 5
# side2 = 5
# side3 = 7
# ```

# **Sample Output:**
# ```
# Triangle type: Isosceles
# ```

print("Answer 6: Triangle Type Classifier")

side1 = 5
side2 = 5
side3 = 7


if side1 == side2 and side2 == side3:
    print("Triangle type: Equilateral")
elif side1 == side2 != side3 or side1 == side3 != side2 or side2 == side3 != side1 or side3 == side2 != side1:
    print("Triangle type: Isosceles")
else:
    print("Triangle type: Scalene")        