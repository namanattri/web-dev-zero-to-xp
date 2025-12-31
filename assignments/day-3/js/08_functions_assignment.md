# Assignment 8: Functions

Complete the following coding challenges to practice creating and using functions in JavaScript/TypeScript.

---

## Question 1: Area Calculator Functions
Create functions to calculate the area of different shapes (circle, rectangle, triangle).

**Sample Input:**
```
circle_area(5)
rectangle_area(10, 5)
triangle_area(6, 8)
```

**Sample Output:**
```
Circle area: 78.54
Rectangle area: 50
Triangle area: 24.0
```

---

## Question 2: Temperature Converter
Create functions to convert between Celsius, Fahrenheit, and Kelvin.

**Sample Input:**
```
celsius_to_fahrenheit(25)
fahrenheit_to_celsius(77)
celsius_to_kelvin(25)
```

**Sample Output:**
```
25°C = 77.0°F
77°F = 25.0°C
25°C = 298.15K
```

---

## Question 3: Palindrome Checker
Write a function that checks if a string is a palindrome (case-insensitive).

**Sample Input:**
```
is_palindrome("racecar")
is_palindrome("hello")
is_palindrome("A man a plan a canal Panama")
```

**Sample Output:**
```
'racecar' is a palindrome: True
'hello' is a palindrome: False
'A man a plan a canal Panama' is a palindrome: True
```

---

## Question 4: List Statistics Function
Create a function that returns multiple statistics (min, max, mean, median) for a list.

**Sample Input:**
```
get_statistics([1, 3, 5, 7, 9, 11])
```

**Sample Output:**
```
{
    'min': 1,
    'max': 11,
    'mean': 6.0,
    'median': 6.0,
    'count': 6
}
```

---

## Question 5: Default Parameters
Create a function to greet a person with optional title and punctuation.

**Sample Input:**
```
greet("Alice")
greet("Smith", title="Dr.")
greet("Johnson", title="Prof.", punctuation="!")
```

**Sample Output:**
```
Hello, Alice.
Hello, Dr. Smith.
Hello, Prof. Johnson!
```

---

## Question 6: Rest Parameters (...args)
Create a function that calculates the average of any number of arguments using rest parameters.

**Sample Input:**
```typescript
average(10, 20, 30)
average(5, 10, 15, 20, 25)
average(100)
```

**Sample Output:**
```
Average of (10, 20, 30): 20.0
Average of (5, 10, 15, 20, 25): 15.0
Average of (100): 100.0
```

---

## Question 7: Keyword Arguments (**kwargs)
Create a function that builds a profile dictionary from keyword arguments.

**Sample Input:**
```
create_profile(name="Alice", age=25, city="NYC")
create_profile(name="Bob", occupation="Engineer", country="USA")
```

**Sample Output:**
```
{'name': 'Alice', 'age': 25, 'city': 'NYC'}
{'name': 'Bob', 'occupation': 'Engineer', 'country': 'USA'}
```

---

## Question 8: Recursive Factorial
Write a recursive function to calculate factorial.

**Sample Input:**
```
factorial(5)
factorial(0)
factorial(7)
```

**Sample Output:**
```
Factorial of 5: 120
Factorial of 0: 1
Factorial of 7: 5040
```

---

## Question 9: Fibonacci with Recursion
Create a recursive function to find the nth Fibonacci number.

**Sample Input:**
```
fibonacci(0)
fibonacci(1)
fibonacci(10)
```

**Sample Output:**
```
Fibonacci(0): 0
Fibonacci(1): 1
Fibonacci(10): 55
```

---

## Question 10: Prime Number Generator
Write a function that returns all prime numbers up to N.

**Sample Input:**
```
get_primes(20)
```

**Sample Output:**
```
Primes up to 20: [2, 3, 5, 7, 11, 13, 17, 19]
```

---

## Question 11: String Formatter Function
Create a function that formats a name (first, last) in different styles.

**Sample Input:**
```
format_name("john", "doe", style="title")
format_name("john", "doe", style="upper")
format_name("john", "doe", style="initials")
```

**Sample Output:**
```
John Doe
JOHN DOE
J.D.
```

---

## Question 12: List Filter Function
Write a function that filters a list based on a condition (e.g., even numbers, positive numbers).

**Sample Input:**
```
filter_list([1, -2, 3, -4, 5, 6], condition="positive")
filter_list([1, 2, 3, 4, 5, 6], condition="even")
```

**Sample Output:**
```
Positive numbers: [1, 3, 5, 6]
Even numbers: [2, 4, 6]
```

---

## Question 13: Calculator with Functions
Create separate functions for basic operations and a main calculator function.

**Sample Input:**
```
calculator(10, 5, "add")
calculator(10, 5, "multiply")
calculator(10, 0, "divide")
```

**Sample Output:**
```
10 + 5 = 15
10 * 5 = 50
Error: Cannot divide by zero
```

---

## Question 14: Nested Functions
Create a function with an inner helper function to calculate powers.

**Sample Input:**
```
power_calculator(2, 3)
power_calculator(5, 2)
```

**Sample Output:**
```
2^3 = 8
5^2 = 25
```

---

## Question 15: Function Returning Function
Write a function that returns another function (closure).

**Sample Input:**
```
make_multiplier(3)
multiply_by_3 = make_multiplier(3)
multiply_by_3(10)
```

**Sample Output:**
```
Multiplying 10 by 3: 30
```

---

## Question 16: Validation Function
Create a function to validate email addresses (basic validation).

**Sample Input:**
```
validate_email("user@example.com")
validate_email("invalid.email")
validate_email("test@domain")
```

**Sample Output:**
```
user@example.com: Valid
invalid.email: Invalid (no @ symbol)
test@domain: Invalid (no domain extension)
```

---

## Question 17: List Transformation
Write a function that applies transformations to list elements.

**Sample Input:**
```
transform_list([1, 2, 3, 4, 5], operation="square")
transform_list([1, 2, 3, 4, 5], operation="double")
```

**Sample Output:**
```
Squared: [1, 4, 9, 16, 25]
Doubled: [2, 4, 6, 8, 10]
```

---

## Question 18: Argument Unpacking
Create a function that accepts coordinates and calculates distance from origin.

**Sample Input:**
```
point = (3, 4)
distance_from_origin(*point)
```

**Sample Output:**
```
Distance of point (3, 4) from origin: 5.0
```

---

## Question 19: Function with Multiple Returns
Write a function that returns both quotient and remainder.

**Sample Input:**
```
divide_with_remainder(17, 5)
q, r = divide_with_remainder(20, 3)
```

**Sample Output:**
```
Quotient: 3, Remainder: 2
20 ÷ 3 = 6 remainder 2
```

---

## Question 20: Function Documentation with JSDoc
Create well-documented functions using JSDoc comments.

**Sample Input:**
```typescript
/**
 * Calculate Body Mass Index
 * @param weight - Weight in kilograms
 * @param height - Height in meters
 * @returns BMI value as number
 */
function calculateBMI(weight: number, height: number): number {
    return weight / (height ** 2);
}
```

**Sample Output:**
```
BMI for 70kg, 1.75m: 22.86
// Hover over function in VS Code to see documentation
```

