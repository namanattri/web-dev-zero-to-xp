/**
 * TypeScript Crash Course - Lesson 1: Variables and Data Types
 * ==============================================================
 * Learn the fundamental building blocks of TypeScript programming
 */

// VARIABLES
// JavaScript/TypeScript has three ways to declare variables: let, const, var
// Use 'let' for variables that can change
// Use 'const' for constants (cannot be reassigned)
// Avoid 'var' (old way, has scope issues)

console.log("=== VARIABLES ===");
let name: string = "Alice";  // String (text)
let age: number = 25;  // Number (integers and decimals)
let height: number = 5.6;  // Same type for integers and floats
let isStudent: boolean = true;  // Boolean (true or false)

console.log(`Name: ${name}`);
console.log(`Age: ${age}`);
console.log(`Height: ${height}`);
console.log(`Is Student: ${isStudent}`);
console.log();

// CONST vs LET
console.log("=== CONST vs LET ===");
const PI: number = 3.14159;  // Cannot be reassigned
let counter: number = 0;  // Can be reassigned

counter = 10;  // OK
// PI = 3.14; // Error: Cannot assign to 'PI' because it is a constant
console.log(`PI: ${PI}`);
console.log(`Counter: ${counter}`);
console.log();

// BASIC DATA TYPES
// 1. Strings - Text data
console.log("=== STRINGS ===");
let firstName: string = "John";
let lastName: string = "Doe";
let fullName: string = firstName + " " + lastName;  // String concatenation
// Template literals (preferred)
let fullNameTemplate: string = `${firstName} ${lastName}`;

console.log(`Full Name: ${fullName}`);
console.log(`Length of name: ${fullName.length}`);
console.log(`Uppercase: ${fullName.toUpperCase()}`);
console.log(`Lowercase: ${fullName.toLowerCase()}`);
console.log();

// 2. Numbers - No distinction between int and float
console.log("=== NUMBERS ===");
let x: number = 10;  // Integer
let y: number = 3.14;  // Float
console.log(`Integer: ${x}`);
console.log(`Float: ${y}`);
console.log(`Type of x: ${typeof x}`);
console.log(`Type of y: ${typeof y}`);
console.log();

// 3. Booleans - true or false
console.log("=== BOOLEANS ===");
let isRaining: boolean = false;
let isSunny: boolean = true;
console.log(`Is it raining? ${isRaining}`);
console.log(`Is it sunny? ${isSunny}`);
console.log();

// TYPE ANNOTATIONS vs TYPE INFERENCE
console.log("=== TYPE ANNOTATIONS ===");
// Explicit type annotation
let explicitNumber: number = 42;

// Type inference (TypeScript infers the type)
let inferredNumber = 42;  // TypeScript knows this is a number

console.log(`Explicit: ${explicitNumber}, Type: ${typeof explicitNumber}`);
console.log(`Inferred: ${inferredNumber}, Type: ${typeof inferredNumber}`);
console.log();

// TYPE CONVERSION
console.log("=== TYPE CONVERSION ===");
let numString: string = "100";
let numInt: number = parseInt(numString);  // String to integer
let numFloat: number = parseFloat("19.99");  // String to float

console.log(`String '100' to integer: ${numInt}`);
console.log(`String '19.99' to float: ${numFloat}`);

let price: number = 19.99;
let priceString: string = price.toString();  // Number to string
console.log(`Float 19.99 to string: '${priceString}'`);

let value: number = 42;
let valueString: string = String(value);  // Another way to convert
console.log(`Integer 42 to string: '${valueString}'`);
console.log();

// NULL and UNDEFINED
console.log("=== NULL AND UNDEFINED ===");
let notAssigned: undefined = undefined;
let empty: null = null;

console.log(`Undefined: ${notAssigned}, Type: ${typeof notAssigned}`);
console.log(`Null: ${empty}, Type: ${typeof empty}`);
console.log();

// ANY TYPE (avoid when possible)
console.log("=== ANY TYPE (use sparingly) ===");
let anything: any = "Hello";
console.log(`Any as string: ${anything}`);
anything = 42;
console.log(`Any as number: ${anything}`);
anything = true;
console.log(`Any as boolean: ${anything}`);
console.log();

// MULTIPLE DECLARATION
console.log("=== MULTIPLE DECLARATION ===");
let a: number = 1, b: number = 2, c: number = 3;
console.log(`a = ${a}, b = ${b}, c = ${c}`);

// Destructuring assignment
let [d, e, f] = [10, 20, 30];
console.log(`d = ${d}, e = ${e}, f = ${f}`);
console.log();

// TEMPLATE LITERALS
console.log("=== TEMPLATE LITERALS ===");
let productName: string = "Laptop";
let productPrice: number = 999;
let message: string = `The ${productName} costs $${productPrice}`;
console.log(message);

// Multi-line strings
let multiLine: string = `This is
a multi-line
string`;
console.log(multiLine);
console.log();

// TYPE UNIONS
console.log("=== TYPE UNIONS ===");
let id: number | string;  // Can be either number or string
id = 101;
console.log(`ID as number: ${id}`);
id = "ABC123";
console.log(`ID as string: ${id}`);
console.log();

// LITERAL TYPES
console.log("=== LITERAL TYPES ===");
let status: "pending" | "approved" | "rejected";
status = "pending";
console.log(`Status: ${status}`);
// status = "invalid"; // Error: Type '"invalid"' is not assignable

