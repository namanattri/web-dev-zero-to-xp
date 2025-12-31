# TypeScript Crash Course - Day 3

## Setup Instructions

### Prerequisites

1. **Install Node.js** (includes npm)
   - Download from [nodejs.org](https://nodejs.org/)
   - Verify installation:
     ```bash
     node --version
     npm --version
     ```

2. **Install TypeScript globally** (optional but recommended)
   ```bash
   npm install -g typescript ts-node
   ```

### Project Setup

1. **Navigate to the project directory:**
   ```bash
   cd code/day-3/js
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

## Running TypeScript Files

### Method 1: Using ts-node (Recommended for Learning)
```bash
# Run any TypeScript file directly
ts-node 01_variables_and_datatypes.ts
ts-node 02_operators.ts
# etc...
```

### Method 2: Compile then Run
```bash
# Compile TypeScript to JavaScript
tsc 01_variables_and_datatypes.ts

# Run the compiled JavaScript
node 01_variables_and_datatypes.js
```

### Method 3: Compile All Files
```bash
# Compile all TypeScript files
npm run build

# Files will be in the dist/ folder
node dist/01_variables_and_datatypes.js
```

## Course Structure

1. **01_variables_and_datatypes.ts** - Variables, types, type annotations
2. **02_operators.ts** - Arithmetic, comparison, logical operators
3. **03_control_flow.ts** - if/else, switch statements
4. **04_loops.ts** - for, while, do-while loops
5. **05_arrays.ts** - Arrays, methods, multi-dimensional arrays
6. **06_sets.ts** - Sets and set operations
7. **07_objects.ts** - Objects, Maps, key-value pairs
8. **08_functions.ts** - Functions, arrow functions, types
9. **09_strings.ts** - String manipulation and methods
10. **10_input_output.ts** - Console I/O and Node.js basics
11. **11_references.ts** - References, mutability, copying
12. **12_practice_exercises.ts** - Hands-on practice

## TypeScript vs JavaScript

- TypeScript is a **superset** of JavaScript
- Adds **static typing** for better error detection
- Compiles to JavaScript
- All JavaScript code is valid TypeScript
- `.ts` files for TypeScript, `.js` files for JavaScript

## Learning Tips

- Run each example file
- Experiment with the code
- Check the type errors TypeScript catches
- Compare with Python examples in `code/day-3/python/`

