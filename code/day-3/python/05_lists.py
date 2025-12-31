"""
Python Crash Course - Lesson 5: Lists
======================================
Learn to work with ordered collections of items
"""

# CREATING LISTS
print("=== CREATING LISTS ===")
# Lists can contain any type of data
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]
empty_list = []

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")
print(f"Empty list: {empty_list}")
print()

# ACCESSING LIST ITEMS
print("=== ACCESSING LIST ITEMS ===")
colors = ["red", "green", "blue", "yellow"]
print(f"First color: {colors[0]}")  # Index starts at 0
print(f"Second color: {colors[1]}")
print(f"Last color: {colors[-1]}")  # Negative index from end
print(f"Second to last: {colors[-2]}")
print()

# MODIFYING LISTS
print("=== MODIFYING LISTS ===")
animals = ["cat", "dog", "bird"]
print(f"Original: {animals}")

animals[1] = "hamster"  # Change an item
print(f"After modification: {animals}")
print()

# ADDING ITEMS
print("=== ADDING ITEMS ===")
numbers = [1, 2, 3]
print(f"Original: {numbers}")

numbers.append(4)  # Add to the end
print(f"After append(4): {numbers}")

numbers.insert(0, 0)  # Insert at specific position
print(f"After insert(0, 0): {numbers}")

numbers.extend([5, 6])  # Add multiple items
print(f"After extend([5, 6]): {numbers}")
print()

# REMOVING ITEMS
print("=== REMOVING ITEMS ===")
items = ["a", "b", "c", "d", "e"]
print(f"Original: {items}")

items.remove("c")  # Remove specific item
print(f"After remove('c'): {items}")

popped = items.pop()  # Remove and return last item
print(f"After pop(): {items}, Popped: {popped}")

popped_first = items.pop(0)  # Remove and return item at index
print(f"After pop(0): {items}, Popped: {popped_first}")
print()

# LIST OPERATIONS
print("=== LIST OPERATIONS ===")
nums = [3, 1, 4, 1, 5, 9, 2]
print(f"List: {nums}")
print(f"Length: {len(nums)}")
print(f"Sum: {sum(nums)}")
print(f"Max: {max(nums)}")
print(f"Min: {min(nums)}")
print(f"Count of 1: {nums.count(1)}")
print(f"Index of 4: {nums.index(4)}")
print()

# SORTING LISTS
print("=== SORTING LISTS ===")
numbers = [5, 2, 8, 1, 9]
print(f"Original: {numbers}")

numbers.sort()  # Sort in place
print(f"After sort(): {numbers}")

numbers.sort(reverse=True)  # Sort in reverse
print(f"After sort(reverse=True): {numbers}")

words = ["banana", "apple", "cherry"]
sorted_words = sorted(words)  # Returns new sorted list
print(f"Original words: {words}")
print(f"Sorted words: {sorted_words}")
print()

# LIST SLICING
print("=== LIST SLICING ===")
letters = ["a", "b", "c", "d", "e", "f"]
print(f"Full list: {letters}")
print(f"First three: {letters[0:3]}")
print(f"From index 2 onwards: {letters[2:]}")
print(f"Up to index 4: {letters[:4]}")
print(f"Last three: {letters[-3:]}")
print(f"Every second item: {letters[::2]}")
print(f"Reversed: {letters[::-1]}")
print()

# LOOPING THROUGH LISTS
print("=== LOOPING THROUGH LISTS ===")
fruits = ["apple", "banana", "orange"]

print("Method 1: Direct iteration")
for fruit in fruits:
    print(f"  {fruit}")
print()

print("Method 2: With index")
for i in range(len(fruits)):
    print(f"  {i}: {fruits[i]}")
print()

print("Method 3: Using enumerate")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")
print()

# LIST COMPREHENSIONS
# A concise way to create lists
print("=== LIST COMPREHENSIONS ===")

# Create a list of squares
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# Create a list of even numbers
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers: {evens}")

# Transform strings to uppercase
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"Uppercase: {upper_words}")
print()

# PRACTICAL EXAMPLES
print("=== PRACTICAL EXAMPLES ===")

# Example 1: Find sum of all even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = sum([x for x in numbers if x % 2 == 0])
print(f"Sum of even numbers: {even_sum}")

# Example 2: Filter list
scores = [45, 67, 89, 92, 56, 78, 88]
passing_scores = [score for score in scores if score >= 60]
print(f"Passing scores: {passing_scores}")

# Example 3: Remove duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))  # Convert to set and back to list
print(f"Unique numbers: {unique}")

# Example 4: Combine two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"Combined lists: {combined}")

# Example 5: Check if item exists
shopping_list = ["milk", "bread", "eggs"]
if "milk" in shopping_list:
    print("Milk is in the shopping list")

