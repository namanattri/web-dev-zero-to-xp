/**
 * TypeScript Crash Course - Lesson 11: References and Mutability
 * ================================================================
 * Learn how JavaScript/TypeScript handles references and memory
 */

// VARIABLES ARE REFERENCES
console.log("=== VARIABLES ARE REFERENCES ===");
const arr1: number[] = [1, 2, 3];
const arr2: number[] = arr1;  // Both reference the same array

console.log(`arr1: ${arr1}`);
console.log(`arr2: ${arr2}`);
console.log(`Are they the same? ${arr1 === arr2}`);

arr2.push(4);
console.log(`After arr2.push(4):`);
console.log(`arr1: ${arr1}`);  // Also changed!
console.log(`arr2: ${arr2}`);
console.log();

// PRIMITIVE VS REFERENCE TYPES
console.log("=== PRIMITIVE VS REFERENCE TYPES ===");

// Primitives (immutable)
let x: number = 5;
let y: number = x;
y = 10;
console.log(`Primitives: x = ${x}, y = ${y}`);  // x unchanged

// Objects (mutable)
const obj1 = { value: 5 };
const obj2 = obj1;
obj2.value = 10;
console.log(`Objects: obj1.value = ${obj1.value}, obj2.value = ${obj2.value}`);  // Both changed
console.log();

// COPYING ARRAYS
console.log("=== COPYING ARRAYS ===");

const original: number[] = [1, 2, 3];

// Method 1: Spread operator (shallow copy)
const copy1: number[] = [...original];

// Method 2: Array.from()
const copy2: number[] = Array.from(original);

// Method 3: slice()
const copy3: number[] = original.slice();

copy1.push(4);
console.log(`Original: ${original}`);  // Unchanged
console.log(`Copy1: ${copy1}`);  // Changed
console.log();

// SHALLOW VS DEEP COPY
console.log("=== SHALLOW VS DEEP COPY ===");

const nestedOriginal: number[][] = [[1, 2], [3, 4]];
const shallowCopy: number[][] = [...nestedOriginal];

shallowCopy[0].push(99);
console.log(`Original: ${JSON.stringify(nestedOriginal)}`);  // Also changed!
console.log(`Shallow copy: ${JSON.stringify(shallowCopy)}`);
console.log("⚠️ Shallow copy doesn't copy nested objects!");
console.log();

// Deep copy using JSON (simple but limited)
const nestedOriginal2: number[][] = [[1, 2], [3, 4]];
const deepCopy: number[][] = JSON.parse(JSON.stringify(nestedOriginal2));

deepCopy[0].push(99);
console.log(`Original: ${JSON.stringify(nestedOriginal2)}`);  // Unchanged!
console.log(`Deep copy: ${JSON.stringify(deepCopy)}`);
console.log("✅ Deep copy creates independent copies!");
console.log();

// COPYING OBJECTS
console.log("=== COPYING OBJECTS ===");

const person = { name: "Alice", age: 25 };

// Shallow copy methods
const copy1Obj = { ...person };  // Spread
const copy2Obj = Object.assign({}, person);  // Object.assign

copy1Obj.age = 30;
console.log(`Original: ${JSON.stringify(person)}`);  // Unchanged
console.log(`Copy: ${JSON.stringify(copy1Obj)}`);
console.log();

// CONST VS LET WITH OBJECTS
console.log("=== CONST VS LET WITH OBJECTS ===");

const constArray: number[] = [1, 2, 3];
// constArray = [4, 5, 6];  // Error: Cannot reassign const
constArray.push(4);  // OK: Can modify the array
console.log(`Const array modified: ${constArray}`);

let letArray: number[] = [1, 2, 3];
letArray = [4, 5, 6];  // OK: Can reassign let
console.log(`Let array reassigned: ${letArray}`);
console.log();

// FUNCTION PARAMETERS
console.log("=== FUNCTION PARAMETERS ===");

function modifyArray(arr: number[]): void {
    arr.push(99);
}

function reassignArray(arr: number[]): void {
    arr = [1, 2, 3];  // Only changes local reference
}

const myArray: number[] = [1, 2, 3];
console.log(`Before modifyArray: ${myArray}`);
modifyArray(myArray);
console.log(`After modifyArray: ${myArray}`);  // Changed!

const myArray2: number[] = [10, 20, 30];
console.log(`Before reassignArray: ${myArray2}`);
reassignArray(myArray2);
console.log(`After reassignArray: ${myArray2}`);  // Unchanged!
console.log();

// OBJECT FREEZE (Make immutable)
console.log("=== OBJECT.FREEZE ===");

const frozenObj = Object.freeze({ name: "Alice", age: 25 });
// frozenObj.age = 30;  // Error in strict mode, silently fails otherwise
console.log(`Frozen object: ${JSON.stringify(frozenObj)}`);
console.log();

// PRACTICAL EXAMPLES
console.log("=== PRACTICAL EXAMPLES ===");

// Safe copy function
function safeCopy<T>(data: T): T {
    return JSON.parse(JSON.stringify(data));
}

const data = { users: [{ name: "Alice" }, { name: "Bob" }] };
const dataCopy = safeCopy(data);
dataCopy.users[0].name = "Charlie";

console.log(`Original: ${JSON.stringify(data)}`);
console.log(`Copy: ${JSON.stringify(dataCopy)}`);
console.log();

// Immutable array operations
const numbers: number[] = [1, 2, 3, 4, 5];

// Don't modify original
const doubled: number[] = numbers.map(x => x * 2);
const filtered: number[] = numbers.filter(x => x > 2);

console.log(`Original: ${numbers}`);
console.log(`Doubled: ${doubled}`);
console.log(`Filtered: ${filtered}`);

