/**
 * TypeScript Crash Course - Lesson 4: Loops (for, while, do-while)
 * ==================================================================
 * Learn to repeat actions efficiently
 */

// FOR LOOP - Iterate a specific number of times
console.log("=== BASIC FOR LOOP ===");
for (let i: number = 0; i < 5; i++) {  // 0 to 4
    console.log(`Count: ${i}`);
}
console.log();

// FOR LOOP WITH RANGE
console.log("=== FOR LOOP WITH RANGE ===");
for (let i: number = 1; i <= 10; i++) {  // 1 to 10
    console.log(`Number: ${i}`);
}
console.log();

// FOR LOOP WITH STEP
console.log("=== FOR LOOP WITH STEP ===");
// Print even numbers from 0 to 10
for (let i: number = 0; i <= 10; i += 2) {
    console.log(`Even number: ${i}`);
}
console.log();

// WHILE LOOP
// Repeats while a condition is true
console.log("=== WHILE LOOP ===");
let count: number = 1;
while (count <= 5) {
    console.log(`Count: ${count}`);
    count++;  // Important: update the counter!
}
console.log();

// DO-WHILE LOOP
// Executes at least once, then checks condition
console.log("=== DO-WHILE LOOP ===");
let num: number = 1;
do {
    console.log(`Number: ${num}`);
    num++;
} while (num <= 3);
console.log();

// BREAK STATEMENT
// Exit the loop prematurely
console.log("=== BREAK STATEMENT ===");
for (let i: number = 1; i <= 10; i++) {
    if (i === 5) {
        console.log("Breaking at 5");
        break;
    }
    console.log(`Number: ${i}`);
}
console.log();

// CONTINUE STATEMENT
// Skip the rest of the current iteration
console.log("=== CONTINUE STATEMENT ===");
for (let i: number = 1; i <= 5; i++) {
    if (i === 3) {
        console.log("Skipping 3");
        continue;
    }
    console.log(`Number: ${i}`);
}
console.log();

// NESTED LOOPS
console.log("=== NESTED LOOPS ===");
// Print a multiplication table
for (let i: number = 1; i <= 3; i++) {
    for (let j: number = 1; j <= 3; j++) {
        console.log(`${i} x ${j} = ${i * j}`);
    }
    console.log();  // Empty line after each row
}

// FOR...OF LOOP (for arrays)
console.log("=== FOR...OF LOOP ===");
const fruits: string[] = ["apple", "banana", "orange"];
for (const fruit of fruits) {
    console.log(`Fruit: ${fruit}`);
}
console.log();

// FOR...IN LOOP (for object properties)
console.log("=== FOR...IN LOOP ===");
const person = {
    name: "Alice",
    age: 25,
    city: "NYC"
};

for (const key in person) {
    console.log(`${key}: ${person[key as keyof typeof person]}`);
}
console.log();

// ARRAY forEach METHOD
console.log("=== ARRAY forEach METHOD ===");
const numbers: number[] = [1, 2, 3, 4, 5];
numbers.forEach((num: number, index: number) => {
    console.log(`Index ${index}: ${num}`);
});
console.log();

// PRACTICAL EXAMPLES
console.log("=== PRACTICAL EXAMPLES ===");

// Example 1: Sum of numbers from 1 to 10
let total: number = 0;
for (let i: number = 1; i <= 10; i++) {
    total += i;
}
console.log(`Sum of 1 to 10: ${total}`);
console.log();

// Example 2: Countdown timer
console.log("Countdown:");
let countdown: number = 5;
while (countdown > 0) {
    console.log(countdown);
    countdown--;
}
console.log("Blast off!");
console.log();

// Example 3: Find first number divisible by 7 and 5
for (let num: number = 1; num <= 100; num++) {
    if (num % 7 === 0 && num % 5 === 0) {
        console.log(`First number divisible by both 7 and 5: ${num}`);
        break;
    }
}
console.log();

// Example 4: Print only odd numbers
console.log("Odd numbers from 1 to 10:");
for (let i: number = 1; i <= 10; i++) {
    if (i % 2 === 0) {  // If even, skip
        continue;
    }
    process.stdout.write(`${i} `);
}
console.log("\n");

// Example 5: Factorial calculation
let factNum: number = 5;
let factorial: number = 1;
for (let i: number = 1; i <= factNum; i++) {
    factorial *= i;
}
console.log(`Factorial of ${factNum}: ${factorial}`);
console.log();

// Example 6: Pattern printing
console.log("Pattern:");
for (let i: number = 1; i <= 5; i++) {
    console.log("*".repeat(i));
}
console.log();

// Example 7: Reverse counting
console.log("Reverse count:");
for (let i: number = 5; i >= 1; i--) {
    console.log(i);
}
console.log();

// Example 8: Array iteration with index
console.log("=== ARRAY ITERATION WITH INDEX ===");
const colors: string[] = ["red", "green", "blue"];

console.log("Method 1: Traditional for loop");
for (let i: number = 0; i < colors.length; i++) {
    console.log(`  ${i}: ${colors[i]}`);
}
console.log();

console.log("Method 2: for...of with entries()");
for (const [index, color] of colors.entries()) {
    console.log(`  ${index}: ${color}`);
}
console.log();

// Example 9: Infinite loop prevention
console.log("=== SAFE LOOPING WITH MAX ITERATIONS ===");
let value: number = 10;
let maxIterations: number = 1000;
let iterations: number = 0;

while (value > 0 && iterations < maxIterations) {
    value -= 0.1;
    iterations++;
}
console.log(`Stopped after ${iterations} iterations`);

