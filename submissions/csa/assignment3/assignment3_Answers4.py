# Assignment 3: Control Flow (if/elif/else)

# Complete the following coding challenges to practice decision-making with control flow statements.

# ## Question 4: Traffic Light
# Write a program that tells you what to do based on a traffic light color (Red: Stop, Yellow: Slow down, Green: Go).

# **Sample Input:**
# ```
# light = "Yellow"
# ```

# **Sample Output:**
# ```
# Traffic light is Yellow: Slow down
# ```

print("Answer 4: Traffic Light")

color = input("light color is: - ")

if color == "Red":
    print("Traffic light is Yellow: Stop")
elif color == "Yellow":
    print("Traffic light is Yellow: Slow down")
elif color == "Green":
    print("Traffic light is Yellow: Go")
else:
    print("Not a traffic signal color")            