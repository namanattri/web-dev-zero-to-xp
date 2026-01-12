# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 13: Fibonacci Sequence
# Generate the first N numbers of the Fibonacci sequence.

# **Sample Input:**
# ```
# n = 10
# ```

# **Sample Output:**
# ```
# 0 1 1 2 3 5 8 13 21 34
# ```

print("Answer 13: Fibonacci Sequence")

n = int(input("Upto which number you want fibonacci:- "))
# n = 10
a = 0
b = 1
if n == 1:
    print(a, end=" ")
elif n == 2:
    print(a,b, end=" ")
else:
    print(a,b, end=" ")
    for i in range(3,n+1):
        temp = b
        b = a + b
        a = temp
        print(b, end=" ")
