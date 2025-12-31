# Assignment 9: String Manipulation

Complete the following coding challenges to practice working with strings in JavaScript/TypeScript.

---

## Question 1: Reverse Words
Reverse the order of words in a sentence (not the characters).

**Sample Input:**
```
sentence = "Python is awesome"
```

**Sample Output:**
```
Original: Python is awesome
Reversed: awesome is Python
```

---

## Question 2: Count Vowels and Consonants
Count the number of vowels and consonants in a string.

**Sample Input:**
```
text = "Hello World"
```

**Sample Output:**
```
Vowels: 3
Consonants: 7
```

---

## Question 3: Title Case Converter
Convert a string to title case, but keep articles lowercase (a, an, the, etc.).

**Sample Input:**
```
text = "the lord of the rings"
```

**Sample Output:**
```
The Lord of the Rings
```

---

## Question 4: Remove Special Characters
Remove all special characters from a string, keeping only letters, numbers, and spaces using regex.

**Sample Input:**
```typescript
const text: string = "Hello, World! #TypeScript2024";
```

**Sample Output:**
```
Original: Hello, World! #TypeScript2024
Cleaned: Hello World TypeScript2024
```

---

## Question 5: Check Anagram
Check if two strings are anagrams of each other.

**Sample Input:**
```
str1 = "listen"
str2 = "silent"
```

**Sample Output:**
```
'listen' and 'silent' are anagrams: True
```

---

## Question 6: String Compression
Compress a string by replacing consecutive repeated characters with character + count.

**Sample Input:**
```
text = "aaabbbbccaa"
```

**Sample Output:**
```
Original: aaabbbbccaa
Compressed: a3b4c2a2
```

---

## Question 7: Find First Non-Repeating Character
Find the first character in a string that doesn't repeat.

**Sample Input:**
```
text = "aabccdeeff"
```

**Sample Output:**
```
First non-repeating character: b
```

---

## Question 8: String Rotation Check
Check if one string is a rotation of another.

**Sample Input:**
```
str1 = "waterbottle"
str2 = "erbottlewat"
```

**Sample Output:**
```
'erbottlewat' is a rotation of 'waterbottle': True
```

---

## Question 9: CamelCase to Snake_Case
Convert a camelCase string to snake_case.

**Sample Input:**
```
camel = "helloWorldPython"
```

**Sample Output:**
```
Camel case: helloWorldPython
Snake case: hello_world_python
```

---

## Question 10: Count Word Occurrences
Count how many times each word appears in a sentence (case-insensitive).

**Sample Input:**
```
sentence = "The quick brown fox jumps over the lazy dog the fox"
```

**Sample Output:**
```
the: 3
quick: 1
brown: 1
fox: 2
jumps: 1
over: 1
lazy: 1
dog: 1
```

---

## Question 11: Extract Numbers from String
Extract all numbers from a string.

**Sample Input:**
```
text = "I have 3 apples and 5 oranges, total 8 fruits"
```

**Sample Output:**
```
Numbers found: [3, 5, 8]
Sum of numbers: 16
```

---

## Question 12: String Padding
Add padding to a string to make it a specific length (center, left, right align).

**Sample Input:**
```
text = "Python"
width = 15
```

**Sample Output:**
```
Left:   'Python         '
Center: '    Python     '
Right:  '         Python'
```

---

## Question 13: Remove Duplicate Characters
Remove duplicate characters from a string while preserving order.

**Sample Input:**
```
text = "programming"
```

**Sample Output:**
```
Original: programming
Without duplicates: progamin
```

---

## Question 14: Longest Word Finder
Find the longest word in a sentence.

**Sample Input:**
```
sentence = "The quick brown fox jumps over the lazy dog"
```

**Sample Output:**
```
Longest word: 'jumps' (length: 5)
```

---

## Question 15: String Substitution
Replace multiple substrings in a string.

**Sample Input:**
```
text = "I love Java and Java is powerful"
replacements = {"Java": "Python", "powerful": "awesome"}
```

**Sample Output:**
```
Original: I love Java and Java is powerful
Modified: I love Python and Python is awesome
```

---

## Question 16: Check Pangram
Check if a sentence contains all letters of the alphabet.

**Sample Input:**
```
sentence = "The quick brown fox jumps over the lazy dog"
```

**Sample Output:**
```
Is pangram: True
```

---

## Question 17: String Interleaving
Interleave two strings character by character.

**Sample Input:**
```
str1 = "abc"
str2 = "12345"
```

**Sample Output:**
```
Interleaved: a1b2c345
```

---

## Question 18: Extract Email Components
Extract username and domain from email addresses using string methods or regex.

**Sample Input:**
```typescript
const email: string = "user.name@example.com";
```

**Sample Output:**
```
Username: user.name
Domain: example.com
Extension: com
```

---

## Question 19: Palindrome Substrings
Find all palindromic substrings of length 3 or more.

**Sample Input:**
```
text = "racecar"
```

**Sample Output:**
```
Palindromic substrings: ['aca', 'cec', 'aceca', 'racecar']
```

---

## Question 20: Text Justification
Justify text to a given width by adjusting spaces between words.

**Sample Input:**
```
words = ["This", "is", "an", "example"]
width = 16
```

**Sample Output:**
```
'This    is    an'
'example         '
```

