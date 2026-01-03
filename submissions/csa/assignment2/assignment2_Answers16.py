# # Assignment 2: Operators

# ## Question 16: Shopping Cart Total
# Calculate total with discount and tax. If total > $100, apply 10% discount. Then add 8% tax.

# **Sample Input:**
# ```
# price1 = 45
# price2 = 60
# price3 = 30
# ```

# **Sample Output:**
# ```
# Subtotal: $135.00
# After discount: $121.50
# After tax: $131.22
# Final total: $131.22

print("Answer 16: Shopping Cart Total")

price1 = 45
price2 = 60
price3 = 30

st = price1+price2+price3
ad = st-(st*10/100)
at = ad+(ad*8/100)

print(f"Subtotal: ${st}\nAfter discount: ${ad}\nAfter tax: ${at}\nFinal total: ${at}")