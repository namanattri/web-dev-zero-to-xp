/**
 * TypeScript Crash Course - Lesson 5: Arrays
 * ============================================
 * Learn to work with ordered collections of items
 */

// CREATING ARRAYS
console.log("=== CREATING ARRAYS ===");
// Arrays can contain any type of data
const fruits: string[] = ["apple", "banana", "orange"];
const numbers: number[] = [1, 2, 3, 4, 5];
const mixed: any[] = [1, "hello", true, 3.14];  // Mixed types (avoid if possible)
const emptyArray: string[] = [];

// Alternative syntax
const alternativeNumbers: Array<number> = [1, 2, 3];

console.log(`Fruits: ${fruits}`);
console.log(`Numbers: ${numbers}`);
console.log(`Mixed: ${mixed}`);
console.log(`Empty array: ${emptyArray}`);
console.log();

// ACCESSING ARRAY ITEMS
console.log("=== ACCESSING ARRAY ITEMS ===");
const colors: string[] = ["red", "green", "blue", "yellow"];
console.log(`First color: ${colors[0]}`);  // Index starts at 0
console.log(`Second color: ${colors[1]}`);
console.log(`Last color: ${colors[colors.length - 1]}`);
console.log(`Array length: ${colors.length}`);
console.log();

// MODIFYING ARRAYS
console.log("=== MODIFYING ARRAYS ===");
const animals: string[] = ["cat", "dog", "bird"];
console.log(`Original: ${animals}`);

animals[1] = "hamster";  // Change an item
console.log(`After modification: ${animals}`);
console.log();

// ADDING ITEMS
console.log("=== ADDING ITEMS ===");
const numList: number[] = [1, 2, 3];
console.log(`Original: ${numList}`);

numList.push(4);  // Add to the end
console.log(`After push(4): ${numList}`);

numList.unshift(0);  // Add to the beginning
console.log(`After unshift(0): ${numList}`);

const extended: number[] = numList.concat([5, 6]);  // Combine arrays (returns new array)
console.log(`After concat([5, 6]): ${extended}`);
console.log();

// REMOVING ITEMS
console.log("=== REMOVING ITEMS ===");
const items: string[] = ["a", "b", "c", "d", "e"];
console.log(`Original: ${items}`);

const popped: string | undefined = items.pop();  // Remove and return last item
console.log(`After pop(): ${items}, Popped: ${popped}`);

const shifted: string | undefined = items.shift();  // Remove and return first item
console.log(`After shift(): ${items}, Shifted: ${shifted}`);

items.splice(1, 1);  // Remove 1 item at index 1
console.log(`After splice(1, 1): ${items}`);
console.log();

// ARRAY METHODS
console.log("=== ARRAY METHODS ===");
const nums: number[] = [3, 1, 4, 1, 5, 9, 2];
console.log(`Array: ${nums}`);
console.log(`Length: ${nums.length}`);
console.log(`Includes 4: ${nums.includes(4)}`);
console.log(`Index of 4: ${nums.indexOf(4)}`);
console.log(`Index of 10: ${nums.indexOf(10)}`);  // Returns -1 if not found
console.log();

// SORTING ARRAYS
console.log("=== SORTING ARRAYS ===");
const numbersList: number[] = [5, 2, 8, 1, 9];
console.log(`Original: ${numbersList}`);

const sorted: number[] = [...numbersList].sort((a, b) => a - b);  // Sort numbers ascending
console.log(`Sorted ascending: ${sorted}`);

const sortedDesc: number[] = [...numbersList].sort((a, b) => b - a);  // Sort descending
console.log(`Sorted descending: ${sortedDesc}`);

const words: string[] = ["banana", "apple", "cherry"];
const sortedWords: string[] = [...words].sort();
console.log(`Sorted words: ${sortedWords}`);
console.log();

// ARRAY SLICING
console.log("=== ARRAY SLICING ===");
const letters: string[] = ["a", "b", "c", "d", "e", "f"];
console.log(`Full array: ${letters}`);
console.log(`First three: ${letters.slice(0, 3)}`);
console.log(`From index 2 onwards: ${letters.slice(2)}`);
console.log(`Last three: ${letters.slice(-3)}`);
console.log(`Reversed: ${[...letters].reverse()}`);
console.log();

// ARRAY ITERATION
console.log("=== ARRAY ITERATION ===");
const fruitList: string[] = ["apple", "banana", "orange"];

console.log("Method 1: forEach");
fruitList.forEach((fruit: string, index: number) => {
    console.log(`  ${index}: ${fruit}`);
});
console.log();

console.log("Method 2: for...of");
for (const fruit of fruitList) {
    console.log(`  ${fruit}`);
}
console.log();

console.log("Method 3: Traditional for loop");
for (let i: number = 0; i < fruitList.length; i++) {
    console.log(`  ${i}: ${fruitList[i]}`);
}
console.log();

// ARRAY MAP
console.log("=== ARRAY MAP ===");
const numsToSquare: number[] = [1, 2, 3, 4, 5];
const squares: number[] = numsToSquare.map((x: number) => x ** 2);
console.log(`Original: ${numsToSquare}`);
console.log(`Squares: ${squares}`);

const wordsToUpper: string[] = ["hello", "world"];
const upperWords: string[] = wordsToUpper.map((word: string) => word.toUpperCase());
console.log(`Uppercase: ${upperWords}`);
console.log();

// ARRAY FILTER
console.log("=== ARRAY FILTER ===");
const allNumbers: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const evens: number[] = allNumbers.filter((x: number) => x % 2 === 0);
console.log(`Even numbers: ${evens}`);

const scores: number[] = [45, 67, 89, 92, 56, 78, 88];
const passingScores: number[] = scores.filter((score: number) => score >= 60);
console.log(`Passing scores: ${passingScores}`);
console.log();

// ARRAY REDUCE
console.log("=== ARRAY REDUCE ===");
const valuesToSum: number[] = [1, 2, 3, 4, 5];
const sum: number = valuesToSum.reduce((acc: number, val: number) => acc + val, 0);
console.log(`Sum: ${sum}`);

const maxValue: number = valuesToSum.reduce((max: number, val: number) => val > max ? val : max);
console.log(`Max value: ${maxValue}`);
console.log();

// MULTI-DIMENSIONAL ARRAYS
console.log("=== MULTI-DIMENSIONAL ARRAYS ===");
const matrix: number[][] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

console.log("2D Matrix:");
matrix.forEach(row => console.log(row));
console.log();

console.log(`Element at [0][0]: ${matrix[0][0]}`);
console.log(`Element at [1][2]: ${matrix[1][2]}`);
console.log();

// SPREADING ARRAYS
console.log("=== SPREADING ARRAYS ===");
const arr1: number[] = [1, 2, 3];
const arr2: number[] = [4, 5, 6];
const combined: number[] = [...arr1, ...arr2];
console.log(`Combined: ${combined}`);

const arrCopy: number[] = [...arr1];
console.log(`Copy: ${arrCopy}`);
console.log();

// DESTRUCTURING ARRAYS
console.log("=== DESTRUCTURING ARRAYS ===");
const coords: [number, number, number] = [10, 20, 30];
const [x, y, z] = coords;
console.log(`x: ${x}, y: ${y}, z: ${z}`);

const [first, ...rest] = [1, 2, 3, 4, 5];
console.log(`First: ${first}, Rest: ${rest}`);
console.log();

// PRACTICAL EXAMPLES
console.log("=== PRACTICAL EXAMPLES ===");

// Example 1: Remove duplicates
const withDuplicates: number[] = [1, 2, 2, 3, 4, 4, 5];
const unique: number[] = [...new Set(withDuplicates)];
console.log(`Unique numbers: ${unique}`);

// Example 2: Find min and max
const dataPoints: number[] = [12, 45, 23, 67, 34, 89, 15];
const min: number = Math.min(...dataPoints);
const max: number = Math.max(...dataPoints);
console.log(`Min: ${min}, Max: ${max}`);

// Example 3: Check if all elements satisfy condition
const ages: number[] = [20, 25, 30, 35];
const allAdults: boolean = ages.every((age: number) => age >= 18);
console.log(`All adults: ${allAdults}`);

// Example 4: Check if at least one element satisfies condition
const hasMinor: boolean = ages.some((age: number) => age < 18);
console.log(`Has minor: ${hasMinor}`);

// Example 5: Flatten nested array
const nested: number[][] = [[1, 2], [3, 4], [5, 6]];
const flattened: number[] = nested.flat();
console.log(`Flattened: ${flattened}`);

