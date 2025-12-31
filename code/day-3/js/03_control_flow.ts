/**
 * TypeScript Crash Course - Lesson 3: Control Flow (if/else if/else)
 * ====================================================================
 * Learn to make decisions in your code
 */

// BASIC IF STATEMENT
console.log("=== BASIC IF STATEMENT ===");
let age: number = 18;

if (age >= 18) {
    console.log("You are an adult");
}
console.log();

// IF-ELSE STATEMENT
console.log("=== IF-ELSE STATEMENT ===");
let temperature: number = 25;

if (temperature > 30) {
    console.log("It's hot outside!");
} else {
    console.log("The weather is pleasant");
}
console.log();

// IF-ELSE IF-ELSE STATEMENT
console.log("=== IF-ELSE IF-ELSE STATEMENT ===");
let score: number = 85;
let grade: string;

if (score >= 90) {
    grade = "A";
} else if (score >= 80) {
    grade = "B";
} else if (score >= 70) {
    grade = "C";
} else if (score >= 60) {
    grade = "D";
} else {
    grade = "F";
}

console.log(`Score: ${score}, Grade: ${grade}`);
console.log();

// NESTED IF STATEMENTS
console.log("=== NESTED IF STATEMENTS ===");
let userAge: number = 20;
let hasTicket: boolean = true;

if (userAge >= 18) {
    if (hasTicket) {
        console.log("You can enter the concert");
    } else {
        console.log("You need a ticket to enter");
    }
} else {
    console.log("You must be 18 or older");
}
console.log();

// MULTIPLE CONDITIONS WITH LOGICAL OPERATORS
console.log("=== MULTIPLE CONDITIONS ===");
let username: string = "admin";
let password: string = "12345";

if (username === "admin" && password === "12345") {
    console.log("Login successful!");
} else {
    console.log("Invalid credentials");
}
console.log();

// SWITCH STATEMENT
console.log("=== SWITCH STATEMENT ===");
let day: number = 3;
let dayName: string;

switch (day) {
    case 1:
        dayName = "Monday";
        break;
    case 2:
        dayName = "Tuesday";
        break;
    case 3:
        dayName = "Wednesday";
        break;
    case 4:
        dayName = "Thursday";
        break;
    case 5:
        dayName = "Friday";
        break;
    case 6:
        dayName = "Saturday";
        break;
    case 7:
        dayName = "Sunday";
        break;
    default:
        dayName = "Invalid day";
}

console.log(`Day ${day} is ${dayName}`);
console.log();

// SWITCH WITH STRING
console.log("=== SWITCH WITH STRING ===");
let fruit: string = "apple";

switch (fruit) {
    case "apple":
        console.log("Apples are $1.50 per lb");
        break;
    case "banana":
        console.log("Bananas are $0.75 per lb");
        break;
    case "orange":
        console.log("Oranges are $2.00 per lb");
        break;
    default:
        console.log("Fruit not found");
}
console.log();

// TRUTHY AND FALSY VALUES
console.log("=== TRUTHY AND FALSY VALUES ===");
// Falsy values: false, 0, "", null, undefined, NaN
// Everything else is truthy

let value1: string = "";
let value2: number = 0;
let value3: string = "Hello";
let value4: number | null = null;

if (value1) {
    console.log("value1 is truthy");
} else {
    console.log("value1 is falsy (empty string)");
}

if (value2) {
    console.log("value2 is truthy");
} else {
    console.log("value2 is falsy (zero)");
}

if (value3) {
    console.log("value3 is truthy (non-empty string)");
}

if (value4) {
    console.log("value4 is truthy");
} else {
    console.log("value4 is falsy (null)");
}
console.log();

// PRACTICAL EXAMPLES
console.log("=== PRACTICAL EXAMPLES ===");

// Example 1: Check if a number is positive, negative, or zero
let number: number = -5;
if (number > 0) {
    console.log(`${number} is positive`);
} else if (number < 0) {
    console.log(`${number} is negative`);
} else {
    console.log(`${number} is zero`);
}
console.log();

// Example 2: Check if a year is a leap year
let year: number = 2024;
if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
    console.log(`${year} is a leap year`);
} else {
    console.log(`${year} is not a leap year`);
}
console.log();

// Example 3: Determine ticket price based on age
let personAge: number = 12;
let price: number;

if (personAge < 3) {
    price = 0;
} else if (personAge <= 12) {
    price = 10;
} else if (personAge <= 65) {
    price = 20;
} else {
    price = 15;
}

console.log(`Age: ${personAge}, Ticket price: $${price}`);
console.log();

// TERNARY OPERATOR (One-line if-else)
console.log("=== TERNARY OPERATOR ===");
let studentAge: number = 20;
let status: string = studentAge >= 18 ? "Adult" : "Minor";
console.log(`Status: ${status}`);

// Nested ternary
let marks: number = 75;
let result: string = marks >= 90 ? "Excellent" :
                      marks >= 75 ? "Good" :
                      marks >= 50 ? "Pass" : "Fail";
console.log(`Marks: ${marks}, Result: ${result}`);
console.log();

// GUARD CLAUSES (Early Returns)
console.log("=== GUARD CLAUSES (in functions) ===");
function processUser(userName: string | null) {
    if (!userName) {
        console.log("No username provided");
        return;
    }
    
    if (userName.length < 3) {
        console.log("Username too short");
        return;
    }
    
    console.log(`Processing user: ${userName}`);
}

processUser(null);
processUser("ab");
processUser("alice");

