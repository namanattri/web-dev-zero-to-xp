/**
 * TypeScript Crash Course - Lesson 2: Operators
 * ===============================================
 * Learn to perform operations on data
 */

// ARITHMETIC OPERATORS
console.log("=== ARITHMETIC OPERATORS ===");
let a: number = 10;
let b: number = 3;

console.log(`a = ${a}, b = ${b}`);
console.log(`Addition (a + b): ${a + b}`);
console.log(`Subtraction (a - b): ${a - b}`);
console.log(`Multiplication (a * b): ${a * b}`);
console.log(`Division (a / b): ${a / b}`);  // Always returns float
console.log(`Modulus (a % b): ${a % b}`);  // Remainder
console.log(`Exponentiation (a ** b): ${a ** b}`);  // Power
console.log();

// Note: JavaScript/TypeScript doesn't have floor division operator
// Use Math.floor() instead
console.log(`Floor Division: ${Math.floor(a / b)}`);
console.log();

// COMPARISON OPERATORS
console.log("=== COMPARISON OPERATORS ===");
let x: number = 5;
let y: number = 10;

console.log(`x = ${x}, y = ${y}`);
console.log(`x == y (Equal value): ${x == y}`);
console.log(`x === y (Equal value and type): ${x === y}`);
console.log(`x != y (Not equal value): ${x != y}`);
console.log(`x !== y (Not equal value or type): ${x !== y}`);
console.log(`x > y (Greater than): ${x > y}`);
console.log(`x < y (Less than): ${x < y}`);
console.log(`x >= y (Greater than or equal to): ${x >= y}`);
console.log(`x <= y (Less than or equal to): ${x <= y}`);
console.log();

// LOOSE vs STRICT EQUALITY
console.log("=== LOOSE vs STRICT EQUALITY ===");
let num: number = 5;
let str: string = "5";

console.log(`${num} == "${str}" (loose): ${num == str}`);  // true
console.log(`${num} === "${str}" (strict): ${num === str}`);  // false
console.log("Always prefer === (strict equality)!");
console.log();

// LOGICAL OPERATORS
console.log("=== LOGICAL OPERATORS ===");
let age: number = 20;
let hasLicense: boolean = true;

console.log(`age = ${age}, hasLicense = ${hasLicense}`);
console.log(`age >= 18 && hasLicense: ${age >= 18 && hasLicense}`);
console.log(`age < 18 || hasLicense: ${age < 18 || hasLicense}`);
console.log(`!hasLicense: ${!hasLicense}`);
console.log();

// ASSIGNMENT OPERATORS
console.log("=== ASSIGNMENT OPERATORS ===");
let count: number = 5;
console.log(`Initial count: ${count}`);

count += 3;  // count = count + 3
console.log(`After count += 3: ${count}`);

count -= 2;  // count = count - 2
console.log(`After count -= 2: ${count}`);

count *= 2;  // count = count * 2
console.log(`After count *= 2: ${count}`);

count /= 3;  // count = count / 3
console.log(`After count /= 3: ${count}`);

count %= 3;  // count = count % 3
console.log(`After count %= 3: ${count}`);
console.log();

// INCREMENT AND DECREMENT
console.log("=== INCREMENT AND DECREMENT ===");
let i: number = 5;
console.log(`Initial i: ${i}`);
console.log(`i++: ${i++}`);  // Post-increment (returns then increments)
console.log(`After i++: ${i}`);
console.log(`++i: ${++i}`);  // Pre-increment (increments then returns)
console.log(`i--: ${i--}`);  // Post-decrement
console.log(`After i--: ${i}`);
console.log(`--i: ${--i}`);  // Pre-decrement
console.log();

// TYPEOF OPERATOR
console.log("=== TYPEOF OPERATOR ===");
console.log(`typeof 42: ${typeof 42}`);
console.log(`typeof "hello": ${typeof "hello"}`);
console.log(`typeof true: ${typeof true}`);
console.log(`typeof undefined: ${typeof undefined}`);
console.log(`typeof null: ${typeof null}`);  // Returns "object" (JavaScript quirk)
console.log();

// TERNARY OPERATOR
console.log("=== TERNARY OPERATOR ===");
let userAge: number = 20;
let canVote: string = userAge >= 18 ? "Yes" : "No";
console.log(`Age: ${userAge}, Can vote: ${canVote}`);

// Nested ternary (use sparingly)
let score: number = 85;
let grade: string = score >= 90 ? "A" : score >= 80 ? "B" : score >= 70 ? "C" : "F";
console.log(`Score: ${score}, Grade: ${grade}`);
console.log();

// NULLISH COALESCING OPERATOR (??)
console.log("=== NULLISH COALESCING ===");
let username: string | null = null;
let displayName: string = username ?? "Guest";
console.log(`Display name: ${displayName}`);

let value: number | null = 0;
let result: number = value ?? 10;  // Returns 0 (not 10, because 0 is not null/undefined)
console.log(`Value: ${value}, Result: ${result}`);
console.log();

// OPTIONAL CHAINING (?.)
console.log("=== OPTIONAL CHAINING ===");
interface User {
    name: string;
    address?: {
        street?: string;
        city?: string;
    };
}

let user1: User = { name: "Alice" };
let user2: User = { name: "Bob", address: { city: "NYC" } };

console.log(`User1 city: ${user1.address?.city ?? "Not provided"}`);
console.log(`User2 city: ${user2.address?.city ?? "Not provided"}`);
console.log(`User2 street: ${user2.address?.street ?? "Not provided"}`);
console.log();

// PRACTICAL EXAMPLES
console.log("=== PRACTICAL EXAMPLES ===");

// Calculate area of a rectangle
let length: number = 10;
let width: number = 5;
let area: number = length * width;
console.log(`Rectangle area (length=${length}, width=${width}): ${area}`);

// Check if a number is even or odd
let number: number = 17;
let isEven: boolean = (number % 2 === 0);
console.log(`Is ${number} even? ${isEven}`);

// Calculate average
let score1: number = 85;
let score2: number = 90;
let score3: number = 78;
let average: number = (score1 + score2 + score3) / 3;
console.log(`Average score: ${average.toFixed(2)}`);

