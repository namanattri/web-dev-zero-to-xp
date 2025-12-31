# Day 3: Python Crash Course

## Overview
Welcome to Day 3! Today you'll learn Python fundamentals - the core 20% that covers 80% of what you need to know. This crash course focuses on building solid coding logic and language basics.

## Prerequisites

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
1. Download from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. ✅ **IMPORTANT:** Check "Add Python to PATH" during installation

**On Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Verify Installation
```bash
python3 --version
pip3 --version
```

## Course Structure

The crash course is divided into 10 lessons, each in its own file:

1. **01_variables_and_datatypes.py** - Variables, strings, numbers, booleans, type conversion
2. **02_operators.py** - Arithmetic, comparison, logical, and assignment operators
3. **03_control_flow.py** - if/elif/else statements, decision making
4. **04_loops.py** - for loops, while loops, break, continue
5. **05_lists.py** - Lists, list operations, slicing, comprehensions
6. **06_dictionaries.py** - Dictionaries, key-value pairs, nested structures
7. **07_functions.py** - Defining functions, parameters, return values
8. **08_strings.py** - String manipulation, formatting, methods
9. **09_input_output.py** - User input, output formatting, basic I/O
10. **10_practice_exercises.py** - Hands-on practice problems

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

**On macOS/Linux:**
```bash
cd ~/Projects/ps/web-dev-zero-to-xp/code/day-3
python3 01_variables_and_datatypes.py
```

**On Windows:**
```bash
cd C:\Projects\ps\web-dev-zero-to-xp\code\day-3
python 01_variables_and_datatypes.py
```

## Learning Path

### Recommended Order

Follow this sequence for best learning:

1. Start with **01_variables_and_datatypes.py** - Understand the basics
2. Move to **02_operators.py** - Learn to manipulate data
3. Study **03_control_flow.py** - Master decision making
4. Practice **04_loops.py** - Learn repetition and iteration
5. Explore **05_lists.py** - Work with collections
6. Understand **06_dictionaries.py** - Key-value data structures
7. Learn **07_functions.py** - Write reusable code
8. Master **08_strings.py** - Text manipulation
9. Try **09_input_output.py** - User interaction
10. Challenge yourself with **10_practice_exercises.py**

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
- **On Windows:** Use `python` instead of `python3`
- **On Mac/Linux:** Python 3 might not be installed. Install using package manager.

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

1. ✅ Complete all 10 lessons
2. ✅ Solve all practice exercises
3. ✅ Build a small project using what you learned
4. ✅ Review concepts you found challenging

## Key Concepts Covered

- ✨ Variables and data types
- ✨ Operators and expressions
- ✨ Control flow (if/else)
- ✨ Loops (for/while)
- ✨ Lists and list operations
- ✨ Dictionaries
- ✨ Functions
- ✨ String manipulation
- ✨ Input/Output
- ✨ Problem-solving with code

## Resources

- **Official Python Docs:** [docs.python.org](https://docs.python.org/3/)
- **Python Tutorial:** [python.org/tutorial](https://docs.python.org/3/tutorial/)
- **Practice Problems:** [leetcode.com](https://leetcode.com), [hackerrank.com](https://www.hackerrank.com)

## Remember

> "The only way to learn a new programming language is by writing programs in it." - Dennis Ritchie

Start with lesson 1 and work your way through. Take your time, experiment, and most importantly - have fun coding! 🚀

