# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.
# ## Question 16: While Loop with Sentinel
# Keep asking for numbers and sum them until user enters -1.

# **Sample Input:**
# ```
# 5
# 10
# 15
# -1
# ```

# **Sample Output:**
# ```
# Enter a number (-1 to stop): 5
# Enter a number (-1 to stop): 10
# Enter a number (-1 to stop): 15
# Enter a number (-1 to stop): -1
# Total sum: 30
# ```
# ---
print("Answer 16: While Loop with Sentinel")


total = 0

while True:
    n = int(input("enter your number:- "))
    if n == -1:
        break
    total += n
print(f"Total sum {total}")
