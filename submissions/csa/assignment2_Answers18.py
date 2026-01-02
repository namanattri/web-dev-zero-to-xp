# # Assignment 2: Operators

# ## Question 18: Logical Operators Practice
# Given three boolean variables, evaluate complex logical expressions.

# **Sample Input:**
# ```
# a = True
# b = False
# c = True
# ```

# **Sample Output:**
# ```
# a and b: False
# a or b: True
# not a: False
# a and (b or c): True
# (a or b) and not c: False

print("Answer 18: Logical Operators Practice")

a = True
b = False
c = True

print(f"a and b: {a and b}")
print(f"a or b: {a or b}")
print(f"not a: {not a}")
print(f"a and (b or c): {a and (b or c)}")
print(f"(a or b) not c: {(a or b) != c}")