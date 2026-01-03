# Assignment 3: Control Flow (if/elif/else)

# Complete the following coding challenges to practice decision-making with control flow statements.

# ## Question 10: Season Identifier
# Identify the season based on month number (12, 1, 2: Winter; 3, 4, 5: Spring; 6, 7, 8: Summer; 9, 10, 11: Fall).

# **Sample Input:**
# ```
# month = 7
# ```

# **Sample Output:**
# ```
# Month 7 is in Summer
# ```

print("Answer 10: Season Identifier")

month = 7

if month == 12 or month == 1 or month == 2:
    print(f"Month {month} is in Winter")
elif month == 3 or month == 4 or month == 5:
    print(f"Month {month} is in Spring") 
elif month == 6 or month == 7 or month == 8:
    print(f"Month {month} is in Summer") 
elif month == 9 or month == 10 or month == 11:
    print(f"Month {month} is in Fall")
else:
    print("Not a month number")               