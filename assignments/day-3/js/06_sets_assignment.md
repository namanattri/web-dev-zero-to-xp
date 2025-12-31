# Assignment 6: Sets

Complete the following coding challenges to practice working with sets and set operations in JavaScript/TypeScript.

---

## Question 1: Remove Duplicates
Convert an array with duplicates into an array with unique elements using sets.

**Sample Input:**
```typescript
const numbers: number[] = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7];
```

**Sample Output:**
```
Original: [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
Unique: [1, 2, 3, 4, 5, 6, 7]
```

---

## Question 2: Common Elements
Find elements that are common between three lists.

**Sample Input:**
```
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [4, 5, 7, 8, 9]
```

**Sample Output:**
```
Common elements: {4, 5}
```

---

## Question 3: Unique Characters
Find all unique characters in a string (case-insensitive).

**Sample Input:**
```
text = "Hello World"
```

**Sample Output:**
```
Unique characters: {' ', 'd', 'e', 'h', 'l', 'o', 'r', 'w'}
Count: 8
```

---

## Question 4: Set Difference - Students
Find students who are in Course A but not in Course B.

**Sample Input:**
```
course_a = {"Alice", "Bob", "Charlie", "David"}
course_b = {"Bob", "David", "Eve", "Frank"}
```

**Sample Output:**
```
Students only in Course A: {'Alice', 'Charlie'}
```

---

## Question 5: Symmetric Difference - Products
Find products that are in either Store A or Store B, but not in both.

**Sample Input:**
```
store_a = {"apple", "banana", "orange", "grape"}
store_b = {"banana", "grape", "mango", "kiwi"}
```

**Sample Output:**
```
Products in only one store: {'apple', 'orange', 'mango', 'kiwi'}
```

---

## Question 6: Subset Checker
Check if one set is a subset of another and provide appropriate message.

**Sample Input:**
```
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
```

**Sample Output:**
```
{1, 2, 3} is a subset of {1, 2, 3, 4, 5}: True
```

---

## Question 7: Superset Validation
Check if a set is a superset of multiple other sets.

**Sample Input:**
```
main_set = {1, 2, 3, 4, 5, 6, 7, 8}
sub1 = {1, 2, 3}
sub2 = {4, 5}
sub3 = {9, 10}
```

**Sample Output:**
```
Is superset of sub1: True
Is superset of sub2: True
Is superset of sub3: False
```

---

## Question 8: Disjoint Sets
Check if two sets have no elements in common.

**Sample Input:**
```
set_a = {1, 2, 3, 4}
set_b = {5, 6, 7, 8}
```

**Sample Output:**
```
Sets are disjoint: True
```

---

## Question 9: Union of Multiple Sets
Find the union of three or more sets.

**Sample Input:**
```
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}
set4 = {7, 8, 9}
```

**Sample Output:**
```
Union of all sets: {1, 2, 3, 4, 5, 6, 7, 8, 9}
```

---

## Question 10: Intersection of Multiple Sets
Find elements common to all sets.

**Sample Input:**
```
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4, 5, 6}
set3 = {3, 4, 5, 6, 7}
```

**Sample Output:**
```
Common to all sets: {3, 4, 5}
```

---

## Question 11: Tag System
Implement a simple tag system. Find posts that have at least one common tag.

**Sample Input:**
```
post1_tags = {"python", "programming", "tutorial"}
post2_tags = {"python", "data-science", "ml"}
post3_tags = {"java", "programming", "oop"}
```

**Sample Output:**
```
Posts 1 and 2 share: {'python'}
Posts 1 and 3 share: {'programming'}
Posts 2 and 3 share: set()
```

---

## Question 12: Vowel Counter
Count unique vowels in a sentence.

**Sample Input:**
```
sentence = "The quick brown fox jumps over the lazy dog"
```

**Sample Output:**
```
Unique vowels: {'a', 'e', 'i', 'o', 'u'}
Count: 5
```

---

## Question 13: Set Comprehension
Create a set of squares of odd numbers from 1 to 20.

**Sample Output:**
```
Squares of odd numbers: {1, 9, 25, 49, 81, 121, 169, 225, 289, 361}
```

---

## Question 14: Word Uniqueness Checker
Check if all words in a sentence are unique.

**Sample Input:**
```
sentence = "the quick brown fox"
```

**Sample Output:**
```
All words unique: True
```

**Sample Input 2:**
```
sentence = "the quick brown the fox"
```

**Sample Output 2:**
```
All words unique: False
Duplicate: the
```

---

## Question 15: Set Operations Menu
Given two sets, perform all set operations and display results.

**Sample Input:**
```
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
```

**Sample Output:**
```
Set A: {1, 2, 3, 4, 5}
Set B: {4, 5, 6, 7, 8}
Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}
Difference (A-B): {1, 2, 3}
Difference (B-A): {6, 7, 8}
Symmetric Difference: {1, 2, 3, 6, 7, 8}
```

---

## Question 16: Email Domain Extractor
Extract unique email domains from a list of email addresses.

**Sample Input:**
```
emails = ["user1@gmail.com", "user2@yahoo.com", "user3@gmail.com", "user4@outlook.com", "user5@yahoo.com"]
```

**Sample Output:**
```
Unique domains: {'gmail.com', 'yahoo.com', 'outlook.com'}
```

---

## Question 17: Frozenset as Dictionary Key
Create a dictionary where keys are frozensets representing student groups and values are project names.

**Sample Input:**
```
team1 = frozenset({"Alice", "Bob"})
team2 = frozenset({"Charlie", "David"})
team3 = frozenset({"Alice", "Bob"})  # Same as team1
```

**Sample Output:**
```
{frozenset({'Alice', 'Bob'}): 'Project A', frozenset({'Charlie', 'David'}): 'Project B'}
Note: team3 overwrites team1 as they have same members
```

---

## Question 18: Attendance Checker
Find students who were present on all days, some days, or absent on all days.

**Sample Input:**
```
day1 = {"Alice", "Bob", "Charlie", "David"}
day2 = {"Alice", "Bob", "Eve"}
day3 = {"Alice", "Charlie", "Frank"}
```

**Sample Output:**
```
Present all days: {'Alice'}
Present some days: {'Bob', 'Charlie', 'David', 'Eve', 'Frank'}
```

---

## Question 19: Power Set Generator
Generate all possible subsets of a given set (up to size 3 for simplicity).

**Sample Input:**
```
original = {1, 2, 3}
```

**Sample Output:**
```
Power set:
{}
{1}
{2}
{3}
{1, 2}
{1, 3}
{2, 3}
{1, 2, 3}
```

---

## Question 20: Symmetric Updates
Perform symmetric update operations on sets.

**Sample Input:**
```
favorites_old = {"pizza", "pasta", "burger"}
favorites_new = {"pizza", "sushi", "tacos"}
```

**Sample Output:**
```
Old favorites: {'pizza', 'pasta', 'burger'}
New favorites: {'pizza', 'sushi', 'tacos'}
Changed favorites (removed + added): {'pasta', 'burger', 'sushi', 'tacos'}
Unchanged: {'pizza'}
```

