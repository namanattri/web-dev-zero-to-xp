# Assignment 7: Dictionaries

Complete the following coding challenges to practice working with dictionaries and key-value pairs.

---

## Question 1: Student Grade Book
Create a dictionary to store student names and their grades. Add, update, and delete entries.

**Sample Input:**
```
Add: ("Alice", 85), ("Bob", 92), ("Charlie", 78)
Update: ("Alice", 90)
Delete: "Bob"
```

**Sample Output:**
```
Initial: {'Alice': 85, 'Bob': 92, 'Charlie': 78}
After update: {'Alice': 90, 'Bob': 92, 'Charlie': 78}
After delete: {'Alice': 90, 'Charlie': 78}
```

---

## Question 2: Word Frequency Counter
Count the frequency of each word in a sentence.

**Sample Input:**
```
sentence = "the quick brown fox jumps over the lazy dog the fox"
```

**Sample Output:**
```
{'the': 3, 'quick': 1, 'brown': 1, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
```

---

## Question 3: Dictionary Merge
Merge two dictionaries. If keys overlap, sum their values.

**Sample Input:**
```
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 25, 'd': 40}
```

**Sample Output:**
```
Merged: {'a': 10, 'b': 35, 'c': 55, 'd': 40}
```

---

## Question 4: Invert Dictionary
Create a new dictionary where keys become values and values become keys.

**Sample Input:**
```
original = {'a': 1, 'b': 2, 'c': 3}
```

**Sample Output:**
```
Inverted: {1: 'a', 2: 'b', 3: 'c'}
```

---

## Question 5: Phone Book
Create a phone book where you can add contacts, search by name, and list all contacts.

**Sample Input:**
```
Operations:
- Add: ("Alice", "555-1234")
- Add: ("Bob", "555-5678")
- Search: "Alice"
- List all
```

**Sample Output:**
```
Contact added: Alice
Contact added: Bob
Alice's number: 555-1234
All contacts:
  Alice: 555-1234
  Bob: 555-5678
```

---

## Question 6: Nested Dictionary - Students
Create a nested dictionary to store student information (name, age, grades).

**Sample Input:**
```
students = {
    'S001': {'name': 'Alice', 'age': 20, 'grades': [85, 90, 88]},
    'S002': {'name': 'Bob', 'age': 21, 'grades': [78, 82, 80]}
}
```

**Sample Output:**
```
Student S001:
  Name: Alice
  Age: 20
  Average grade: 87.67
```

---

## Question 7: Group Anagrams
Group words that are anagrams of each other.

**Sample Input:**
```
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

**Sample Output:**
```
{
    'aet': ['eat', 'tea', 'ate'],
    'ant': ['tan', 'nat'],
    'abt': ['bat']
}
```

---

## Question 8: Dictionary Comprehension
Create a dictionary of numbers (1-10) and their squares using dictionary comprehension.

**Sample Output:**
```
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
```

---

## Question 9: Character Position Mapper
Create a dictionary that maps each character in a string to its positions (indices).

**Sample Input:**
```
text = "hello"
```

**Sample Output:**
```
{'h': [0], 'e': [1], 'l': [2, 3], 'o': [4]}
```

---

## Question 10: Inventory Management
Manage product inventory with add, remove, and update stock operations.

**Sample Input:**
```
inventory = {"apple": 50, "banana": 30, "orange": 40}
Operations:
- Sell 10 apples
- Add 20 bananas
- Remove orange from inventory
```

**Sample Output:**
```
Initial: {'apple': 50, 'banana': 30, 'orange': 40}
After selling: {'apple': 40, 'banana': 30, 'orange': 40}
After adding: {'apple': 40, 'banana': 50, 'orange': 40}
After removing: {'apple': 40, 'banana': 50}
```

---

## Question 11: Default Values with get()
Access dictionary values safely using .get() with default values.

**Sample Input:**
```
scores = {'Alice': 85, 'Bob': 92}
names = ['Alice', 'Bob', 'Charlie']
```

**Sample Output:**
```
Alice's score: 85
Bob's score: 92
Charlie's score: Not found (default: 0)
```

---

## Question 12: Dictionary from Two Lists
Create a dictionary from two lists (keys and values).

**Sample Input:**
```
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
```

**Sample Output:**
```
{'name': 'Alice', 'age': 25, 'city': 'New York'}
```

---

## Question 13: Find Max Value in Dictionary
Find the key with the maximum value in a dictionary.

**Sample Input:**
```
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}
```

**Sample Output:**
```
Highest scorer: David with 95 points
```

---

## Question 14: Remove Keys with Condition
Remove all keys from a dictionary where the value is below a threshold.

**Sample Input:**
```
scores = {'Alice': 85, 'Bob': 55, 'Charlie': 78, 'David': 45}
threshold = 60
```

**Sample Output:**
```
After removing scores below 60:
{'Alice': 85, 'Charlie': 78}
```

---

## Question 15: Nested Dictionary Navigation
Access and modify values in a deeply nested dictionary.

**Sample Input:**
```
data = {
    'user': {
        'profile': {
            'name': 'Alice',
            'settings': {
                'theme': 'dark',
                'notifications': True
            }
        }
    }
}
```

**Sample Output:**
```
Theme: dark
After changing theme to 'light':
Theme: light
```

---

## Question 16: Dictionary Union
Combine multiple dictionaries into one (later values override earlier ones).

**Sample Input:**
```
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'c': 5, 'd': 6}
```

**Sample Output:**
```
Combined: {'a': 1, 'b': 3, 'c': 5, 'd': 6}
```

---

## Question 17: Sort Dictionary by Value
Sort a dictionary by its values in descending order.

**Sample Input:**
```
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}
```

**Sample Output:**
```
Sorted by score:
David: 95
Bob: 92
Alice: 85
Charlie: 78
```

---

## Question 18: Dictionary of Lists
Create a dictionary where values are lists, and perform operations like appending.

**Sample Input:**
```
courses = {
    'Math': ['Alice', 'Bob'],
    'Science': ['Charlie'],
    'History': ['Alice', 'David']
}
```

**Sample Output:**
```
Add 'Eve' to Math:
{'Math': ['Alice', 'Bob', 'Eve'], 'Science': ['Charlie'], 'History': ['Alice', 'David']}
```

---

## Question 19: Count Letter Grades
Convert numerical grades to letter grades and count each grade frequency.

**Sample Input:**
```
scores = [85, 92, 78, 95, 88, 76, 90, 82]
```

**Sample Output:**
```
Grade distribution:
A: 3
B: 4
C: 1
```

---

## Question 20: Two-Way Dictionary
Create a dictionary that can be looked up by either key or value (bidirectional).

**Sample Input:**
```
mapping = {'USA': 'Washington', 'France': 'Paris', 'Japan': 'Tokyo'}
```

**Sample Output:**
```
Capital of France: Paris
Country with capital Tokyo: Japan
```

