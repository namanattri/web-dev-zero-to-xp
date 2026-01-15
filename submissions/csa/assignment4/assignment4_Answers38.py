# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 38: Zig-Zag Number Pattern
# Print numbers in a zig-zag pattern (alternate direction each row).

# **Sample Input:**
# ```
# rows = 5
# ```

# **Sample Output:**
# ```
# 1 2 3 4 5
# 10 9 8 7 6
# 11 12 13 14 15
# 20 19 18 17 16
# 21 22 23 24 25
# ```

# ---

print("Answer 38: Zig-Zag Number Pattern")

# n = 5
# p = 1
# q = n
# for i in range(n):
#     for j in range(n):
#         if i%2 == 0:
#             print(p, end=" ")
#         p += 1
#     print()


# chatgpt


n = 5

for i in range(n):
    start = i * n + 1
    end = start + n - 1
    # print("Row:", i, "Start:", start, "End:", end)
    if i%2 == 0:
        for j in range(start,end + 1):
            print(j,end=" ")
    else:
        for j in range(end,start-1,-1):
            print(j,end=" ")
    print()