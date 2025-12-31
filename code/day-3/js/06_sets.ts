/**
 * TypeScript Crash Course - Lesson 6: Sets
 * ==========================================
 * Learn to work with unique, unordered collections
 */

// CREATING SETS
console.log("=== CREATING SETS ===");
const fruits: Set<string> = new Set(["apple", "banana", "orange"]);
const numbers: Set<number> = new Set([1, 2, 3, 4, 5]);

// Automatically removes duplicates
const duplicates: Set<number> = new Set([1, 2, 2, 3, 3, 3, 4]);
console.log(`Set with duplicates removed: ${Array.from(duplicates)}`);

const emptySet: Set<any> = new Set();
console.log(`Empty set size: ${emptySet.size}`);
console.log();

// ADDING ITEMS
console.log("=== ADDING ITEMS ===");
const colors: Set<string> = new Set(["red", "green", "blue"]);
console.log(`Original: ${Array.from(colors)}`);

colors.add("yellow");
console.log(`After add('yellow'): ${Array.from(colors)}`);

colors.add("red");  // No effect (already exists)
console.log(`After add('red') again: ${Array.from(colors)}`);
console.log();

// REMOVING ITEMS
console.log("=== REMOVING ITEMS ===");
const nums: Set<number> = new Set([1, 2, 3, 4, 5]);
console.log(`Original: ${Array.from(nums)}`);

nums.delete(3);
console.log(`After delete(3): ${Array.from(nums)}`);

nums.clear();
console.log(`After clear(): ${Array.from(nums)}`);
console.log();

// SET OPERATIONS
console.log("=== SET OPERATIONS ===");
const setA: Set<number> = new Set([1, 2, 3, 4, 5]);
const setB: Set<number> = new Set([4, 5, 6, 7, 8]);

console.log(`Set A: ${Array.from(setA)}`);
console.log(`Set B: ${Array.from(setB)}`);

// Union
const union: Set<number> = new Set([...setA, ...setB]);
console.log(`Union: ${Array.from(union)}`);

// Intersection
const intersection: Set<number> = new Set(
    [...setA].filter(x => setB.has(x))
);
console.log(`Intersection: ${Array.from(intersection)}`);

// Difference (A - B)
const difference: Set<number> = new Set(
    [...setA].filter(x => !setB.has(x))
);
console.log(`Difference (A-B): ${Array.from(difference)}`);

// Symmetric Difference
const symDiff: Set<number> = new Set([
    ...[...setA].filter(x => !setB.has(x)),
    ...[...setB].filter(x => !setA.has(x))
]);
console.log(`Symmetric Difference: ${Array.from(symDiff)}`);
console.log();

// MEMBERSHIP TESTING
console.log("=== MEMBERSHIP TESTING ===");
const fruitSet: Set<string> = new Set(["apple", "banana", "orange"]);
console.log(`Has 'apple': ${fruitSet.has("apple")}`);
console.log(`Has 'mango': ${fruitSet.has("mango")}`);
console.log();

// ITERATING SETS
console.log("=== ITERATING SETS ===");
const colorSet: Set<string> = new Set(["red", "green", "blue"]);

console.log("Using for...of:");
for (const color of colorSet) {
    console.log(`  ${color}`);
}

console.log("\nUsing forEach:");
colorSet.forEach((color: string) => {
    console.log(`  ${color}`);
});
console.log();

// PRACTICAL EXAMPLES
console.log("=== PRACTICAL EXAMPLES ===");

// Remove duplicates from array
const arrWithDups: number[] = [1, 2, 2, 3, 4, 4, 5];
const uniqueArr: number[] = [...new Set(arrWithDups)];
console.log(`Unique: ${uniqueArr}`);

// Find common elements
const courseA: Set<string> = new Set(["Alice", "Bob", "Charlie"]);
const courseB: Set<string> = new Set(["Bob", "Charlie", "David"]);
const common: Set<string> = new Set(
    [...courseA].filter(x => courseB.has(x))
);
console.log(`Students in both courses: ${Array.from(common)}`);

// Check subset
const setX: Set<number> = new Set([1, 2, 3]);
const setY: Set<number> = new Set([1, 2, 3, 4, 5]);
const isSubset: boolean = [...setX].every(x => setY.has(x));
console.log(`Is X subset of Y: ${isSubset}`);

