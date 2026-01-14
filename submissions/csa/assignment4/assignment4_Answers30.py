# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 30: Alphabetic Triangle Pattern
# Print a triangle pattern using alphabets.

# **Sample Input:**
# ```
# rows = 5
# ```

# **Sample Output:**
# ```
# A
# A B
# A B C
# A B C D
# A B C D E
# ```

# ---

print("Answer 30: Alphabetic Triangle Pattern")
n = 5

for i in range(n):
    p = 65
    for j in range(i+1):
        print(chr(p), end=" ")
        p += 1
    print()


