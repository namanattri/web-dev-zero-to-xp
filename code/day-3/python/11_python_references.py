"""
Python Crash Course - Lesson 10: Understanding Python References
==================================================================
Learn how Python handles variables, references, and memory
"""

# PYTHON VARIABLES ARE REFERENCES
print("=== PYTHON VARIABLES ARE REFERENCES ===")
print("In Python, variables are references (names) that point to objects in memory")
print()

# Example 1: Variables point to objects
x = 5
print(f"x = {x}")
print(f"Memory address of x: {id(x)}")
print(f"Type of x: {type(x)}")
print()

# MULTIPLE REFERENCES TO SAME OBJECT
print("=== MULTIPLE REFERENCES TO SAME OBJECT ===")

# With mutable objects (lists)
list1 = [1, 2, 3]
list2 = list1  # Both variables reference the SAME list object

print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list1 memory address: {id(list1)}")
print(f"list2 memory address: {id(list2)}")
print(f"Are they the same object? {list1 is list2}")
print()

# Modify through one reference
list2.append(4)
print("After list2.append(4):")
print(f"list1: {list1}")  # list1 also changed!
print(f"list2: {list2}")
print()

# MUTABLE VS IMMUTABLE OBJECTS
print("=== MUTABLE VS IMMUTABLE OBJECTS ===")

# IMMUTABLE: int, float, string, tuple, frozenset
print("Immutable objects (int, float, string, tuple):")
a = 10
b = a  # b references same object as a
print(f"a = {a}, b = {b}")
print(f"a is b: {a is b}")  # True - same object

b = 20  # b now references a NEW object
print(f"After b = 20:")
print(f"a = {a}, b = {b}")
print(f"a is b: {a is b}")  # False - different objects now
print()

# MUTABLE: list, dict, set
print("Mutable objects (list, dict, set):")
list_a = [1, 2, 3]
list_b = list_a  # References same object
print(f"list_a: {list_a}, list_b: {list_b}")
print(f"list_a is list_b: {list_a is list_b}")

list_b.append(4)  # Modifies the shared object
print(f"After list_b.append(4):")
print(f"list_a: {list_a}, list_b: {list_b}")  # Both changed!
print()

# IDENTITY VS EQUALITY
print("=== IDENTITY VS EQUALITY ===")

# 'is' checks if two variables reference the SAME object
# '==' checks if two objects have the SAME value

list1 = [1, 2, 3]
list2 = [1, 2, 3]  # New list with same values
list3 = list1       # Reference to same list

print(f"list1: {list1}, id: {id(list1)}")
print(f"list2: {list2}, id: {id(list2)}")
print(f"list3: {list3}, id: {id(list3)}")
print()

print(f"list1 == list2: {list1 == list2}")  # True - same values
print(f"list1 is list2: {list1 is list2}")  # False - different objects
print()

print(f"list1 == list3: {list1 == list3}")  # True - same values
print(f"list1 is list3: {list1 is list3}")  # True - same object
print()

# COPYING OBJECTS
print("=== COPYING OBJECTS ===")

# Method 1: Using copy() method (shallow copy)
original = [1, 2, 3, 4]
copy1 = original.copy()

print(f"original: {original}, id: {id(original)}")
print(f"copy1: {copy1}, id: {id(copy1)}")
print(f"Are they the same object? {original is copy1}")
print()

copy1.append(5)
print("After copy1.append(5):")
print(f"original: {original}")  # Unchanged!
print(f"copy1: {copy1}")
print()

# Method 2: Using list() constructor
copy2 = list(original)
print(f"copy2 = list(original): {copy2}")
print(f"original is copy2: {original is copy2}")
print()

# Method 3: Using slice notation
copy3 = original[:]
print(f"copy3 = original[:]: {copy3}")
print(f"original is copy3: {original is copy3}")
print()

# SHALLOW COPY VS DEEP COPY
print("=== SHALLOW COPY VS DEEP COPY ===")

# Shallow copy: copies outer list but inner lists are still references
nested_original = [[1, 2], [3, 4], [5, 6]]
nested_shallow = nested_original.copy()

print(f"nested_original: {nested_original}")
print(f"nested_shallow: {nested_shallow}")
print(f"Are they the same? {nested_original is nested_shallow}")
print(f"Are inner lists the same? {nested_original[0] is nested_shallow[0]}")
print()

# Modify inner list
nested_shallow[0].append(99)
print("After nested_shallow[0].append(99):")
print(f"nested_original: {nested_original}")  # Also changed!
print(f"nested_shallow: {nested_shallow}")
print("⚠️ Shallow copy doesn't copy nested objects!")
print()

# Deep copy: copies everything recursively
import copy
nested_original2 = [[1, 2], [3, 4], [5, 6]]
nested_deep = copy.deepcopy(nested_original2)

print(f"nested_original2: {nested_original2}")
print(f"nested_deep: {nested_deep}")
print(f"Are inner lists the same? {nested_original2[0] is nested_deep[0]}")
print()

nested_deep[0].append(99)
print("After nested_deep[0].append(99):")
print(f"nested_original2: {nested_original2}")  # Unchanged!
print(f"nested_deep: {nested_deep}")
print("✅ Deep copy creates independent copies!")
print()

# FUNCTION PARAMETERS ARE REFERENCES
print("=== FUNCTION PARAMETERS ARE REFERENCES ===")

def modify_list(lst):
    """This function receives a reference to the list"""
    lst.append(99)
    print(f"Inside function: {lst}")

def reassign_list(lst):
    """This function reassigns the local variable"""
    lst = [1, 2, 3]  # Creates new local list
    print(f"Inside function: {lst}")

my_list = [1, 2, 3]
print(f"Before modify_list: {my_list}")
modify_list(my_list)
print(f"After modify_list: {my_list}")  # Changed!
print()

my_list2 = [10, 20, 30]
print(f"Before reassign_list: {my_list2}")
reassign_list(my_list2)
print(f"After reassign_list: {my_list2}")  # Unchanged!
print()

# SAFE FUNCTION PARAMETER PASSING
print("=== SAFE FUNCTION PARAMETER PASSING ===")

def safe_modify(lst):
    """Create a copy to avoid modifying original"""
    local_copy = lst.copy()
    local_copy.append(99)
    return local_copy

original_list = [1, 2, 3]
print(f"Original: {original_list}")
modified_list = safe_modify(original_list)
print(f"After safe_modify:")
print(f"  Original: {original_list}")  # Unchanged
print(f"  Modified: {modified_list}")  # New list
print()

# NONE - PYTHON'S NULL REFERENCE
print("=== NONE - PYTHON'S NULL REFERENCE ===")

value = None
print(f"value: {value}")
print(f"Type: {type(value)}")
print(f"Is it None? {value is None}")  # Use 'is' with None
print(f"Is it truthy? {bool(value)}")  # None is falsy
print()

# Checking for None
def get_user_name(user_id):
    """Simulate function that might return None"""
    if user_id == 1:
        return "Alice"
    return None

name = get_user_name(2)
if name is None:
    print("User not found")
else:
    print(f"User: {name}")
print()

# PRACTICAL EXAMPLES
print("=== PRACTICAL EXAMPLES ===")

# Example 1: Avoiding unintended modifications
print("\n--- Example 1: Avoiding Unintended Modifications ---")
def process_scores(scores):
    """Process scores without modifying original"""
    sorted_scores = scores.copy()  # Create copy
    sorted_scores.sort()
    return sorted_scores

original_scores = [85, 92, 78, 90]
sorted_scores = process_scores(original_scores)
print(f"Original scores: {original_scores}")  # Unchanged
print(f"Sorted scores: {sorted_scores}")
print()

# Example 2: Default mutable arguments (COMMON MISTAKE!)
print("\n--- Example 2: Mutable Default Arguments ---")

def add_item_wrong(item, lst=[]):  # DON'T DO THIS!
    """WRONG: Default list is shared across calls"""
    lst.append(item)
    return lst

def add_item_correct(item, lst=None):  # DO THIS!
    """CORRECT: Create new list each time"""
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print("Wrong approach:")
list1 = add_item_wrong("apple")
list2 = add_item_wrong("banana")
print(f"list1: {list1}")  # ['apple', 'banana'] - Unexpected!
print(f"list2: {list2}")  # ['apple', 'banana'] - Same object!
print()

print("Correct approach:")
list3 = add_item_correct("apple")
list4 = add_item_correct("banana")
print(f"list3: {list3}")  # ['apple']
print(f"list4: {list4}")  # ['banana']
print()

# Example 3: Understanding list operations
print("\n--- Example 3: List Operations and References ---")
a = [1, 2, 3]
b = a

print(f"Initial: a = {a}, b = {b}")
print(f"a is b: {a is b}")

# Modifying in place
a.append(4)
print(f"After a.append(4): a = {a}, b = {b}")  # Both changed
print(f"a is b: {a is b}")  # Still same object
print()

# Reassigning creates new object
a = a + [5]  # Creates NEW list
print(f"After a = a + [5]: a = {a}, b = {b}")  # b unchanged
print(f"a is b: {a is b}")  # Different objects now
print()

# Example 4: Dictionary references
print("\n--- Example 4: Dictionary References ---")
dict1 = {"name": "Alice", "age": 25}
dict2 = dict1  # Reference to same dictionary

print(f"dict1: {dict1}")
print(f"dict2: {dict2}")

dict2["age"] = 26
print(f"After dict2['age'] = 26:")
print(f"dict1: {dict1}")  # Also changed!
print(f"dict2: {dict2}")
print()

# Create independent copy
dict3 = dict1.copy()
dict3["age"] = 30
print(f"After dict3['age'] = 30:")
print(f"dict1: {dict1}")  # Unchanged
print(f"dict3: {dict3}")
print()

print("="*60)
print("KEY TAKEAWAYS:")
print("1. Python variables are references to objects")
print("2. Mutable objects can be modified through any reference")
print("3. Use .copy() to create independent copies")
print("4. Use copy.deepcopy() for nested structures")
print("5. Use 'is' to check if references point to same object")
print("6. Use '==' to check if values are equal")
print("7. Function parameters are passed by reference")
print("="*60)

