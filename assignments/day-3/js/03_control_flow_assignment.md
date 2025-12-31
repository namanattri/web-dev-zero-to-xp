# Assignment 3: Control Flow (if/else if/else)

Complete the following coding challenges to practice decision-making with control flow statements in JavaScript/TypeScript.

---

## Question 1: Age Category
Write a program that categorizes a person's age into: Child (0-12), Teen (13-19), Adult (20-59), Senior (60+).

**Sample Input:**
```
age = 25
```

**Sample Output:**
```
Age category: Adult
```

---

## Question 2: Grade Calculator
Convert a numerical score to a letter grade:
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: Below 60

**Sample Input:**
```
score = 87
```

**Sample Output:**
```
Score: 87
Grade: B
```

---

## Question 3: Login System
Create a simple login system that checks username and password. Print appropriate messages for success or different failure reasons.

**Sample Input:**
```typescript
const username: string = "admin";
const password: string = "12345";
const correctUser: string = "admin";
const correctPass: string = "admin123";
```

**Sample Output:**
```
Incorrect password
```

---

## Question 4: Traffic Light
Write a program that tells you what to do based on a traffic light color (Red: Stop, Yellow: Slow down, Green: Go).

**Sample Input:**
```
light = "Yellow"
```

**Sample Output:**
```
Traffic light is Yellow: Slow down
```

---

## Question 5: Ticket Pricing
Calculate movie ticket price based on age:
- Under 3: Free
- 3-12: $10
- 13-64: $20
- 65+: $15

**Sample Input:**
```
age = 8
```

**Sample Output:**
```
Ticket price for age 8: $10
```

---

## Question 6: Triangle Type Classifier
Given three sides of a triangle, classify it as Equilateral (all sides equal), Isosceles (two sides equal), or Scalene (all sides different).

**Sample Input:**
```
side1 = 5
side2 = 5
side3 = 7
```

**Sample Output:**
```
Triangle type: Isosceles
```

---

## Question 7: Number Comparison
Compare two numbers and print which is larger, or if they're equal.

**Sample Input:**
```
num1 = 45
num2 = 38
```

**Sample Output:**
```
45 is greater than 38
```

---

## Question 8: Shipping Cost Calculator
Calculate shipping cost based on order total:
- $0-$50: $10 shipping
- $50-$100: $5 shipping
- Over $100: Free shipping

**Sample Input:**
```
order_total = 75
```

**Sample Output:**
```
Order total: $75
Shipping cost: $5
Final total: $80
```

---

## Question 9: Largest of Three Numbers
Find and print the largest of three given numbers.

**Sample Input:**
```
a = 23
b = 45
c = 17
```

**Sample Output:**
```
The largest number is: 45
```

---

## Question 10: Season Identifier
Identify the season based on month number (12, 1, 2: Winter; 3, 4, 5: Spring; 6, 7, 8: Summer; 9, 10, 11: Fall).

**Sample Input:**
```
month = 7
```

**Sample Output:**
```
Month 7 is in Summer
```

---

## Question 11: Nested Decision - College Admission
Check college admission eligibility:
- Must have GPA >= 3.0
- If GPA >= 3.5, check if SAT >= 1200 (Accepted)
- If GPA 3.0-3.5, check if SAT >= 1300 (Accepted)
- Otherwise: Not accepted

**Sample Input:**
```
gpa = 3.6
sat = 1250
```

**Sample Output:**
```
Admission decision: Accepted
```

---

## Question 12: Discount Eligibility
Apply discount based on multiple conditions:
- Senior citizen (65+) OR student: 15% discount
- Regular customer with loyalty card: 10% discount
- New customer: No discount

**Sample Input:**
```
age = 70
is_student = False
has_loyalty_card = True
```

**Sample Output:**
```
Discount applied: 15% (Senior citizen)
```

---

## Question 13: BMI Category
Calculate BMI and categorize: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (30+).

**Sample Input:**
```
weight = 70  # kg
height = 1.75  # meters
```

**Sample Output:**
```
BMI: 22.86
Category: Normal weight
```

---

## Question 14: Quadrant Finder
Given x and y coordinates, determine which quadrant a point lies in (or if it's on an axis).

**Sample Input:**
```
x = 3
y = -5
```

**Sample Output:**
```
Point (3, -5) is in Quadrant IV
```

---

## Question 15: Password Validator
Check if a password meets requirements:
- At least 8 characters long
- If less than 8: "Too short"
- If 8-12: "Medium strength"
- If 13+: "Strong"

**Sample Input:**
```
password = "mypassword123"
length = 13
```

**Sample Output:**
```
Password strength: Strong
```

---

## Question 16: Tax Calculator
Calculate tax based on income brackets:
- $0-$10,000: 0%
- $10,001-$40,000: 10%
- $40,001-$80,000: 20%
- $80,001+: 30%

**Sample Input:**
```
income = 55000
```

**Sample Output:**
```
Income: $55,000
Tax rate: 20%
Tax amount: $11,000
After-tax income: $44,000
```

---

## Question 17: Vowel or Consonant
Check if a given letter is a vowel or consonant (assume lowercase input).

**Sample Input:**
```
letter = 'e'
```

**Sample Output:**
```
'e' is a vowel
```

---

## Question 18: Number Sign and Magnitude
Check if a number is positive/negative/zero AND small (<10), medium (10-100), or large (>100).

**Sample Input:**
```
num = 75
```

**Sample Output:**
```
75 is positive and medium
```

---

## Question 19: Restaurant Bill Splitter
Calculate individual cost based on number of people and whether to include tip:
- If party size > 5: Add 18% gratuity automatically
- Otherwise: Ask if they want to add 15% tip

**Sample Input:**
```
total_bill = 150
party_size = 6
```

**Sample Output:**
```
Total bill: $150
Party size: 6
Automatic gratuity (18%): $27.00
Total with tip: $177.00
Per person: $29.50
```

---

## Question 20: Ternary Operator Practice
Use ternary operator to assign values based on conditions. Check if a student passed (score >= 60) and assign "Pass" or "Fail".

**Sample Input:**
```typescript
const score: number = 72;
const result: string = score >= 60 ? "Pass" : "Fail";
```

**Sample Output:**
```
Result: Pass
```

