# Assignment 11: JavaScript/TypeScript References

Complete the following coding challenges to practice understanding references, mutability, and memory management in JavaScript/TypeScript.

---

## Question 1: Variable Reference Demo
Demonstrate how variables reference objects in JavaScript/TypeScript.

**Sample Code:**
```typescript
const a: number[] = [1, 2, 3];
const b: number[] = a;
```

**Sample Output:**
```
a: [1, 2, 3]
b: [1, 2, 3]
Are a and b the same object? true (a === b)
After b.push(4):
a: [1, 2, 3, 4]
b: [1, 2, 3, 4]
```

---

## Question 2: Immutable vs Mutable
Show the difference between mutable and immutable object behavior.

**Sample Output:**
```
=== IMMUTABLE (int) ===
x = 5, id: 123456
y = x, id: 123456
After y = 10:
x = 5, id: 123456
y = 10, id: 789012

=== MUTABLE (list) ===
list1 = [1, 2], id: 234567
list2 = list1, id: 234567
After list2.append(3):
list1 = [1, 2, 3]
list2 = [1, 2, 3]
```

---

## Question 3: Array Copy Methods
Demonstrate different ways to copy an array and their effects.

**Sample Output:**
```
Original: [1, 2, 3]

Method 1: Assignment (b = a)
Modifying b affects a: true

Method 2: Spread operator [...a]
Modifying b affects a: false

Method 3: Array.from()
Modifying b affects a: false

Method 4: .slice()
Modifying b affects a: false
```

---

## Question 4: Shallow vs Deep Copy
Demonstrate the difference with nested arrays.

**Sample Output:**
```
Original: [[1, 2], [3, 4]]

Shallow copy (using spread):
After modifying inner array:
Original: [[1, 2, 99], [3, 4]]
Shallow: [[1, 2, 99], [3, 4]]
Both affected!

Deep copy (using JSON.parse(JSON.stringify())):
After modifying inner array:
Original: [[1, 2], [3, 4]]
Deep: [[1, 2, 99], [3, 4]]
Only deep copy affected!
```

---

## Question 5: Function Parameter Modification
Show how function parameters work with references.

**Sample Output:**
```
=== Modifying mutable parameter ===
Before: [1, 2, 3]
Inside function: [1, 2, 3, 4]
After: [1, 2, 3, 4]
Original was modified!

=== Reassigning parameter ===
Before: [1, 2, 3]
Inside function: [10, 20]
After: [1, 2, 3]
Original unchanged!
```

---

## Question 6: Identity vs Equality
Demonstrate the difference between `is` and `==`.

**Sample Output:**
```
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

list1 == list2: True (same values)
list1 is list2: False (different objects)

list1 == list3: True (same values)
list1 is list3: True (same object)
```

---

## Question 7: Mutable Default Parameter
Demonstrate default parameters with objects/arrays in JavaScript/TypeScript.

**Sample Output:**
```
=== WITH DEFAULT EMPTY ARRAY ===
Call 1: [1]
Call 2: [2]
Call 3: [3]
Note: JavaScript doesn't share default arrays like Python

=== CORRECT WAY (being explicit) ===
Call 1: [1]
Call 2: [2]
Call 3: [3]
Each call gets new array!
```

---

## Question 8: Dictionary Reference Behavior
Show how dictionaries behave with references.

**Sample Output:**
```
dict1 = {'a': 1, 'b': 2}
dict2 = dict1

After dict2['c'] = 3:
dict1: {'a': 1, 'b': 2, 'c': 3}
dict2: {'a': 1, 'b': 2, 'c': 3}
Both modified!

Using .copy():
dict3: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict1: {'a': 1, 'b': 2, 'c': 3}
Independent!
```

---

## Question 9: None Reference
Demonstrate proper None checking and usage.

**Sample Output:**
```
value = None
Type: <class 'NoneType'>
Is None: True
Is falsy: True

Using 'is None' (correct):
if value is None: Value is None

Using '== None' (works but not preferred):
if value == None: Value is None
```

---

## Question 10: String Interning
Show how Python interns small strings.

**Sample Output:**
```
Small strings:
a = "hello", b = "hello"
a is b: True (interned)

Large strings:
c = "hello world", d = "hello world"
c is d: False (not interned)
c == d: True (same value)
```

---

## Question 11: List Modification in Loop
Show the danger of modifying a list while iterating.

**Sample Output:**
```
=== WRONG: Modifying during iteration ===
Original: [1, 2, 3, 4, 5]
Trying to remove evens...
Result: [1, 3, 5]
Some elements skipped!

=== CORRECT: Iterate over copy ===
Original: [1, 2, 3, 4, 5]
Result: [1, 3, 5]
All evens removed correctly!
```

---

## Question 12: Reference Counter
Demonstrate reference counting concept (using id).

**Sample Output:**
```
a = [1, 2, 3]
Number of references: 1

b = a
Number of references: 2

c = a
Number of references: 3

del b
Number of references: 2
```

---

## Question 13: Nested Dictionary Copy
Show deep copy necessity with nested dictionaries.

**Sample Output:**
```
Original: {'user': {'name': 'Alice', 'age': 25}}

Shallow copy:
Modified nested value in copy
Original: {'user': {'name': 'Bob', 'age': 25}}
Also changed!

Deep copy:
Modified nested value in copy
Original: {'user': {'name': 'Alice', 'age': 25}}
Unchanged!
```

---

## Question 14: List Aliasing
Create multiple references to the same list and show effects.

**Sample Output:**
```
aliases = [a, b, c] all pointing to same list

Initial: [1, 2, 3]

a.append(4)
All aliases: [1, 2, 3, 4]

b[0] = 99
All aliases: [99, 2, 3, 4]

All changes reflected everywhere!
```

---

## Question 15: Tuple Immutability with Mutable Contents
Show that tuples containing mutable objects can change.

**Sample Output:**
```
t = ([1, 2], 3, 4)

Trying t[0] = [99]: Error! Tuple is immutable

But: t[0].append(3) works!
Result: ([1, 2, 3], 3, 4)

Tuple structure unchanged, but list inside modified!
```

---

## Question 16: Chained Assignment
Demonstrate chained assignment with mutable objects.

**Sample Output:**
```
a = b = c = [1, 2, 3]

All three reference same list:
id(a): 123456
id(b): 123456
id(c): 123456

Modify through any variable:
c.append(4)
All show: [1, 2, 3, 4]
```

---

## Question 17: Return Reference from Function
Show that returning mutable objects returns references.

**Sample Output:**
```
original = get_list()
copy1 = original
copy2 = original.copy()

Modifying original:
original: [1, 2, 3, 4]
copy1: [1, 2, 3, 4] (same reference)
copy2: [1, 2, 3] (independent copy)
```

---

## Question 18: Global vs Local Reference
Demonstrate reference behavior with global keyword.

**Sample Output:**
```
Global list: [1, 2, 3]

Function without global:
Inside: [10, 20]
Outside: [1, 2, 3] (unchanged)

Function with global:
Inside: [10, 20]
Outside: [10, 20] (changed)
```

---

## Question 19: Memory Address Tracking
Track memory addresses through operations.

**Sample Output:**
```
Creating list:
a = [1, 2, 3], id: 140234567890

Appending (in-place):
a = [1, 2, 3, 4], id: 140234567890 (same)

Concatenating (new object):
a = [1, 2, 3, 4, 5, 6], id: 140234999999 (different)
```

---

## Question 20: Reference Practical Example
Implement a function that safely processes a list without modifying the original.

**Sample Code:**
```python
def process_safely(data):
    """Process list without modifying original"""
    # Your implementation here
    pass

def process_unsafely(data):
    """Process list that modifies original"""
    # Your implementation here
    pass
```

**Sample Output:**
```
Original: [1, 2, 3, 4, 5]

After unsafe processing:
Original: [2, 4, 6, 8, 10]
Modified!

Original: [1, 2, 3, 4, 5]
After safe processing:
Original: [1, 2, 3, 4, 5]
Result: [2, 4, 6, 8, 10]
Unchanged!
```

