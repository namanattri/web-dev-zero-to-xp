# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.


# ## Question 3: Countdown Timer
# Create a countdown from a given number to 0.

# **Sample Input:**
# ```
# start = 10
# ```

# **Sample Output:**
# ```
# 10
# 9
# 8
# ...
# 1
# Blast off!

print("Answer 3: Countdown Timer")

"""For Loop"""
# start = 10

# for i in range(10,-0,-1):
#     print(i)
# print("Blast off!")    

"""while Loop"""
start = 10

while start > 0:
    print(start)
    start -= 1 
print("Blast off!")    
