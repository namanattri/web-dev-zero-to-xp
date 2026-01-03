# Assignment 3: Control Flow (if/elif/else)

# Complete the following coding challenges to practice decision-making with control flow statements.

# ## Question 14: Quadrant Finder
# Given x and y coordinates, determine which quadrant a point lies in (or if it's on an axis).

# **Sample Input:**
# ```
# x = 3
# y = -5
# ```

# **Sample Output:**
# ```
# Point (3, -5) is in Quadrant IV
# ```

print("Answer 14: Quadrant Finder")

x = 3
y = -5

if x > 0 and y > 0:
    print(f"Point ({x}, {y}) is in Quadrant I")
elif x < 0 and y > 0:
    print(f"Point ({x}, {y}) is in Quadrant II")  
elif x < 0 and y < 0:
    print(f"Point ({x}, {y}) is in Quadrant III") 
elif x > 0 and y < 0:
    print(f"Point ({x}, {y}) is in Quadrant IV")            
elif x < 0 and y == 0 or x > 0 and y == 0:
    print(f"Point ({x}, {y}) is in Quadrant x-axis") 
elif x == 0 and y > 0 or x == 0 and y < 0 :
    print(f"Point ({x}, {y}) is in Quadrant y-axis")   
elif x == 0 and y == 0:
    print(f"Point ({x}, {y}) is in Quadrant origin")           