# Assignment 10: Input and Output

Complete the following coding challenges to practice user input and formatted output in Python.

---

## Question 1: Interactive Calculator
Create an interactive calculator that keeps running until the user types "quit".

**Sample Interaction:**
```
Enter first number: 10
Enter second number: 5
Enter operation (+, -, *, /): +
Result: 15
Continue? (yes/no): yes
Enter first number: 20
Enter second number: 4
Enter operation (+, -, *, /): *
Result: 80
Continue? (yes/no): no
Thank you for using the calculator!
```

---

## Question 2: Student Registration
Create a program that collects student information and displays it formatted.

**Sample Input:**
```
Name: Alice Johnson
Age: 20
Grade: 85.5
```

**Sample Output:**
```
========== STUDENT REGISTRATION ==========
Name:     Alice Johnson
Age:      20 years
Grade:    85.50
Status:   Passed
==========================================
```

---

## Question 3: Mad Libs Generator
Create a mad libs program that asks for different types of words.

**Sample Input:**
```
Adjective: funny
Noun: elephant
Verb: dances
```

**Sample Output:**
```
The funny elephant dances in the park!
```

---

## Question 4: Number Guessing Game
Create an interactive number guessing game with hints.

**Sample Interaction:**
```
Guess a number between 1 and 100: 50
Too low! Try again.
Guess a number between 1 and 100: 75
Too high! Try again.
Guess a number between 1 and 100: 63
Congratulations! You found it in 3 attempts!
```

---

## Question 5: Shopping List Manager
Create an interactive shopping list program with add, remove, and display options.

**Sample Interaction:**
```
Menu:
1. Add item
2. Remove item
3. Display list
4. Quit

Choice: 1
Enter item: Milk
Item added!

Choice: 1
Enter item: Bread
Item added!

Choice: 3
Shopping List:
1. Milk
2. Bread

Choice: 4
Goodbye!
```

---

## Question 6: Survey Collector
Collect responses to multiple questions and display a summary.

**Sample Input:**
```
Name: Bob
Favorite color: Blue
Favorite food: Pizza
Hobby: Reading
```

**Sample Output:**
```
====== SURVEY SUMMARY ======
Participant: Bob
Responses:
  - Favorite color: Blue
  - Favorite food: Pizza
  - Hobby: Reading
Thank you for participating!
============================
```

---

## Question 7: Table Generator
Create a formatted table from user input.

**Sample Input:**
```
How many students? 3
Student 1 name: Alice
Student 1 score: 85
Student 2 name: Bob
Student 2 score: 92
Student 3 name: Charlie
Student 3 score: 78
```

**Sample Output:**
```
Name       | Score | Grade
-----------|-------|------
Alice      |  85   |   B
Bob        |  92   |   A
Charlie    |  78   |   C
```

---

## Question 8: Password Creator
Create a program that helps users create secure passwords with validation.

**Sample Interaction:**
```
Enter desired password length (8-20): 12
Include numbers? (y/n): y
Include special characters? (y/n): y

Generated password: aB3$xY9!mKp2
Is this acceptable? (y/n): y
Password saved successfully!
```

---

## Question 9: Countdown Timer
Create an interactive countdown timer.

**Sample Input:**
```
Enter seconds: 5
```

**Sample Output:**
```
5...
4...
3...
2...
1...
Time's up!
```

---

## Question 10: Unit Converter
Create an interactive unit converter for different measurements.

**Sample Interaction:**
```
Conversion options:
1. Miles to Kilometers
2. Pounds to Kilograms
3. Fahrenheit to Celsius

Choose conversion: 1
Enter miles: 10
10 miles = 16.09 kilometers
```

---

## Question 11: Receipt Generator
Generate a formatted receipt for purchases.

**Sample Input:**
```
Item 1: Coffee - $3.50
Item 2: Sandwich - $7.25
Item 3: Cookie - $2.00
```

**Sample Output:**
```
========== RECEIPT ==========
Coffee           $3.50
Sandwich         $7.25
Cookie           $2.00
----------------------------
Subtotal        $12.75
Tax (8%)         $1.02
----------------------------
Total           $13.77
============================
```

---

## Question 12: Todo List with Priority
Create a todo list where users can add tasks with priority levels.

**Sample Interaction:**
```
1. Add task
2. View tasks
3. Exit

Choice: 1
Enter task: Complete homework
Priority (High/Medium/Low): High
Task added!

Choice: 2
TODO LIST:
[HIGH] Complete homework
```

---

## Question 13: BMI Calculator (Interactive)
Create an interactive BMI calculator with health recommendations.

**Sample Input:**
```
Enter weight (kg): 70
Enter height (m): 1.75
```

**Sample Output:**
```
===== BMI CALCULATOR =====
Weight: 70.0 kg
Height: 1.75 m
BMI: 22.86
Category: Normal weight
Recommendation: Maintain your healthy lifestyle!
==========================
```

---

## Question 14: Quiz Program
Create an interactive quiz with multiple questions and scoring.

**Sample Interaction:**
```
Question 1: What is 2 + 2?
Answer: 4
Correct!

Question 2: What is the capital of France?
Answer: Paris
Correct!

Question 3: What is 5 * 6?
Answer: 25
Incorrect! The correct answer is 30.

Quiz complete!
Score: 2/3 (66.67%)
```

---

## Question 15: Contact Information Formatter
Collect and format contact information.

**Sample Input:**
```
First Name: John
Last Name: Doe
Phone: 5551234
Email: john@example.com
```

**Sample Output:**
```
╔══════════════════════════╗
║     CONTACT CARD         ║
╠══════════════════════════╣
║ Name:  John Doe          ║
║ Phone: (555) 123-4567    ║
║ Email: john@example.com  ║
╚══════════════════════════╝
```

---

## Question 16: Progress Bar
Create a text-based progress bar for a task.

**Sample Output:**
```
Processing...
[##########          ] 50%
[####################] 100%
Complete!
```

---

## Question 17: Menu-Driven Program
Create a menu-driven restaurant ordering system.

**Sample Interaction:**
```
=== MENU ===
1. Burger - $8.99
2. Pizza - $12.99
3. Salad - $6.99
4. Checkout

Your choice: 1
Added Burger to cart.

Your choice: 2
Added Pizza to cart.

Your choice: 4

Your Order:
- Burger: $8.99
- Pizza: $12.99
Total: $21.98
```

---

## Question 18: Interactive Story
Create an interactive story with user choices.

**Sample Interaction:**
```
You find yourself in a dark forest.
Do you go left or right? left

You encounter a friendly wolf.
Do you pet it or run? pet

The wolf leads you to treasure!
THE END
```

---

## Question 19: Data Entry Validation
Create a program that validates user input with retry logic.

**Sample Interaction:**
```
Enter age (1-120): 150
Invalid! Age must be between 1 and 120.
Enter age (1-120): 25
Valid!

Enter email: invalid
Invalid email format!
Enter email: user@example.com
Valid!
```

---

## Question 20: Formatted Report
Generate a formatted report from user data.

**Sample Input:**
```
Company: Tech Corp
Quarter: Q1 2024
Revenue: 1000000
Expenses: 650000
```

**Sample Output:**
```
╔═══════════════════════════════╗
║     QUARTERLY REPORT          ║
╠═══════════════════════════════╣
║ Company:  Tech Corp           ║
║ Period:   Q1 2024             ║
║                               ║
║ Revenue:   $1,000,000.00      ║
║ Expenses:  $  650,000.00      ║
║ ───────────────────────────   ║
║ Profit:    $  350,000.00      ║
║ Margin:    35.00%             ║
╚═══════════════════════════════╝
```

