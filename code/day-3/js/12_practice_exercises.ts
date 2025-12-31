/**
 * TypeScript Crash Course - Lesson 12: Practice Exercises
 * =========================================================
 * Put your skills to the test with practical challenges
 */

console.log("=".repeat(60));
console.log("TYPESCRIPT PRACTICE EXERCISES");
console.log("=".repeat(60));
console.log();

// EXERCISE 1: FizzBuzz
console.log("=== EXERCISE 1: FizzBuzz ===");
console.log("Print numbers 1-30, but:");
console.log("- Print 'Fizz' for multiples of 3");
console.log("- Print 'Buzz' for multiples of 5");
console.log("- Print 'FizzBuzz' for multiples of both");
console.log();

for (let i: number = 1; i <= 30; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        process.stdout.write("FizzBuzz ");
    } else if (i % 3 === 0) {
        process.stdout.write("Fizz ");
    } else if (i % 5 === 0) {
        process.stdout.write("Buzz ");
    } else {
        process.stdout.write(`${i} `);
    }
}
console.log("\n");

// EXERCISE 2: Palindrome Checker
console.log("=== EXERCISE 2: Palindrome Checker ===");

function isPalindrome(text: string): boolean {
    const cleaned: string = text.replace(/[^a-z0-9]/gi, "").toLowerCase();
    return cleaned === cleaned.split("").reverse().join("");
}

const testWords: string[] = ["racecar", "hello", "A man a plan a canal Panama", "typescript"];
testWords.forEach(word => {
    const result: string = isPalindrome(word) ? "is" : "is not";
    console.log(`'${word}' ${result} a palindrome`);
});
console.log();

// EXERCISE 3: Find Prime Numbers
console.log("=== EXERCISE 3: Find Prime Numbers ===");

function isPrime(n: number): boolean {
    if (n < 2) return false;
    for (let i: number = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) return false;
    }
    return true;
}

const primes: number[] = [];
for (let num: number = 2; num < 50; num++) {
    if (isPrime(num)) primes.push(num);
}
console.log(`Prime numbers up to 50: ${primes}`);
console.log();

// EXERCISE 4: Reverse Words in Sentence
console.log("=== EXERCISE 4: Reverse Words in Sentence ===");

function reverseWords(sentence: string): string {
    return sentence.split(" ").reverse().join(" ");
}

const sentence: string = "TypeScript is awesome";
const reversed: string = reverseWords(sentence);
console.log(`Original: ${sentence}`);
console.log(`Reversed: ${reversed}`);
console.log();

// EXERCISE 5: Character Counter
console.log("=== EXERCISE 5: Character Counter ===");

function countCharacters(text: string): Map<string, number> {
    const charCount: Map<string, number> = new Map();
    for (const char of text.toLowerCase()) {
        if (/[a-z0-9]/.test(char)) {
            charCount.set(char, (charCount.get(char) || 0) + 1);
        }
    }
    return charCount;
}

const text: string = "Hello World";
const charCounts: Map<string, number> = countCharacters(text);
console.log(`Text: '${text}'`);
console.log("Character frequencies:");
charCounts.forEach((count, char) => {
    console.log(`  ${char}: ${count}`);
});
console.log();

// EXERCISE 6: Find Duplicates
console.log("=== EXERCISE 6: Find Duplicates in Array ===");

function findDuplicates<T>(arr: T[]): T[] {
    const seen: Set<T> = new Set();
    const duplicates: Set<T> = new Set();
    
    arr.forEach(item => {
        if (seen.has(item)) {
            duplicates.add(item);
        }
        seen.add(item);
    });
    
    return Array.from(duplicates);
}

const numbers: number[] = [1, 2, 3, 2, 4, 5, 1, 6, 7, 3];
const dups: number[] = findDuplicates(numbers);
console.log(`Array: ${numbers}`);
console.log(`Duplicates: ${dups}`);
console.log();

// EXERCISE 7: Fibonacci Sequence
console.log("=== EXERCISE 7: Fibonacci Sequence ===");

function fibonacci(n: number): number[] {
    if (n <= 0) return [];
    if (n === 1) return [0];
    
    const fib: number[] = [0, 1];
    for (let i: number = 2; i < n; i++) {
        fib.push(fib[i-1] + fib[i-2]);
    }
    return fib;
}

const fibSequence: number[] = fibonacci(10);
console.log(`First 10 Fibonacci numbers: ${fibSequence}`);
console.log();

// EXERCISE 8: Anagram Checker
console.log("=== EXERCISE 8: Anagram Checker ===");

function areAnagrams(str1: string, str2: string): boolean {
    const clean1: string = str1.replace(/\s/g, "").toLowerCase();
    const clean2: string = str2.replace(/\s/g, "").toLowerCase();
    return clean1.split("").sort().join("") === clean2.split("").sort().join("");
}

const pairs: [string, string][] = [
    ["listen", "silent"],
    ["hello", "world"],
    ["The eyes", "They see"]
];

pairs.forEach(([word1, word2]) => {
    const result: string = areAnagrams(word1, word2) ? "are" : "are not";
    console.log(`'${word1}' and '${word2}' ${result} anagrams`);
});
console.log();

// EXERCISE 9: Array Flattener
console.log("=== EXERCISE 9: Flatten Nested Array ===");

function flattenArray<T>(arr: (T | T[])[]): T[] {
    const flat: T[] = [];
    arr.forEach(item => {
        if (Array.isArray(item)) {
            flat.push(...flattenArray(item));
        } else {
            flat.push(item);
        }
    });
    return flat;
}

const nested: (number | number[])[] = [1, [2, 3], [4, [5, 6]], 7];
const flattened: number[] = flattenArray(nested);
console.log(`Nested: ${JSON.stringify(nested)}`);
console.log(`Flattened: ${flattened}`);
console.log();

// EXERCISE 10: Simple Statistics
console.log("=== EXERCISE 10: Calculate Statistics ===");

interface Stats {
    mean: number;
    median: number;
    mode: number;
}

function calculateStats(nums: number[]): Stats {
    // Mean
    const mean: number = nums.reduce((a, b) => a + b, 0) / nums.length;
    
    // Median
    const sorted: number[] = [...nums].sort((a, b) => a - b);
    const mid: number = Math.floor(sorted.length / 2);
    const median: number = sorted.length % 2 === 0
        ? (sorted[mid - 1] + sorted[mid]) / 2
        : sorted[mid];
    
    // Mode (most frequent)
    const frequency: Map<number, number> = new Map();
    nums.forEach(num => {
        frequency.set(num, (frequency.get(num) || 0) + 1);
    });
    
    let mode: number = nums[0];
    let maxFreq: number = 0;
    frequency.forEach((freq, num) => {
        if (freq > maxFreq) {
            maxFreq = freq;
            mode = num;
        }
    });
    
    return { mean, median, mode };
}

const data: number[] = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7];
const stats: Stats = calculateStats(data);
console.log(`Data: ${data}`);
console.log(`Mean: ${stats.mean.toFixed(2)}`);
console.log(`Median: ${stats.median}`);
console.log(`Mode: ${stats.mode}`);
console.log();

console.log("=".repeat(60));
console.log("CONGRATULATIONS! You've completed all exercises!");
console.log("Keep practicing to master TypeScript programming!");
console.log("=".repeat(60));

