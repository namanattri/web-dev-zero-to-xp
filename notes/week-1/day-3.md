# Day 3: Python Crash Course

## Overview
Welcome to Day 3! Today you'll learn Python fundamentals - the core 20% that covers 80% of what you need to know. This crash course focuses on building solid coding logic and language basics.

## Prerequisites

> **📝 Windows Users:** Before proceeding, it's highly recommended to set up WSL (Windows Subsystem for Linux). See the [Day 2 notes](day-2.md) for complete WSL setup instructions. Once WSL is set up, follow the Linux instructions throughout this guide.

### Check if Python is Installed

Before starting, verify Python is installed on your system:

**On macOS/Linux:**
```bash
python3 --version
```

**On Windows:**
```bash
python --version
```

You should see output like `Python 3.x.x`. If not, follow the installation steps below.

### Installing Python

If Python is not installed:

**On macOS:**
```bash
# Using Homebrew
brew install python3
```

**On Windows:**

*If using WSL (Recommended):*
```bash
# Follow the WSL setup instructions above, then:
sudo apt update
sudo apt install python3 python3-pip -y
```

*If using native Windows (Not Recommended):*
1. Download from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. ✅ **IMPORTANT:** Check "Add Python to PATH" during installation

**On Linux (Ubuntu/Debian) or WSL:**
```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

### Verify Installation
```bash
python3 --version
pip3 --version
```

## Course Structure

The crash course is divided into 12 lessons, each in its own file:

1. **01_variables_and_datatypes.py** - Variables, strings, numbers, booleans, type conversion
2. **02_operators.py** - Arithmetic, comparison, logical, and assignment operators
3. **03_control_flow.py** - if/elif/else statements, decision making
4. **04_loops.py** - for loops, while loops, break, continue
5. **05_lists.py** - Lists, list operations, slicing, comprehensions, multi-dimensional arrays
6. **06_sets.py** - Sets, set operations, union, intersection, difference
7. **07_dictionaries.py** - Dictionaries, key-value pairs, nested structures
8. **08_functions.py** - Defining functions, parameters, return values
9. **09_strings.py** - String manipulation, formatting, methods
10. **10_input_output.py** - User input, output formatting, interactive programs
11. **11_python_references.py** - Understanding references, mutable vs immutable, copying
12. **12_practice_exercises.py** - Hands-on practice problems

## How to Run the Code

### Method 1: Using VS Code Terminal

1. **Open VS Code**
2. **Open the project folder:** File → Open Folder → Select `web-dev-zero-to-xp`
3. **Open the integrated terminal:** View → Terminal (or `` Ctrl+` ``)
4. **Navigate to the code folder:**
   ```bash
   cd code/day-3
   ```
5. **Run any Python file:**
   ```bash
   python3 01_variables_and_datatypes.py
   ```

### Method 2: Using VS Code Run Button

1. **Open the Python file** you want to run in VS Code
2. **Click the ▶️ "Run" button** in the top-right corner
3. The output will appear in the integrated terminal

### Method 3: Using Code Runner Extension (Recommended)

1. **Install Code Runner extension:**
   - Open VS Code Extensions (Ctrl+Shift+X or Cmd+Shift+X)
   - Search for "Code Runner"
   - Click Install

2. **Run code:**
   - Open any Python file
   - Right-click in the editor → "Run Code"
   - Or press `Ctrl+Alt+N` (Windows/Linux) or `Cmd+Alt+N` (Mac)

### Method 4: Using System Terminal

**On macOS/Linux/WSL:**
```bash
cd ~/Projects/ps/web-dev-zero-to-xp/code/day-3/python
python3 01_variables_and_datatypes.py
```

**On Windows (Native - Not Recommended):**
```bash
cd C:\Projects\ps\web-dev-zero-to-xp\code\day-3\python
python 01_variables_and_datatypes.py
```

**Note for Windows users:** If using WSL, use the macOS/Linux commands above.

## Learning Path

### Recommended Order

Follow this sequence for best learning:

1. Start with **01_variables_and_datatypes.py** - Understand the basics
2. Move to **02_operators.py** - Learn to manipulate data
3. Study **03_control_flow.py** - Master decision making
4. Practice **04_loops.py** - Learn repetition and iteration
5. Explore **05_lists.py** - Work with collections and arrays
6. Learn **06_sets.py** - Unique collections and set operations
7. Understand **07_dictionaries.py** - Key-value data structures
8. Master **08_functions.py** - Write reusable code
9. Study **09_strings.py** - Text manipulation
10. Try **10_input_output.py** - Interactive user programs
11. Deep dive into **11_python_references.py** - Understand memory and references
12. Challenge yourself with **12_practice_exercises.py**

### Learning Tips

- **Run every example** - Don't just read, execute the code
- **Modify the code** - Change values and see what happens
- **Break things** - Make mistakes and learn from errors
- **Practice daily** - Consistency is key
- **Build small projects** - Apply what you learn immediately

## Running Multiple Files

To run all lessons in sequence:

```bash
cd code/day-3
for file in *.py; do echo "Running $file"; python3 "$file"; echo ""; done
```

Or run them individually as you complete each lesson.

## Troubleshooting

### "python3: command not found"
- **On WSL/Mac/Linux:** Python 3 might not be installed. Install using package manager.
- **On Windows (Native):** Use `python` instead of `python3`
- **Recommended:** Use WSL on Windows for better compatibility

### "No module named..."
- Some examples use built-in modules only, no installation needed
- If you see this error, the module should be part of Python standard library

### Permission Denied
```bash
chmod +x *.py  # Make files executable (Mac/Linux)
```

### VS Code Not Recognizing Python
1. Install Python extension for VS Code
2. Select Python interpreter: Ctrl+Shift+P → "Python: Select Interpreter"
3. Choose the Python 3.x version installed on your system

## Interactive Mode

For experimenting, use Python's interactive mode:

```bash
python3
>>> print("Hello, World!")
>>> x = 5
>>> x + 3
8
>>> exit()
```

## Next Steps

After completing this crash course:

1. ✅ Complete all 12 lessons
2. ✅ Solve all practice exercises
3. ✅ Build a small project using what you learned
4. ✅ Review concepts you found challenging

## Key Concepts Covered

- ✨ Variables and data types
- ✨ Operators and expressions
- ✨ Control flow (if/else)
- ✨ Loops (for/while)
- ✨ Lists and list operations (including multi-dimensional arrays)
- ✨ Sets and set operations
- ✨ Dictionaries
- ✨ Functions
- ✨ String manipulation
- ✨ Input/Output
- ✨ Python references and memory management
- ✨ Problem-solving with code

## Resources

- **Official Python Docs:** [docs.python.org](https://docs.python.org/3/)
- **Python Tutorial:** [python.org/tutorial](https://docs.python.org/3/tutorial/)
- **Practice Problems:** [leetcode.com](https://leetcode.com), [hackerrank.com](https://www.hackerrank.com)

## Remember

> "The only way to learn a new programming language is by writing programs in it." - Dennis Ritchie

Start with lesson 1 and work your way through. Take your time, experiment, and most importantly - have fun coding! 🚀

---

# Day 3: JavaScript/TypeScript Crash Course

## Overview
This section provides the same comprehensive programming course but using **TypeScript** - a typed superset of JavaScript. TypeScript adds static typing to JavaScript, making it easier to catch errors during development while maintaining full JavaScript compatibility.

## Why TypeScript?

- ✅ **Type Safety** - Catch errors before runtime
- ✅ **Better IDE Support** - Enhanced autocomplete and intellisense
- ✅ **Modern JavaScript** - Use latest ES features
- ✅ **Scales Better** - Ideal for larger projects
- ✅ **Compiles to JavaScript** - Runs anywhere JavaScript runs

## Prerequisites

> **📝 Windows Users:** If you haven't already, set up WSL (Windows Subsystem for Linux). See the [Day 2 notes](day-2.md) for complete WSL setup instructions. Once WSL is set up, follow the macOS/Linux instructions throughout this guide.

### Check if Node.js is Installed

Node.js includes npm (Node Package Manager) which we'll use to install TypeScript.

**On macOS/Linux/WSL:**
```bash
node --version
npm --version
```

You should see version numbers. If not, follow the NVM installation steps below.

### Installing Node.js via NVM (Recommended)

**NVM (Node Version Manager)** is the recommended way to install Node.js. It allows you to:
- Install multiple Node.js versions
- Switch between versions easily
- Avoid permission issues with global packages
- Keep your Node.js installation up-to-date

#### Step 1: Install NVM

**On macOS/Linux/WSL:**

```bash
# Download and install NVM
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# OR using wget
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

After installation, restart your terminal or run:

```bash
# Add NVM to your current shell session
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

**On Windows (Native - Not Recommended):**

*If using WSL (Recommended):* Follow the macOS/Linux/WSL instructions above

*If using native Windows PowerShell:*
1. Download **nvm-windows** from: [github.com/coreybutler/nvm-windows/releases](https://github.com/coreybutler/nvm-windows/releases)
2. Download `nvm-setup.exe` from the latest release
3. Run the installer
4. Restart your terminal

**Verify NVM installation:**
```bash
nvm --version
```

#### Step 2: Install Node.js using NVM

**Install the latest LTS (Long Term Support) version:**

```bash
# Install latest LTS version
nvm install --lts

# OR install a specific version
nvm install 20.11.0

# Use the installed version
nvm use --lts
```

**On Windows:**
```bash
# Install latest LTS version
nvm install lts

# Use the installed version
nvm use lts
```

**Set default Node.js version:**
```bash
nvm alias default node  # Use latest version as default
# OR
nvm alias default 20    # Use Node 20.x as default
```

#### Step 3: Install TypeScript

After Node.js is installed via NVM:

```bash
# Install TypeScript and ts-node globally
npm install -g typescript ts-node

# Verify installation
tsc --version
ts-node --version
```

#### Useful NVM Commands

```bash
nvm ls                    # List installed Node.js versions
nvm ls-remote            # List available Node.js versions (macOS/Linux)
nvm ls available         # List available Node.js versions (Windows)
nvm install 18           # Install Node.js version 18.x
nvm use 18               # Switch to Node.js version 18.x
nvm current              # Show currently active version
nvm uninstall 16         # Uninstall Node.js version 16.x
```

### Verify Installation
```bash
node --version        # Should show v18.x.x or higher
npm --version         # Should show 9.x.x or higher
tsc --version         # TypeScript compiler
ts-node --version     # TypeScript execution environment
```

## What is TypeScript?

TypeScript is JavaScript with **type annotations**:

```typescript
// JavaScript
function add(a, b) {
    return a + b;
}

// TypeScript
function add(a: number, b: number): number {
    return a + b;
}
```

Key differences:
- `.ts` files (TypeScript) vs `.js` files (JavaScript)
- Type annotations (optional but recommended)
- Compiles to JavaScript before running
- All JavaScript code is valid TypeScript

## Course Structure

The crash course is divided into 12 lessons in TypeScript (`.ts` files):

1. **01_variables_and_datatypes.ts** - Variables, types, type annotations, type inference
2. **02_operators.ts** - Arithmetic, comparison, logical operators, nullish coalescing
3. **03_control_flow.ts** - if/else, switch statements, truthy/falsy values
4. **04_loops.ts** - for, while, do-while, for...of, for...in loops
5. **05_arrays.ts** - Arrays, methods, map/filter/reduce, multi-dimensional arrays
6. **06_sets.ts** - Sets and set operations
7. **07_objects.ts** - Objects, Maps, interfaces, key-value pairs
8. **08_functions.ts** - Functions, arrow functions, types, callbacks
9. **09_strings.ts** - String manipulation, template literals, methods
10. **10_input_output.ts** - Console I/O, readline, Node.js basics
11. **11_references.ts** - References, mutability, shallow vs deep copy
12. **12_practice_exercises.ts** - Hands-on practice problems

## Project Setup

### Initialize TypeScript Project

1. **Navigate to the code folder:**
   ```bash
   cd code/day-3/js
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

This installs:
- TypeScript compiler (`typescript`)
- TypeScript execution (`ts-node`)
- Node.js type definitions (`@types/node`)

### Configuration Files

**package.json** - Project configuration and dependencies
**tsconfig.json** - TypeScript compiler options

Both are already set up in the project!

## How to Run TypeScript Files

### Method 1: Using ts-node (Recommended for Learning)

Run TypeScript files directly without compiling:

```bash
cd code/day-3/js

# Run any TypeScript file
ts-node 01_variables_and_datatypes.ts
ts-node 02_operators.ts
ts-node 03_control_flow.ts
# ... etc
```

### Method 2: Compile then Run

Compile TypeScript to JavaScript, then run:

```bash
# Compile a single file
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

### Method 4: Using VS Code

1. **Open the TypeScript file** in VS Code
2. **Open integrated terminal** (`` Ctrl+` ``)
3. **Run:**
   ```bash
   ts-node 01_variables_and_datatypes.ts
   ```

Or install the **Code Runner** extension and click the ▶️ run button!

## Learning Path

### Recommended Order

Follow this sequence for best learning:

1. Start with **01_variables_and_datatypes.ts** - Understand types and annotations
2. Move to **02_operators.ts** - Learn JavaScript operators
3. Study **03_control_flow.ts** - Master decision making
4. Practice **04_loops.ts** - Learn iteration patterns
5. Explore **05_arrays.ts** - Work with array methods
6. Learn **06_sets.ts** - Unique collections
7. Understand **07_objects.ts** - Key-value structures and Maps
8. Master **08_functions.ts** - Functions and arrow syntax
9. Study **09_strings.ts** - Text manipulation
10. Try **10_input_output.ts** - Console and Node.js I/O
11. Deep dive into **11_references.ts** - Memory management
12. Challenge yourself with **12_practice_exercises.ts**

### Learning Tips

- **Compare with Python** - Notice similarities and differences
- **Run every example** - See how TypeScript catches errors
- **Experiment with types** - Try removing type annotations
- **Use VS Code** - Get full IntelliSense support
- **Check errors** - TypeScript highlights mistakes before running

## TypeScript vs JavaScript vs Python

| Feature | Python | JavaScript | TypeScript |
|---------|--------|------------|------------|
| File Extension | `.py` | `.js` | `.ts` |
| Typing | Dynamic | Dynamic | Static (optional) |
| Semicolons | No | Optional | Optional |
| Arrays | Lists | Arrays | Typed Arrays |
| Dictionaries | dict | Object/Map | Object/Map |
| Functions | def | function | function + types |
| Classes | Yes | Yes | Yes + interfaces |

## Common TypeScript Concepts

### Type Annotations
```typescript
let name: string = "Alice";
let age: number = 25;
let isStudent: boolean = true;
```

### Interfaces
```typescript
interface Person {
    name: string;
    age: number;
}

const person: Person = { name: "Alice", age: 25 };
```

### Union Types
```typescript
let id: number | string;
id = 123;      // OK
id = "ABC123"; // OK
```

### Type Inference
```typescript
let x = 5;  // TypeScript infers x is number
```

## Assignments

The same coding assignments work for both Python and TypeScript! Check:
- `assignments/day-3/js/` folder

These assignments are language-agnostic and help you practice core programming concepts.

## Troubleshooting

### "tsc: command not found"
```bash
npm install -g typescript
```

### "ts-node: command not found"
```bash
npm install -g ts-node
```

### Module not found errors
```bash
cd code/day-3/js
npm install
```

### VS Code TypeScript Errors
1. Install **TypeScript** extension
2. Reload VS Code
3. Check `tsconfig.json` is present

### Permission Errors (Linux/Mac/WSL)
If using NVM, you shouldn't need sudo. If you do:
```bash
sudo npm install -g typescript ts-node
```

**Better solution:** Reinstall Node.js via NVM (see installation section above) to avoid permission issues.

## Next Steps

After completing this crash course:

1. ✅ Complete all 12 TypeScript lessons
2. ✅ Compare with Python equivalents
3. ✅ Solve assignment problems in both languages
4. ✅ Build a small project in TypeScript
5. ✅ Explore advanced TypeScript features (generics, decorators)

## Key Concepts Covered

- ✨ Variables and type annotations
- ✨ Operators and expressions
- ✨ Control flow (if/else, switch)
- ✨ Loops (for, while, for...of)
- ✨ Arrays and array methods
- ✨ Sets and Maps
- ✨ Objects and interfaces
- ✨ Functions and arrow functions
- ✨ String manipulation
- ✨ Input/Output with Node.js
- ✨ References and memory management
- ✨ Problem-solving with code

## Resources

- **Official TypeScript Docs:** [typescriptlang.org](https://www.typescriptlang.org/docs/)
- **TypeScript Playground:** [typescriptlang.org/play](https://www.typescriptlang.org/play)
- **MDN JavaScript:** [developer.mozilla.org](https://developer.mozilla.org/)
- **Node.js Docs:** [nodejs.org/docs](https://nodejs.org/docs)

## Remember

> "TypeScript is JavaScript with superpowers!" 

Compare both Python and TypeScript versions to understand programming concepts deeply. Each language has its strengths - Python for simplicity and readability, TypeScript for type safety and JavaScript ecosystem integration.

Happy coding! 🚀

