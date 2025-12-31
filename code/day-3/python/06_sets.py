"""
Python Crash Course - Lesson 6: Sets
=====================================
Learn to work with unique, unordered collections
"""

# WHAT ARE SETS?
print("=== WHAT ARE SETS? ===")
print("Sets are unordered collections of unique elements")
print("- No duplicates allowed")
print("- No indexing (unordered)")
print("- Fast membership testing")
print("- Mutable (can add/remove items)")
print()

# CREATING SETS
print("=== CREATING SETS ===")

# Using curly braces
fruits = {"apple", "banana", "orange"}
print(f"Fruits set: {fruits}")

# Using set() constructor
numbers = set([1, 2, 3, 4, 5])
print(f"Numbers set: {numbers}")

# Set automatically removes duplicates
duplicates = {1, 2, 2, 3, 3, 3, 4}
print(f"Set with duplicates: {duplicates}")  # {1, 2, 3, 4}

# Empty set (must use set(), not {})
empty_set = set()
print(f"Empty set: {empty_set}")
print(f"Type: {type(empty_set)}")

empty_dict = {}  # This creates a dictionary, not a set!
print(f"Empty dict: {empty_dict}, Type: {type(empty_dict)}")
print()

# ADDING ITEMS
print("=== ADDING ITEMS ===")
colors = {"red", "green", "blue"}
print(f"Original: {colors}")

# Add single item
colors.add("yellow")
print(f"After add('yellow'): {colors}")

# Add duplicate (no effect)
colors.add("red")
print(f"After add('red') again: {colors}")  # Still same

# Add multiple items
colors.update(["purple", "orange", "pink"])
print(f"After update(): {colors}")
print()

# REMOVING ITEMS
print("=== REMOVING ITEMS ===")
numbers = {1, 2, 3, 4, 5}
print(f"Original: {numbers}")

# remove() - raises error if item doesn't exist
numbers.remove(3)
print(f"After remove(3): {numbers}")

# discard() - no error if item doesn't exist
numbers.discard(10)  # No error
print(f"After discard(10): {numbers}")  # Unchanged

# pop() - removes and returns arbitrary item
popped = numbers.pop()
print(f"After pop(): {numbers}, Popped: {popped}")

# clear() - removes all items
temp_set = {1, 2, 3}
temp_set.clear()
print(f"After clear(): {temp_set}")
print()

# SET OPERATIONS
print("=== SET OPERATIONS ===")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print()

# Union (all elements from both sets)
union = set_a | set_b
print(f"Union (A | B): {union}")
# Or use .union()
union2 = set_a.union(set_b)
print(f"Union (A.union(B)): {union2}")
print()

# Intersection (common elements)
intersection = set_a & set_b
print(f"Intersection (A & B): {intersection}")
# Or use .intersection()
intersection2 = set_a.intersection(set_b)
print(f"Intersection (A.intersection(B)): {intersection2}")
print()

# Difference (elements in A but not in B)
difference = set_a - set_b
print(f"Difference (A - B): {difference}")
# Or use .difference()
difference2 = set_a.difference(set_b)
print(f"Difference (A.difference(B)): {difference2}")
print()

# Symmetric Difference (elements in A or B but not both)
sym_diff = set_a ^ set_b
print(f"Symmetric Difference (A ^ B): {sym_diff}")
# Or use .symmetric_difference()
sym_diff2 = set_a.symmetric_difference(set_b)
print(f"Symmetric Difference (A.symmetric_difference(B)): {sym_diff2}")
print()

# SUBSET AND SUPERSET
print("=== SUBSET AND SUPERSET ===")

set_x = {1, 2, 3}
set_y = {1, 2, 3, 4, 5}
set_z = {6, 7, 8}

print(f"X: {set_x}")
print(f"Y: {set_y}")
print(f"Z: {set_z}")
print()

# Subset (all elements of X are in Y)
print(f"Is X subset of Y? {set_x.issubset(set_y)}")  # True
print(f"Is X <= Y? {set_x <= set_y}")  # True

# Superset (Y contains all elements of X)
print(f"Is Y superset of X? {set_y.issuperset(set_x)}")  # True
print(f"Is Y >= X? {set_y >= set_x}")  # True

# Disjoint (no common elements)
print(f"Are X and Z disjoint? {set_x.isdisjoint(set_z)}")  # True
print(f"Are X and Y disjoint? {set_x.isdisjoint(set_y)}")  # False
print()

# MEMBERSHIP TESTING
print("=== MEMBERSHIP TESTING ===")
fruits = {"apple", "banana", "orange", "grape"}

print(f"Fruits: {fruits}")
print(f"Is 'apple' in fruits? {'apple' in fruits}")  # True
print(f"Is 'mango' in fruits? {'mango' in fruits}")  # False
print(f"Is 'mango' not in fruits? {'mango' not in fruits}")  # True
print()

# LOOPING THROUGH SETS
print("=== LOOPING THROUGH SETS ===")
colors = {"red", "green", "blue", "yellow"}

print("Colors:")
for color in colors:
    print(f"  {color}")
print()

# FROZEN SETS (Immutable Sets)
print("=== FROZEN SETS ===")

# Frozenset is immutable (cannot add/remove items)
immutable_set = frozenset([1, 2, 3, 4, 5])
print(f"Frozen set: {immutable_set}")
print(f"Type: {type(immutable_set)}")

# Can be used as dictionary keys (regular sets cannot)
# Can be elements of other sets
outer_set = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Set of frozen sets: {outer_set}")
print()

# SET COMPREHENSIONS
print("=== SET COMPREHENSIONS ===")

# Create set of squares
squares = {x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Create set of even numbers
evens = {x for x in range(1, 11) if x % 2 == 0}
print(f"Even numbers: {evens}")

# Process strings
words = ["hello", "world", "hello", "python", "world"]
unique_upper = {word.upper() for word in words}
print(f"Unique uppercase words: {unique_upper}")
print()

# PRACTICAL EXAMPLES
print("=== PRACTICAL EXAMPLES ===")

# Example 1: Remove duplicates from list
print("\n--- Example 1: Remove Duplicates ---")
numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]
unique_numbers = list(set(numbers))
print(f"Original list: {numbers}")
print(f"Unique numbers: {unique_numbers}")
# Note: Order is not preserved!

# To preserve order while removing duplicates
def remove_duplicates_preserve_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

unique_ordered = remove_duplicates_preserve_order(numbers)
print(f"Unique (order preserved): {unique_ordered}")
print()

# Example 2: Find common elements
print("\n--- Example 2: Find Common Elements ---")
course_a_students = {"Alice", "Bob", "Charlie", "David"}
course_b_students = {"Charlie", "David", "Eve", "Frank"}

common_students = course_a_students & course_b_students
print(f"Course A students: {course_a_students}")
print(f"Course B students: {course_b_students}")
print(f"Students in both courses: {common_students}")
print()

# Example 3: Find unique elements
print("\n--- Example 3: Find Unique to Each ---")
only_in_a = course_a_students - course_b_students
only_in_b = course_b_students - course_a_students
print(f"Only in Course A: {only_in_a}")
print(f"Only in Course B: {only_in_b}")
print()

# Example 4: Check for unique characters
print("\n--- Example 4: Unique Characters in String ---")
text = "hello world"
unique_chars = set(text)
print(f"Text: '{text}'")
print(f"Unique characters: {unique_chars}")
print(f"Number of unique chars: {len(unique_chars)}")
print()

# Example 5: Tag system
print("\n--- Example 5: Tag Management ---")
user1_tags = {"python", "coding", "beginner"}
user2_tags = {"python", "advanced", "data-science"}

all_tags = user1_tags | user2_tags
common_interests = user1_tags & user2_tags
unique_to_user1 = user1_tags - user2_tags

print(f"User 1 tags: {user1_tags}")
print(f"User 2 tags: {user2_tags}")
print(f"All tags: {all_tags}")
print(f"Common interests: {common_interests}")
print(f"Unique to user 1: {unique_to_user1}")
print()

# Example 6: Validate unique IDs
print("\n--- Example 6: Check for Duplicates ---")
user_ids = [101, 102, 103, 104, 103, 105]
if len(user_ids) != len(set(user_ids)):
    print(f"⚠️ Duplicate IDs found!")
    print(f"Total IDs: {len(user_ids)}")
    print(f"Unique IDs: {len(set(user_ids))}")
else:
    print("✅ All IDs are unique")
print()

# Example 7: Mathematical sets
print("\n--- Example 7: Mathematical Operations ---")
vowels = set("aeiou")
alphabet_sample = set("abcdefghij")

print(f"Vowels: {vowels}")
print(f"Sample alphabet: {alphabet_sample}")
print(f"Vowels in sample: {vowels & alphabet_sample}")
print(f"Consonants in sample: {alphabet_sample - vowels}")
print()

print("="*60)
print("KEY TAKEAWAYS:")
print("1. Sets store unique elements only")
print("2. Sets are unordered (no indexing)")
print("3. Fast for membership testing")
print("4. Support mathematical operations (union, intersection, etc.)")
print("5. Use sets to remove duplicates")
print("6. Use frozenset for immutable sets")
print("="*60)

