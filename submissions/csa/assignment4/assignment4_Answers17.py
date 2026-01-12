# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 17: Find Power of 2
# Find all powers of 2 less than or equal to N.

# **Sample Input:**
# ```
# n = 100
# ```

# **Sample Output:**
# ```
# 1 2 4 8 16 32 64
# ```
# ---
print("Answer 17: Find Power of 2")

# n = int(input("Upto which number you want power of 2:- "))
n = 100
power = 1
    
count = 0 
while power <= n:
    print(power, end=' ')
    power *= 2
    count +=1

