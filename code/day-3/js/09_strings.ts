/**
 * TypeScript Crash Course - Lesson 9: String Manipulation
 * =========================================================
 * Learn to work with text data effectively
 */

// BASIC STRING OPERATIONS
console.log("=== BASIC STRING OPERATIONS ===");
const text: string = "Hello, TypeScript!";
console.log(`String: ${text}`);
console.log(`Length: ${text.length}`);
console.log(`First character: ${text[0]}`);
console.log(`Last character: ${text[text.length - 1]}`);
console.log();

// CASE CONVERSION
console.log("=== CASE CONVERSION ===");
const message: string = "Hello World";
console.log(`Original: ${message}`);
console.log(`Uppercase: ${message.toUpperCase()}`);
console.log(`Lowercase: ${message.toLowerCase()}`);
console.log();

// STRING SLICING
console.log("=== STRING SLICING ===");
const str: string = "TypeScript Programming";
console.log(`Full string: ${str}`);
console.log(`First 10 characters: ${str.slice(0, 10)}`);
console.log(`From index 11 onwards: ${str.slice(11)}`);
console.log(`Last 11 characters: ${str.slice(-11)}`);
console.log();

// STRING METHODS
console.log("=== STRING METHODS ===");
console.log(`Includes 'Script': ${str.includes("Script")}`);
console.log(`Starts with 'Type': ${str.startsWith("Type")}`);
console.log(`Ends with 'ing': ${str.endsWith("ing")}`);
console.log(`Index of 'Script': ${str.indexOf("Script")}`);
console.log();

// TEMPLATE LITERALS
console.log("=== TEMPLATE LITERALS ===");
const name: string = "Alice";
const age: number = 25;
const greeting: string = `My name is ${name} and I am ${age} years old`;
console.log(greeting);

// Multi-line strings
const multiLine: string = `This is
a multi-line
string`;
console.log(multiLine);
console.log();

// SPLITTING AND JOINING
console.log("=== SPLITTING AND JOINING ===");
const sentence: string = "TypeScript is awesome and fun";
const words: string[] = sentence.split(" ");
console.log(`Split into words: ${words}`);

const joined: string = words.join("-");
console.log(`Joined with hyphens: ${joined}`);
console.log();

// TRIMMING
console.log("=== TRIMMING ===");
const padded: string = "   Hello, World!   ";
console.log(`Original: '${padded}'`);
console.log(`Trimmed: '${padded.trim()}'`);
console.log(`Left trim: '${padded.trimStart()}'`);
console.log(`Right trim: '${padded.trimEnd()}'`);
console.log();

// REPLACING
console.log("=== REPLACING ===");
const original: string = "I love Java programming";
const replaced: string = original.replace("Java", "TypeScript");
console.log(`Original: ${original}`);
console.log(`Replaced: ${replaced}`);

// Replace all occurrences
const multipleWords: string = "one one one";
const replacedAll: string = multipleWords.replaceAll("one", "two");
console.log(`Replace all: ${replacedAll}`);
console.log();

// STRING PADDING
console.log("=== STRING PADDING ===");
const num: string = "5";
console.log(`Pad start: '${num.padStart(3, "0")}'`);  // "005"
console.log(`Pad end: '${num.padEnd(3, "0")}'`);  // "500"
console.log();

// PRACTICAL EXAMPLES
console.log("=== PRACTICAL EXAMPLES ===");

// Reverse a string
function reverseString(str: string): string {
    return str.split("").reverse().join("");
}
console.log(`Reversed 'hello': ${reverseString("hello")}`);

// Count vowels
function countVowels(str: string): number {
    const vowels = "aeiouAEIOU";
    return str.split("").filter(char => vowels.includes(char)).length;
}
console.log(`Vowels in 'TypeScript': ${countVowels("TypeScript")}`);

// Is palindrome
function isPalindrome(str: string): boolean {
    const cleaned = str.toLowerCase().replace(/[^a-z0-9]/g, "");
    return cleaned === cleaned.split("").reverse().join("");
}
console.log(`'racecar' is palindrome: ${isPalindrome("racecar")}`);

// Title case
function toTitleCase(str: string): string {
    return str.split(" ")
        .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
        .join(" ");
}
console.log(`Title case: ${toTitleCase("hello world typescript")}`);

