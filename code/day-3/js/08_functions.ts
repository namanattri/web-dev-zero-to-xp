/**
 * TypeScript Crash Course - Lesson 8: Functions
 * ===============================================
 * Learn to create reusable blocks of code
 */

// BASIC FUNCTION
console.log("=== BASIC FUNCTION ===");
function greet(): void {
    console.log("Hello, World!");
}
greet();
console.log();

// FUNCTION WITH PARAMETERS
console.log("=== FUNCTION WITH PARAMETERS ===");
function greetPerson(name: string): void {
    console.log(`Hello, ${name}!`);
}
greetPerson("Alice");
console.log();

// FUNCTION WITH RETURN VALUE
console.log("=== RETURN VALUES ===");
function multiply(a: number, b: number): number {
    return a * b;
}
const result: number = multiply(4, 5);
console.log(`4 x 5 = ${result}`);
console.log();

// DEFAULT PARAMETERS
console.log("=== DEFAULT PARAMETERS ===");
function greetWithTitle(name: string, title: string = "Mr."): void {
    console.log(`Hello, ${title} ${name}!`);
}
greetWithTitle("Smith");
greetWithTitle("Johnson", "Dr.");
console.log();

// OPTIONAL PARAMETERS
console.log("=== OPTIONAL PARAMETERS ===");
function buildName(firstName: string, lastName?: string): string {
    return lastName ? `${firstName} ${lastName}` : firstName;
}
console.log(buildName("John"));
console.log(buildName("John", "Doe"));
console.log();

// ARROW FUNCTIONS
console.log("=== ARROW FUNCTIONS ===");
const add = (a: number, b: number): number => a + b;
console.log(`Arrow function: 3 + 4 = ${add(3, 4)}`);

const square = (x: number): number => x ** 2;
console.log(`Square of 5: ${square(5)}`);

// Single expression, implicit return
const double = (x: number) => x * 2;
console.log(`Double of 7: ${double(7)}`);
console.log();

// REST PARAMETERS
console.log("=== REST PARAMETERS ===");
function sumAll(...numbers: number[]): number {
    return numbers.reduce((sum, num) => sum + num, 0);
}
console.log(`Sum of 1,2,3: ${sumAll(1, 2, 3)}`);
console.log(`Sum of 5,10,15,20: ${sumAll(5, 10, 15, 20)}`);
console.log();

// FUNCTION TYPES
console.log("=== FUNCTION TYPES ===");
type MathOperation = (a: number, b: number) => number;

const subtract: MathOperation = (a, b) => a - b;
const divide: MathOperation = (a, b) => a / b;

console.log(`10 - 3 = ${subtract(10, 3)}`);
console.log(`10 / 2 = ${divide(10, 2)}`);
console.log();

// CALLBACK FUNCTIONS
console.log("=== CALLBACK FUNCTIONS ===");
function processArray(arr: number[], callback: (x: number) => number): number[] {
    return arr.map(callback);
}

const nums = [1, 2, 3, 4, 5];
const squared = processArray(nums, x => x ** 2);
console.log(`Squared: ${squared}`);
console.log();

// FUNCTION OVERLOADING
console.log("=== FUNCTION OVERLOADING ===");
function format(value: string): string;
function format(value: number): string;
function format(value: string | number): string {
    if (typeof value === "string") {
        return value.toUpperCase();
    }
    return value.toFixed(2);
}

console.log(format("hello"));
console.log(format(3.14159));
console.log();

// PRACTICAL EXAMPLES
console.log("=== PRACTICAL EXAMPLES ===");

// Temperature converter
function celsiusToFahrenheit(celsius: number): number {
    return (celsius * 9/5) + 32;
}
console.log(`25°C = ${celsiusToFahrenheit(25)}°F`);

// Factorial
function factorial(n: number): number {
    let result = 1;
    for (let i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}
console.log(`Factorial of 5: ${factorial(5)}`);

// Get statistics
function getStatistics(numbers: number[]): {min: number, max: number, avg: number} {
    return {
        min: Math.min(...numbers),
        max: Math.max(...numbers),
        avg: numbers.reduce((a, b) => a + b, 0) / numbers.length
    };
}

const data = [10, 20, 30, 40, 50];
const stats = getStatistics(data);
console.log(`Stats: ${JSON.stringify(stats)}`);

