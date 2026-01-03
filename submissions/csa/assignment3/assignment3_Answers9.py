# Assignment 3: Control Flow (if/elif/else)

# Complete the following coding challenges to practice decision-making with control flow statements.

# ## Question 9: Largest of Three Numbers
# Find and print the largest of three given numbers.

# **Sample Input:**
# ```
# a = 23
# b = 45
# c = 17
# ```

# **Sample Output:**
# ```
# The largest number is: 45
# ```

print("Answer 9: Largest of Three Numbers")

a = 23
b = 45
c = 17

if a > b and a > c:
    print(f"The largest number is: {a}")
elif b > a and b > c:
    print(f"The largest number is: {b}")
else:
    print(f"The largest number is: {c}")
