# Assignment 3: Control Flow (if/elif/else)

# Complete the following coding challenges to practice decision-making with control flow statements.

# ## Question 16: Tax Calculator
# Calculate tax based on income brackets:
# - $0-$10,000: 0%
# - $10,001-$40,000: 10%
# - $40,001-$80,000: 20%
# - $80,001+: 30%

# **Sample Input:**
# ```
# income = 55000
# ```

# **Sample Output:**
# ```
# Income: $55,000
# Tax rate: 20%
# Tax amount: $11,000
# After-tax income: $44,000
# ```

print("Answer 16: Tax Calculator")

income = 55000

if income > 0 and income <=10000:
    print(f"Income: ${income}\nTax rate: ${0}%\nTax amount: ${income*(0/100)}\nAfter-tax income: ${income-(income*(0/100))}")
elif income > 10000 and income <=40000:
    print(f"Income: ${income}\nTax rate: ${10}%\nTax amount: ${income*(10/100)}\nAfter-tax income: ${income-(income*(10/100))}")
elif income > 40000 and income <=80000:
    print(f"Income: ${income}\nTax rate: ${20}%\nTax amount: ${income*(20/100)}\nAfter-tax income: ${income-(income*(20/100))}")
elif income > 80000:
    print(f"Income: ${income}\nTax rate: ${30}%\nTax amount: ${income*(30/100)}\nAfter-tax income: ${income-(income*(30/100))}") 
else:
    print("Negative or zero value not allowed")   