# Assignment 3: Control Flow (if/elif/else)

# Complete the following coding challenges to practice decision-making with control flow statements.

# ## Question 19: Restaurant Bill Splitter
# Calculate individual cost based on number of people and whether to include tip:
# - If party size > 5: Add 18% gratuity automatically
# - Otherwise: Ask if they want to add 15% tip

# **Sample Input:**
# ```
# total_bill = 150
# party_size = 6
# ```

# **Sample Output:**
# ```
# Total bill: $150
# Party size: 6
# Automatic gratuity (18%): $27.00
# Total with tip: $177.00
# Per person: $29.50
# ```

print("Answer 19: Restaurant Bill Splitter")

total_bill = 150
party_size = 6

if party_size > 5:
    print(f"Total bill: ${total_bill}\nParty size: {party_size}\nAutomatic gratuity (18%): ${total_bill*(18/100)}\nTotal with tip: ${total_bill+(total_bill*(18/100))}\nPer person: ${(total_bill+(total_bill*(18/100)))/party_size}")
else:
    print(f"Total bill: ${total_bill}\nParty size: {party_size}\nAutomatic gratuity (0%): ${total_bill*(0)}\nTotal with tip: ${total_bill+(total_bill*(0))}\nPer person: ${(total_bill+(total_bill*(0)))/party_size}")    