# Assignment 5: Lists

Complete the following coding challenges to practice working with lists and multi-dimensional arrays.

---

## Question 1: List Statistics
Given a list of numbers, find the sum, average, maximum, and minimum.

**Sample Input:**
```
numbers = [12, 45, 23, 67, 34, 89, 15]
```

**Sample Output:**
```
Sum: 285
Average: 40.71
Maximum: 89
Minimum: 12
```

---

## Question 2: Remove Element
Remove all occurrences of a specific element from a list.

**Sample Input:**
```
items = [1, 2, 3, 2, 4, 2, 5]
remove_value = 2
```

**Sample Output:**
```
Original list: [1, 2, 3, 2, 4, 2, 5]
After removing 2: [1, 3, 4, 5]
```

---

## Question 3: Reverse a List
Reverse a list without using the built-in reverse() method.

**Sample Input:**
```
numbers = [1, 2, 3, 4, 5]
```

**Sample Output:**
```
Original: [1, 2, 3, 4, 5]
Reversed: [5, 4, 3, 2, 1]
```

---

## Question 4: Find Second Largest
Find the second largest number in a list.

**Sample Input:**
```
numbers = [45, 23, 78, 12, 89, 56]
```

**Sample Output:**
```
Second largest number: 78
```

---

## Question 5: Merge and Sort Lists
Merge two lists and sort the result in ascending order.

**Sample Input:**
```
list1 = [3, 7, 1, 9]
list2 = [2, 8, 4, 6]
```

**Sample Output:**
```
Merged and sorted: [1, 2, 3, 4, 6, 7, 8, 9]
```

---

## Question 6: List Rotation
Rotate a list to the right by N positions.

**Sample Input:**
```
items = [1, 2, 3, 4, 5, 6, 7]
n = 3
```

**Sample Output:**
```
Original: [1, 2, 3, 4, 5, 6, 7]
Rotated by 3: [5, 6, 7, 1, 2, 3, 4]
```

---

## Question 7: Count Occurrences
Count the frequency of each element in a list.

**Sample Input:**
```
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
```

**Sample Output:**
```
apple: 3
banana: 2
orange: 1
```

---

## Question 8: List Intersection
Find common elements between two lists.

**Sample Input:**
```
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
```

**Sample Output:**
```
Common elements: [4, 5]
```

---

## Question 9: Chunk a List
Split a list into chunks of specified size.

**Sample Input:**
```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3
```

**Sample Output:**
```
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

---

## Question 10: List Comprehension - Squares
Create a new list containing squares of even numbers from the original list.

**Sample Input:**
```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**Sample Output:**
```
Squares of even numbers: [4, 16, 36, 64, 100]
```

---

## Question 11: 2D Matrix - Row Sums
Calculate the sum of each row in a 2D matrix.

**Sample Input:**
```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

**Sample Output:**
```
Row 0 sum: 6
Row 1 sum: 15
Row 2 sum: 24
```

---

## Question 12: 2D Matrix - Column Sums
Calculate the sum of each column in a 2D matrix.

**Sample Input:**
```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

**Sample Output:**
```
Column 0 sum: 12
Column 1 sum: 15
Column 2 sum: 18
```

---

## Question 13: Diagonal Sum
Calculate the sum of diagonal elements in a square matrix.

**Sample Input:**
```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

**Sample Output:**
```
Main diagonal sum: 15
Anti-diagonal sum: 15
```

---

## Question 14: Matrix Multiplication Element
Multiply corresponding elements of two matrices (element-wise multiplication).

**Sample Input:**
```
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[2, 3], [4, 5]]
```

**Sample Output:**
```
Result:
[[2, 6], [12, 20]]
```

---

## Question 15: Flatten Nested List
Flatten a nested list (one level deep).

**Sample Input:**
```
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
```

**Sample Output:**
```
Flattened: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## Question 16: Sliding Window Maximum
Find the maximum element in each sliding window of size K.

**Sample Input:**
```
arr = [1, 3, 5, 2, 4, 6, 8, 7]
k = 3
```

**Sample Output:**
```
[5, 5, 5, 6, 8, 8]
```

---

## Question 17: Remove Duplicates (Preserve Order)
Remove duplicates from a list while maintaining the original order.

**Sample Input:**
```
items = [1, 2, 3, 2, 4, 1, 5, 6, 3]
```

**Sample Output:**
```
Without duplicates: [1, 2, 3, 4, 5, 6]
```

---

## Question 18: Pair Sum
Find all pairs in a list that sum to a target value.

**Sample Input:**
```
numbers = [1, 2, 3, 4, 5, 6]
target = 7
```

**Sample Output:**
```
Pairs that sum to 7:
(1, 6)
(2, 5)
(3, 4)
```

---

## Question 19: Create Identity Matrix
Create an N x N identity matrix (1s on diagonal, 0s elsewhere).

**Sample Input:**
```
n = 4
```

**Sample Output:**
```
[1, 0, 0, 0]
[0, 1, 0, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]
```

---

## Question 20: Zig-Zag Pattern
Convert a 1D list into a 2D zig-zag pattern.

**Sample Input:**
```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
rows = 3
```

**Sample Output:**
```
[1, 2, 3, 4]
[8, 7, 6, 5]
[9, 10, 11, 12]
```

