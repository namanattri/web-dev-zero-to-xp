# # Assignment 2: Operators

# ## Question 14: Temperature Range
# Check if temperature is comfortable (between 20°C and 25°C inclusive).

# **Sample Input:**
# ```
# temperature = 22
# ```

# **Sample Output:**
# ```
# Temperature 22°C is comfortable: True

print("Answer 14: Temperature Range")

temperature = 22
is_true = True

if temperature >= 20 and temperature <= 25:
    print(f"Temperature {temperature}°C is comfortable: {is_true}")
