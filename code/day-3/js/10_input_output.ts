/**
 * TypeScript Crash Course - Lesson 10: Input and Output
 * =======================================================
 * Learn to interact with users through console I/O
 */

import * as readline from 'readline';

// BASIC CONSOLE OUTPUT
console.log("=== BASIC OUTPUT ===");
console.log("Hello, TypeScript!");
console.log("Multiple", "arguments", "with", "console.log");
console.log("Age:", 25);
console.log();

// FORMATTED OUTPUT
console.log("=== FORMATTED OUTPUT ===");
const name: string = "Alice";
const age: number = 25;
const city: string = "New York";

// Template literals (preferred)
console.log(`Name: ${name}, Age: ${age}, City: ${city}`);

// String concatenation
console.log("Name: " + name + ", Age: " + age);
console.log();

// NUMBER FORMATTING
console.log("=== NUMBER FORMATTING ===");
const price: number = 19.99;
const quantity: number = 5;
const total: number = price * quantity;

console.log(`Price: $${price.toFixed(2)}`);
console.log(`Total: $${total.toFixed(2)}`);
console.log();

// CONSOLE METHODS
console.log("=== CONSOLE METHODS ===");
console.log("Standard output");
console.error("Error message");
console.warn("Warning message");
console.info("Info message");
console.debug("Debug message");
console.log();

// CONSOLE TABLE
console.log("=== CONSOLE TABLE ===");
const users = [
    { name: "Alice", age: 25, city: "NYC" },
    { name: "Bob", age: 30, city: "LA" },
    { name: "Charlie", age: 35, city: "Chicago" }
];
console.table(users);
console.log();

// TIMING
console.log("=== TIMING ===");
console.time("Operation");
let sum = 0;
for (let i = 0; i < 1000000; i++) {
    sum += i;
}
console.timeEnd("Operation");
console.log();

// INPUT WITH READLINE (Async)
console.log("=== INPUT WITH READLINE ===");
console.log("Note: This demonstrates async input handling\n");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Example function for getting input
function askQuestion(query: string): Promise<string> {
    return new Promise(resolve => {
        rl.question(query, (answer: string) => {
            resolve(answer);
        });
    });
}

// Example usage (commented out to prevent hanging)
async function exampleInputOutput() {
    console.log("--- Simple Calculator ---");
    
    // Simulated input (for demonstration)
    const num1: number = 10;
    const num2: number = 5;
    const operation: string = "+";
    
    console.log(`Enter first number: ${num1}`);
    console.log(`Enter second number: ${num2}`);
    console.log(`Enter operation (+, -, *, /): ${operation}`);
    
    let result: number | string;
    switch (operation) {
        case "+":
            result = num1 + num2;
            break;
        case "-":
            result = num1 - num2;
            break;
        case "*":
            result = num1 * num2;
            break;
        case "/":
            result = num2 !== 0 ? num1 / num2 : "Error: Division by zero";
            break;
        default:
            result = "Invalid operation";
    }
    
    console.log(`Result: ${num1} ${operation} ${num2} = ${result}`);
    console.log();
}

// Run the example
exampleInputOutput().then(() => {
    rl.close();
});

// COMMAND LINE ARGUMENTS
console.log("=== COMMAND LINE ARGUMENTS ===");
console.log("Process args:", process.argv);
console.log(`Script name: ${process.argv[1]}`);
console.log("Arguments:", process.argv.slice(2));
console.log();

// ENVIRONMENT VARIABLES
console.log("=== ENVIRONMENT VARIABLES ===");
console.log(`Node version: ${process.version}`);
console.log(`Platform: ${process.platform}`);
console.log(`Current directory: ${process.cwd()}`);
console.log();

// FILE OUTPUT (using fs)
console.log("=== FILE I/O (Example) ===");
console.log("To write to file:");
console.log(`
import * as fs from 'fs';
fs.writeFileSync('output.txt', 'Hello, File!');
const content = fs.readFileSync('output.txt', 'utf-8');
console.log(content);
`);

// FORMATTED TABLE OUTPUT
console.log("=== FORMATTED TABLE ===");
const scores = [
    { name: "Alice", math: 95, science: 92 },
    { name: "Bob", math: 87, science: 89 },
    { name: "Charlie", math: 91, science: 94 }
];

console.log("Name\t\tMath\tScience\tAverage");
console.log("----------------------------------------");
scores.forEach(student => {
    const avg = ((student.math + student.science) / 2).toFixed(1);
    console.log(`${student.name}\t\t${student.math}\t${student.science}\t${avg}`);
});

