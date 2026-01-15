# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 31: Alternating Pattern
# Print a checkerboard/alternating pattern using two symbols.

# **Sample Input:**
# ```
# rows = 5
# cols = 5
# ```

# **Sample Output:**
# ```
# * # * # *
# # * # * #
# * # * # *
# # * # * #
# * # * # *
# ```


# ---

print("Answer 31: Alternating Pattern")

n = 5


for i in range(n):
    for j in range(n):
        if (i%2 == 0 and j%2 == 0) or (i%2 != 0 and j%2 != 0):
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()



