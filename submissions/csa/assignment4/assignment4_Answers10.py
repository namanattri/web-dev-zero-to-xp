# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 10: Prime Number Checker
# Check if a number is prime using a loop to test divisibility.

# **Sample Input:**
# ```
# number = 17
# ```

# **Sample Output:**
# ```
# 17 is a prime number
# ```

# ---
print("Answer 10: Prime Number Checker")

# n = 5
# count = 0
# for i in range(2,n+1):
    
#     if n % i == 0:
#         count += 1
    
# if count == 1:
#     print(f"{n} is a prime number")
# else:   
#     print(f"{n} is not a prime number")


n = 5
count = 0
i = 1
while i <= n:
    
    if n % i == 0:
        count += 1
    i += 1
if count == 2:
    print(f"{n} is a prime number")
else:   
    print(f"{n} is not a prime number")

