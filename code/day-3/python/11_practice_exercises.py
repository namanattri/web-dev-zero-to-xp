"""
Python Crash Course - Lesson 11: Practice Exercises
====================================================
Put your skills to the test with practical challenges
"""

print("="*60)
print("PYTHON PRACTICE EXERCISES")
print("="*60)
print()

# EXERCISE 1: FizzBuzz
print("=== EXERCISE 1: FizzBuzz ===")
print("Print numbers 1-30, but:")
print("- Print 'Fizz' for multiples of 3")
print("- Print 'Buzz' for multiples of 5")
print("- Print 'FizzBuzz' for multiples of both")
print()

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print("\n")

# EXERCISE 2: Palindrome Checker
print("=== EXERCISE 2: Palindrome Checker ===")

def is_palindrome(text):
    """Check if a string is a palindrome"""
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

test_words = ["racecar", "hello", "A man a plan a canal Panama", "python"]
for word in test_words:
    result = "is" if is_palindrome(word) else "is not"
    print(f"'{word}' {result} a palindrome")
print()

# EXERCISE 3: Find Prime Numbers
print("=== EXERCISE 3: Find Prime Numbers ===")

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [num for num in range(2, 50) if is_prime(num)]
print(f"Prime numbers up to 50: {primes}")
print()

# EXERCISE 4: Reverse Words in a Sentence
print("=== EXERCISE 4: Reverse Words in Sentence ===")

def reverse_words(sentence):
    """Reverse the order of words in a sentence"""
    words = sentence.split()
    return " ".join(reversed(words))

sentence = "Python is awesome"
reversed_sentence = reverse_words(sentence)
print(f"Original: {sentence}")
print(f"Reversed: {reversed_sentence}")
print()

# EXERCISE 5: Count Characters
print("=== EXERCISE 5: Character Counter ===")

def count_characters(text):
    """Count frequency of each character"""
    char_count = {}
    for char in text.lower():
        if char.isalnum():  # Only count letters and numbers
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

text = "Hello World"
char_counts = count_characters(text)
print(f"Text: '{text}'")
print("Character frequencies:")
for char, count in sorted(char_counts.items()):
    print(f"  {char}: {count}")
print()

# EXERCISE 6: Find Duplicates
print("=== EXERCISE 6: Find Duplicates in List ===")

def find_duplicates(lst):
    """Find all duplicate values in a list"""
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)

numbers = [1, 2, 3, 2, 4, 5, 1, 6, 7, 3]
dups = find_duplicates(numbers)
print(f"List: {numbers}")
print(f"Duplicates: {dups}")
print()

# EXERCISE 7: Fibonacci Sequence
print("=== EXERCISE 7: Fibonacci Sequence ===")

def fibonacci(n):
    """Generate first n Fibonacci numbers"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

fib_sequence = fibonacci(10)
print(f"First 10 Fibonacci numbers: {fib_sequence}")
print()

# EXERCISE 8: Anagram Checker
print("=== EXERCISE 8: Anagram Checker ===")

def are_anagrams(str1, str2):
    """Check if two strings are anagrams"""
    # Remove spaces and convert to lowercase
    clean1 = str1.replace(" ", "").lower()
    clean2 = str2.replace(" ", "").lower()
    return sorted(clean1) == sorted(clean2)

pairs = [
    ("listen", "silent"),
    ("hello", "world"),
    ("The eyes", "They see")
]

for word1, word2 in pairs:
    result = "are" if are_anagrams(word1, word2) else "are not"
    print(f"'{word1}' and '{word2}' {result} anagrams")
print()

# EXERCISE 9: List Flattener
print("=== EXERCISE 9: Flatten Nested List ===")

def flatten_list(nested_list):
    """Flatten a nested list"""
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

nested = [1, [2, 3], [4, [5, 6]], 7]
flattened = flatten_list(nested)
print(f"Nested: {nested}")
print(f"Flattened: {flattened}")
print()

# EXERCISE 10: Simple Statistics
print("=== EXERCISE 10: Calculate Statistics ===")

def calculate_stats(numbers):
    """Calculate mean, median, and mode"""
    # Mean
    mean = sum(numbers) / len(numbers)
    
    # Median
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 0:
        median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    else:
        median = sorted_nums[n//2]
    
    # Mode (most frequent)
    from collections import Counter
    count = Counter(numbers)
    mode = count.most_common(1)[0][0]
    
    return {
        "mean": mean,
        "median": median,
        "mode": mode
    }

data = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7]
stats = calculate_stats(data)
print(f"Data: {data}")
print(f"Mean: {stats['mean']:.2f}")
print(f"Median: {stats['median']}")
print(f"Mode: {stats['mode']}")
print()

# CHALLENGE: Password Generator
print("=== BONUS: Password Generator ===")

def generate_password(length=12):
    """Generate a random password"""
    import random
    import string
    
    # Include uppercase, lowercase, digits, and special characters
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Sample passwords:")
for i in range(3):
    print(f"  {i+1}. {generate_password(12)}")

print()
print("="*60)
print("CONGRATULATIONS! You've completed all exercises!")
print("Keep practicing to master Python programming!")
print("="*60)

