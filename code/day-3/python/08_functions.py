"""
Python Crash Course - Lesson 8: Functions
==========================================
Learn to create reusable blocks of code
"""

# BASIC FUNCTION
print("=== BASIC FUNCTION ===")

def greet():
    """A simple function that prints a greeting"""
    print("Hello, World!")

greet()  # Call the function
print()

# FUNCTION WITH PARAMETERS
print("=== FUNCTION WITH PARAMETERS ===")

def greet_person(name):
    """Greet a person by name"""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")
print()

# FUNCTION WITH MULTIPLE PARAMETERS
print("=== MULTIPLE PARAMETERS ===")

def add_numbers(a, b):
    """Add two numbers"""
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)
add_numbers(10, 20)
print()

# FUNCTION WITH RETURN VALUE
print("=== RETURN VALUES ===")

def multiply(a, b):
    """Multiply two numbers and return the result"""
    return a * b

result = multiply(4, 5)
print(f"4 x 5 = {result}")

# Use return value in another expression
total = multiply(3, 7) + 10
print(f"(3 x 7) + 10 = {total}")
print()

# DEFAULT PARAMETERS
print("=== DEFAULT PARAMETERS ===")

def greet_with_title(name, title="Mr."):
    """Greet with optional title"""
    print(f"Hello, {title} {name}!")

greet_with_title("Smith")  # Uses default title
greet_with_title("Johnson", "Dr.")  # Custom title
print()

# KEYWORD ARGUMENTS
print("=== KEYWORD ARGUMENTS ===")

def describe_pet(animal, name, age):
    """Display pet information"""
    print(f"I have a {animal} named {name}, age {age}")

# Using positional arguments
describe_pet("dog", "Buddy", 3)

# Using keyword arguments (order doesn't matter)
describe_pet(name="Whiskers", age=2, animal="cat")
print()

# RETURN MULTIPLE VALUES
print("=== RETURN MULTIPLE VALUES ===")

def get_min_max(numbers):
    """Return both minimum and maximum values"""
    return min(numbers), max(numbers)

nums = [3, 7, 1, 9, 4]
minimum, maximum = get_min_max(nums)
print(f"List: {nums}")
print(f"Min: {minimum}, Max: {maximum}")
print()

# ARBITRARY ARGUMENTS (*args)
print("=== ARBITRARY ARGUMENTS (*args) ===")

def sum_all(*numbers):
    """Sum any number of arguments"""
    total = sum(numbers)
    return total

print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 5, 10, 15, 20: {sum_all(5, 10, 15, 20)}")
print()

# ARBITRARY KEYWORD ARGUMENTS (**kwargs)
print("=== ARBITRARY KEYWORD ARGUMENTS (**kwargs) ===")

def print_info(**info):
    """Print any number of keyword arguments"""
    for key, value in info.items():
        print(f"  {key}: {value}")

print("Person info:")
print_info(name="Alice", age=25, city="NYC")
print()

# FUNCTION WITH DOCSTRING
print("=== FUNCTION DOCUMENTATION ===")

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
    
    Returns:
        The area of the rectangle
    """
    return length * width

area = calculate_area(5, 3)
print(f"Area: {area}")
# Access docstring
print(f"Function doc: {calculate_area.__doc__.strip()}")
print()

# PRACTICAL EXAMPLES
print("=== PRACTICAL EXAMPLES ===")

# Example 1: Temperature converter
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")
print()

# Example 2: Check if number is even
def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0

print(f"Is 4 even? {is_even(4)}")
print(f"Is 7 even? {is_even(7)}")
print()

# Example 3: Find factorial
def factorial(n):
    """Calculate factorial of n"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"Factorial of 5: {factorial(5)}")
print()

# Example 4: Filter list
def get_passing_scores(scores, passing_mark=60):
    """Return list of scores above passing mark"""
    return [score for score in scores if score >= passing_mark]

all_scores = [45, 78, 92, 55, 88, 67]
passing = get_passing_scores(all_scores)
print(f"All scores: {all_scores}")
print(f"Passing scores: {passing}")
print()

# Example 5: String formatter
def format_name(first, last):
    """Format name to title case"""
    return f"{first.title()} {last.title()}"

full_name = format_name("john", "doe")
print(f"Formatted name: {full_name}")
print()

# Example 6: List statistics
def get_statistics(numbers):
    """Return dictionary of statistics"""
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }

data = [10, 20, 30, 40, 50]
stats = get_statistics(data)
print(f"Statistics for {data}:")
for key, value in stats.items():
    print(f"  {key}: {value}")

