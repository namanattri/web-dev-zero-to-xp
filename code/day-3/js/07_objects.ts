/**
 * TypeScript Crash Course - Lesson 7: Objects and Maps
 * ======================================================
 * Learn to work with key-value pairs
 */

// CREATING OBJECTS
console.log("=== CREATING OBJECTS ===");
interface Person {
    name: string;
    age: number;
    city: string;
}

const person: Person = {
    name: "Alice",
    age: 25,
    city: "New York"
};

console.log(`Person: ${JSON.stringify(person)}`);

const emptyObj: {} = {};
console.log(`Empty object: ${JSON.stringify(emptyObj)}`);
console.log();

// ACCESSING VALUES
console.log("=== ACCESSING VALUES ===");
interface Student {
    name: string;
    grade: string;
    score: number;
}

const student: Student = {
    name: "John",
    grade: "A",
    score: 95
};

console.log(`Name (dot notation): ${student.name}`);
console.log(`Grade (bracket notation): ${student["grade"]}`);
console.log();

// MODIFYING OBJECTS
console.log("=== MODIFYING OBJECTS ===");
const car = {
    brand: "Toyota",
    model: "Camry",
    year: 2020
};

console.log(`Original: ${JSON.stringify(car)}`);

car.year = 2021;
console.log(`After updating year: ${JSON.stringify(car)}`);

(car as any).color = "blue";
console.log(`After adding color: ${JSON.stringify(car)}`);
console.log();

// REMOVING PROPERTIES
console.log("=== REMOVING PROPERTIES ===");
const inventory = {
    apples: 10,
    oranges: 5,
    bananas: 8
};

delete (inventory as any).oranges;
console.log(`After deleting oranges: ${JSON.stringify(inventory)}`);
console.log();

// OBJECT METHODS
console.log("=== OBJECT METHODS ===");
const product = {
    name: "Laptop",
    price: 999,
    brand: "Dell"
};

console.log(`Keys: ${Object.keys(product)}`);
console.log(`Values: ${Object.values(product)}`);
console.log(`Entries: ${JSON.stringify(Object.entries(product))}`);
console.log();

// NESTED OBJECTS
console.log("=== NESTED OBJECTS ===");
const students = {
    student1: {
        name: "Alice",
        grade: "A",
        score: 95
    },
    student2: {
        name: "Bob",
        grade: "B",
        score: 87
    }
};

console.log(`Student 1 name: ${students.student1.name}`);
console.log(`Student 2 score: ${students.student2.score}`);
console.log();

// MAP - Better for key-value pairs
console.log("=== MAP ===");
const scores: Map<string, number> = new Map();
scores.set("Alice", 95);
scores.set("Bob", 87);
scores.set("Charlie", 92);

console.log(`Alice's score: ${scores.get("Alice")}`);
console.log(`Map size: ${scores.size}`);
console.log(`Has Bob: ${scores.has("Bob")}`);

console.log("\nIterating Map:");
scores.forEach((score: number, name: string) => {
    console.log(`  ${name}: ${score}`);
});

scores.delete("Bob");
console.log(`\nAfter deleting Bob: ${scores.size} entries`);
console.log();

// OBJECT DESTRUCTURING
console.log("=== OBJECT DESTRUCTURING ===");
const user = { username: "alice", email: "alice@example.com", age: 25 };
const { username, email } = user;
console.log(`Username: ${username}, Email: ${email}`);

// With renaming
const { username: userName, age: userAge } = user;
console.log(`User: ${userName}, Age: ${userAge}`);
console.log();

// SPREAD OPERATOR
console.log("=== SPREAD OPERATOR ===");
const obj1 = { a: 1, b: 2 };
const obj2 = { c: 3, d: 4 };
const merged = { ...obj1, ...obj2 };
console.log(`Merged: ${JSON.stringify(merged)}`);

const objCopy = { ...obj1 };
console.log(`Copy: ${JSON.stringify(objCopy)}`);
console.log();

// PRACTICAL EXAMPLES
console.log("=== PRACTICAL EXAMPLES ===");

// Word counter
const text = "hello world hello python";
const wordCount = new Map<string, number>();
text.split(" ").forEach(word => {
    wordCount.set(word, (wordCount.get(word) || 0) + 1);
});
console.log("Word count:");
wordCount.forEach((count, word) => {
    console.log(`  ${word}: ${count}`);
});

