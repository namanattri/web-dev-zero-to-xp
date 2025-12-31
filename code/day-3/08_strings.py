"""
Python Crash Course - Lesson 8: String Manipulation
====================================================
Learn to work with text data effectively
"""

# BASIC STRING OPERATIONS
print("=== BASIC STRING OPERATIONS ===")
text = "Hello, Python!"
print(f"String: {text}")
print(f"Length: {len(text)}")
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print()

# STRING METHODS - CASE CONVERSION
print("=== CASE CONVERSION ===")
message = "Hello World"
print(f"Original: {message}")
print(f"Uppercase: {message.upper()}")
print(f"Lowercase: {message.lower()}")
print(f"Title case: {message.title()}")
print(f"Swap case: {message.swapcase()}")
print(f"Capitalize: {message.capitalize()}")
print()

# STRING METHODS - CHECKING
print("=== STRING CHECKING ===")
text1 = "Hello123"
text2 = "12345"
text3 = "hello"

print(f"'{text1}' is alphanumeric: {text1.isalnum()}")
print(f"'{text2}' is digit: {text2.isdigit()}")
print(f"'{text3}' is alpha: {text3.isalpha()}")
print(f"'{text3}' is lowercase: {text3.islower()}")
print(f"'HELLO' is uppercase: {'HELLO'.isupper()}")
print()

# STRING SLICING
print("=== STRING SLICING ===")
text = "Python Programming"
print(f"Full string: {text}")
print(f"First 6 characters: {text[0:6]}")
print(f"From index 7 onwards: {text[7:]}")
print(f"Last 11 characters: {text[-11:]}")
print(f"Every 2nd character: {text[::2]}")
print(f"Reversed: {text[::-1]}")
print()

# STRING CONCATENATION
print("=== STRING CONCATENATION ===")
first_name = "John"
last_name = "Doe"

# Method 1: Using +
full_name = first_name + " " + last_name
print(f"Using +: {full_name}")

# Method 2: Using join
full_name = " ".join([first_name, last_name])
print(f"Using join: {full_name}")

# Method 3: Using f-strings (recommended)
full_name = f"{first_name} {last_name}"
print(f"Using f-string: {full_name}")
print()

# STRING FORMATTING
print("=== STRING FORMATTING ===")
name = "Alice"
age = 25
price = 19.99

# f-strings (Python 3.6+)
message = f"My name is {name} and I am {age} years old"
print(message)

# Format with decimal places
print(f"Price: ${price:.2f}")

# Format with padding
print(f"Number: {42:5d}")  # Right-aligned in 5 spaces
print(f"Text: {'Hello':>10}")  # Right-aligned
print(f"Text: {'Hello':<10}")  # Left-aligned
print(f"Text: {'Hello':^10}")  # Center-aligned
print()

# SPLITTING AND JOINING
print("=== SPLITTING AND JOINING ===")
sentence = "Python is awesome and fun"
words = sentence.split()  # Split by whitespace
print(f"Original: {sentence}")
print(f"Split into words: {words}")

csv_data = "apple,banana,orange"
fruits = csv_data.split(",")  # Split by comma
print(f"CSV: {csv_data}")
print(f"Split by comma: {fruits}")

# Join list into string
new_sentence = " ".join(words)
print(f"Joined back: {new_sentence}")
print()

# REMOVING WHITESPACE
print("=== REMOVING WHITESPACE ===")
text = "   Hello, World!   "
print(f"Original: '{text}'")
print(f"strip(): '{text.strip()}'")  # Remove from both ends
print(f"lstrip(): '{text.lstrip()}'")  # Remove from left
print(f"rstrip(): '{text.rstrip()}'")  # Remove from right
print()

# REPLACING
print("=== REPLACING ===")
text = "I love Java programming"
print(f"Original: {text}")
new_text = text.replace("Java", "Python")
print(f"After replace: {new_text}")

# Replace multiple occurrences
text = "one one one"
print(f"Original: {text}")
print(f"Replace first 2: {text.replace('one', 'two', 2)}")
print()

# FINDING SUBSTRINGS
print("=== FINDING SUBSTRINGS ===")
text = "Python is great. Python is powerful."
print(f"Text: {text}")
print(f"Index of 'is': {text.find('is')}")
print(f"Index of 'Python' (from start): {text.index('Python')}")
print(f"Count of 'Python': {text.count('Python')}")
print(f"Starts with 'Python': {text.startswith('Python')}")
print(f"Ends with 'powerful.': {text.endswith('powerful.')}")
print()

# MULTI-LINE STRINGS
print("=== MULTI-LINE STRINGS ===")
poem = """
Roses are red,
Violets are blue,
Python is awesome,
And so are you!
"""
print(poem)

# STRING ESCAPING
print("=== STRING ESCAPING ===")
print("Line 1\nLine 2")  # Newline
print("Tab\tSeparated")  # Tab
print("Quote: \"Hello\"")  # Escape quotes
print("Backslash: \\")  # Escape backslash
print()

# PRACTICAL EXAMPLES
print("=== PRACTICAL EXAMPLES ===")

# Example 1: Email validator (basic)
def is_valid_email(email):
    """Basic email validation"""
    return "@" in email and "." in email

print(f"Is 'test@example.com' valid? {is_valid_email('test@example.com')}")
print(f"Is 'invalid.email' valid? {is_valid_email('invalid.email')}")
print()

# Example 2: Password strength checker
def check_password_strength(password):
    """Check if password meets basic criteria"""
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    is_long = len(password) >= 8
    
    if has_upper and has_lower and has_digit and is_long:
        return "Strong"
    elif is_long:
        return "Medium"
    else:
        return "Weak"

print(f"Password 'abc123': {check_password_strength('abc123')}")
print(f"Password 'Abc12345': {check_password_strength('Abc12345')}")
print()

# Example 3: Title case converter
def to_title_case(text):
    """Convert to title case, ignoring small words"""
    small_words = ["a", "an", "the", "in", "on", "at"]
    words = text.split()
    result = []
    for i, word in enumerate(words):
        if i == 0 or word.lower() not in small_words:
            result.append(word.capitalize())
        else:
            result.append(word.lower())
    return " ".join(result)

title = "the lord of the rings"
print(f"Original: {title}")
print(f"Title case: {to_title_case(title)}")
print()

# Example 4: Remove special characters
def remove_special_chars(text):
    """Keep only letters, numbers, and spaces"""
    return ''.join(c for c in text if c.isalnum() or c.isspace())

text_with_special = "Hello, World! #Python2024"
clean_text = remove_special_chars(text_with_special)
print(f"Original: {text_with_special}")
print(f"Cleaned: {clean_text}")
print()

# Example 5: Count vowels
def count_vowels(text):
    """Count vowels in a string"""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

sentence = "Python Programming"
print(f"Sentence: {sentence}")
print(f"Vowel count: {count_vowels(sentence)}")

