# # Assignment 4: Loops (for and while)

# Complete the following coding challenges to practice iteration with loops.

# ## Question 14: Character Counter
# Count how many times a specific character appears in a string using a loop.

# **Sample Input:**
# ```
# text = "hello world"
# char = 'l'
# ```

# **Sample Output:**
# ```
# Character 'l' appears 3 times in "hello world"
# ```
# ---
print("Answer 14: Character Counter")

text = "hello world"
char = "l"
count = 0

for i in text:
    if i == char:
        count += 1
print(f"Character {char} appears {count} times in \"{text}\" ")

