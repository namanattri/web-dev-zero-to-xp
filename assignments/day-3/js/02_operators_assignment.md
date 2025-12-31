# Assignment 2: Operators

Complete the following coding challenges to practice working with different types of operators in Python.

---

## Question 1: Basic Calculator
Write a program that takes two numbers and performs all arithmetic operations (+, -, *, /, //, %, **) on them. Print each result.

**Sample Input:**
```
a = 17
b = 5
```

**Sample Output:**
```
17 + 5 = 22
17 - 5 = 12
17 * 5 = 85
17 / 5 = 3.4
17 // 5 = 3
17 % 5 = 2
17 ** 5 = 1419857
```

---

## Question 2: Even or Odd Checker
Write a program that checks if a number is even or odd using the modulus operator.

**Sample Input:**
```
number = 23
```

**Sample Output:**
```
23 is odd
```

---

## Question 3: Comparison Chain
Create a program that compares three numbers and determines which is the largest using comparison operators.

**Sample Input:**
```
a = 15
b = 23
c = 19
```

**Sample Output:**
```
The largest number is: 23
```

---

## Question 4: Eligibility Checker
Check if a person is eligible to vote. They must be 18 or older AND have citizenship. Use logical operators.

**Sample Input:**
```
age = 20
is_citizen = True
```

**Sample Output:**
```
Eligible to vote: True
```

---

## Question 5: Discount Calculator
Calculate a discount on a product. If the price is above $100, apply a 20% discount. Use comparison and arithmetic operators.

**Sample Input:**
```
price = 150
```

**Sample Output:**
```
Original price: $150
Discount: $30.0
Final price: $120.0
```

---

## Question 6: Triangle Validator
Check if three sides can form a valid triangle. (Sum of any two sides must be greater than the third side)

**Sample Input:**
```
a = 3
b = 4
c = 5
```

**Sample Output:**
```
Can form a triangle: True
```

---

## Question 7: Leap Year Checker
Determine if a year is a leap year using logical and comparison operators.
Rules: Divisible by 4 AND (not divisible by 100 OR divisible by 400)

**Sample Input:**
```
year = 2024
```

**Sample Output:**
```
2024 is a leap year: True
```

---

## Question 8: Grade Boundary Checker
Check if a score falls within grade boundaries using comparison operators.

**Sample Input:**
```
score = 85
```

**Sample Output:**
```
Score 85 is between 80 and 90: True
Grade: B
```

---

## Question 9: Compound Assignment
Start with a number and use all compound assignment operators (+=, -=, *=, /=, //=, %=, **=) one by one. Print after each operation.

**Sample Input:**
```
num = 100
```

**Sample Output:**
```
Initial: 100
After += 50: 150
After -= 30: 120
After *= 2: 240
After /= 4: 60.0
After //= 7: 8.0
After %= 3: 2.0
After **= 3: 8.0
```

---

## Question 10: Range Checker
Check if a number is within a specific range (inclusive) using logical operators.

**Sample Input:**
```
number = 45
min_val = 1
max_val = 100
```

**Sample Output:**
```
45 is within range [1, 100]: True
```

---

## Question 11: BMI Calculator
Calculate BMI (Body Mass Index) using the formula: BMI = weight / (height²)
Classify the BMI: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (≥30)

**Sample Input:**
```
weight = 70  # kg
height = 1.75  # meters
```

**Sample Output:**
```
BMI: 22.86
Classification: Normal weight
```

---

## Question 12: Divisibility Test
Check if a number is divisible by both 3 and 5 using logical operators.

**Sample Input:**
```
number = 15
```

**Sample Output:**
```
15 is divisible by 3: True
15 is divisible by 5: True
15 is divisible by both 3 and 5: True
```

---

## Question 13: Password Strength
Check password strength based on length (at least 8 characters) and if it contains a number. Use logical operators.

**Sample Input:**
```
password = "secure123"
has_number = True
length = 9
```

**Sample Output:**
```
Password strength: Strong (length >= 8 AND contains number)
```

---

## Question 14: Temperature Range
Check if temperature is comfortable (between 20°C and 25°C inclusive).

**Sample Input:**
```
temperature = 22
```

**Sample Output:**
```
Temperature 22°C is comfortable: True
```

---

## Question 15: Quadratic Discriminant
Calculate the discriminant of a quadratic equation (b² - 4ac) and determine the nature of roots.
- Discriminant > 0: Two real roots
- Discriminant = 0: One real root
- Discriminant < 0: No real roots

**Sample Input:**
```
a = 1
b = -3
c = 2
```

**Sample Output:**
```
Discriminant: 1
Nature of roots: Two real and distinct roots
```

---

## Question 16: Shopping Cart Total
Calculate total with discount and tax. If total > $100, apply 10% discount. Then add 8% tax.

**Sample Input:**
```
price1 = 45
price2 = 60
price3 = 30
```

**Sample Output:**
```
Subtotal: $135.00
After discount: $121.50
After tax: $131.22
Final total: $131.22
```

---

## Question 17: Number Sign Checker
Determine if a number is positive, negative, or zero using comparison operators.

**Sample Input:**
```
num = -15
```

**Sample Output:**
```
-15 is negative
```

---

## Question 18: Logical Operators Practice
Given three boolean variables, evaluate complex logical expressions.

**Sample Input:**
```
a = True
b = False
c = True
```

**Sample Output:**
```
a and b: False
a or b: True
not a: False
a and (b or c): True
(a or b) and not c: False
```

---

## Question 19: Time Converter
Convert minutes to hours and minutes using floor division and modulus.

**Sample Input:**
```
total_minutes = 135
```

**Sample Output:**
```
135 minutes = 2 hours and 15 minutes
```

---

## Question 20: Comparison Results
Compare two numbers and print all comparison results.

**Sample Input:**
```
x = 10
y = 20
```

**Sample Output:**
```
x == y: False
x != y: True
x > y: False
x < y: True
x >= y: False
x <= y: True
```

