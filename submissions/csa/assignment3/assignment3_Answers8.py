# Assignment 3: Control Flow (if/elif/else)

# Complete the following coding challenges to practice decision-making with control flow statements.

# ## Question 8: Shipping Cost Calculator
# Calculate shipping cost based on order total:
# - $0-$50: $10 shipping
# - $50-$100: $5 shipping
# - Over $100: Free shipping

# **Sample Input:**
# ```
# order_total = 75
# ```

# **Sample Output:**
# ```
# Order total: $75
# Shipping cost: $5
# Final total: $80
# ```

print("Answer 8: Shipping Cost Calculator")
order_total = 75



if order_total > 0 and order_total <= 50:
    print(f"Order total: ${order_total}\nShipping cost: $10\nFinal total: ${order_total + 10} ")
elif order_total > 50 and order_total <= 100:
    print(f"Order total: ${order_total}\nShipping cost: $5\nFinal total: ${order_total + 5} ")
elif order_total > 100:
    print(f"Order total: ${order_total}\nShipping cost: Free\nFinal total: ${order_total + 0} ")    