"""
Python Crash Course - Lesson 6: Dictionaries
=============================================
Learn to work with key-value pairs
"""

# CREATING DICTIONARIES
print("=== CREATING DICTIONARIES ===")
# Dictionaries store data in key-value pairs
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(f"Person: {person}")

# Empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")
print()

# ACCESSING VALUES
print("=== ACCESSING VALUES ===")
student = {
    "name": "John",
    "grade": "A",
    "score": 95
}

print(f"Name: {student['name']}")
print(f"Grade: {student['grade']}")

# Using get() method (safer - returns None if key doesn't exist)
print(f"Score: {student.get('score')}")
print(f"Age (not in dict): {student.get('age', 'Not found')}")
print()

# MODIFYING DICTIONARIES
print("=== MODIFYING DICTIONARIES ===")
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020
}
print(f"Original: {car}")

# Update existing value
car["year"] = 2021
print(f"After updating year: {car}")

# Add new key-value pair
car["color"] = "blue"
print(f"After adding color: {car}")
print()

# REMOVING ITEMS
print("=== REMOVING ITEMS ===")
inventory = {
    "apples": 10,
    "oranges": 5,
    "bananas": 8
}
print(f"Original: {inventory}")

# Remove specific key
del inventory["oranges"]
print(f"After deleting oranges: {inventory}")

# Remove and return value
count = inventory.pop("bananas")
print(f"After popping bananas: {inventory}, Count: {count}")
print()

# DICTIONARY METHODS
print("=== DICTIONARY METHODS ===")
product = {
    "name": "Laptop",
    "price": 999,
    "brand": "Dell"
}

print(f"Keys: {list(product.keys())}")
print(f"Values: {list(product.values())}")
print(f"Items: {list(product.items())}")
print(f"Length: {len(product)}")
print()

# CHECKING IF KEY EXISTS
print("=== CHECKING KEY EXISTENCE ===")
book = {
    "title": "Python Basics",
    "author": "John Doe",
    "pages": 300
}

if "title" in book:
    print(f"Title exists: {book['title']}")

if "isbn" not in book:
    print("ISBN not found in book dictionary")
print()

# LOOPING THROUGH DICTIONARIES
print("=== LOOPING THROUGH DICTIONARIES ===")
scores = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92
}

print("Method 1: Loop through keys")
for name in scores:
    print(f"  {name}: {scores[name]}")
print()

print("Method 2: Loop through keys explicitly")
for name in scores.keys():
    print(f"  {name}")
print()

print("Method 3: Loop through values")
for score in scores.values():
    print(f"  Score: {score}")
print()

print("Method 4: Loop through key-value pairs")
for name, score in scores.items():
    print(f"  {name} scored {score}")
print()

# NESTED DICTIONARIES
print("=== NESTED DICTIONARIES ===")
students = {
    "student1": {
        "name": "Alice",
        "grade": "A",
        "score": 95
    },
    "student2": {
        "name": "Bob",
        "grade": "B",
        "score": 87
    }
}

print(f"Student 1 name: {students['student1']['name']}")
print(f"Student 2 score: {students['student2']['score']}")
print()

# DICTIONARY COMPREHENSION
print("=== DICTIONARY COMPREHENSION ===")
# Create a dictionary of squares
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Filter dictionary
prices = {"apple": 1.5, "banana": 0.5, "orange": 2.0}
expensive = {fruit: price for fruit, price in prices.items() if price > 1.0}
print(f"Expensive fruits: {expensive}")
print()

# PRACTICAL EXAMPLES
print("=== PRACTICAL EXAMPLES ===")

# Example 1: Word counter
text = "hello world hello python world"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print(f"Word count: {word_count}")
print()

# Example 2: Student grade tracker
students_grades = {
    "Alice": [85, 90, 92],
    "Bob": [78, 82, 88],
    "Charlie": [95, 93, 97]
}

for student, grades in students_grades.items():
    average = sum(grades) / len(grades)
    print(f"{student}'s average: {average:.2f}")
print()

# Example 3: Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}  # Python 3.5+
print(f"Merged dictionaries: {merged}")
print()

# Example 4: Inventory management
inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 20
}

# Update inventory
inventory["apples"] -= 10  # Sold 10 apples
inventory["grapes"] = 25   # Added new item
print(f"Updated inventory: {inventory}")
print()

# Example 5: Convert list of tuples to dictionary
pairs = [("name", "Alice"), ("age", 25), ("city", "NYC")]
person_dict = dict(pairs)
print(f"Person from tuples: {person_dict}")

