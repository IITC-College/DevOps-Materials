#!/usr/bin/env python3
# Understanding stdin, stdout, stderr

"""
STANDARD STREAMS IN CLI:

Every process has three standard streams:

1. STDIN (Standard Input) - File descriptor 0
   - Input to the program
   - Default: keyboard
   - Can be redirected from file or pipe

2. STDOUT (Standard Output) - File descriptor 1
   - Normal output from the program
   - Default: terminal screen
   - Can be redirected to file or pipe

3. STDERR (Standard Error) - File descriptor 2
   - Error messages and warnings
   - Default: terminal screen (usually)
   - Can be redirected separately from stdout

WHY THREE STREAMS?

Separation of concerns:
- stdout: Data/results
- stderr: Errors/warnings
- stdin: User input

This allows flexible I/O redirection

EXAMPLES IN BASH:

# Redirect stdout to file
mytool > output.txt

# Redirect stderr to file
mytool 2> errors.txt

# Redirect both
mytool > output.txt 2> errors.txt

# Redirect both to same file
mytool > all.txt 2>&1

# Pipe stdout to another command
mytool | grep "pattern"

# Read from file instead of keyboard
mytool < input.txt

# Chain commands
cat data.txt | mytool | sort | uniq

PYTHON USAGE:

import sys

# Write to stdout (normal)
print("This is normal output")
sys.stdout.write("Normal output\n")

# Write to stderr (errors)
print("Error occurred!", file=sys.stderr)
sys.stderr.write("Error: something wrong\n")

# Read from stdin
line = sys.stdin.readline()
for line in sys.stdin:
    process(line)

PRACTICAL EXAMPLE:

#!/usr/bin/env python3
import sys

def process_data():
    # Normal output to stdout
    print("Processing data...")
    print("Result: 42")
    
    # Errors to stderr
    if error_condition:
        print("Warning: low memory", file=sys.stderr)

# Usage:
# python tool.py > results.txt 2> errors.log
# Normal output → results.txt
# Errors → errors.log

PIPES:

Send output of one program to input of another:

# Count lines in output
mytool | wc -l

# Filter results
mytool | grep "ERROR"

# Chain multiple tools
cat data.csv | mytool process | sort | uniq

BEST PRACTICES:

1. Use stdout for data/results
2. Use stderr for errors/warnings
3. Use stdin to read input when provided
4. Support both arguments and stdin:
   mytool file.txt         # Read from file
   cat file.txt | mytool   # Read from stdin

5. Don't mix data and errors in stdout
6. Use logging for debugging (not stdout/stderr)

CHECKING STREAMS IN PYTHON:

import sys

# Is stdout redirected?
if sys.stdout.isatty():
    print("Outputting to terminal")
else:
    print("Outputting to file or pipe")

# Is stdin from terminal or pipe?
if sys.stdin.isatty():
    # Interactive mode
    name = input("Enter name: ")
else:
    # Reading from pipe
    for line in sys.stdin:
        process(line)
"""

import sys

print("Standard streams:")
print(f"  stdin:  {sys.stdin}")
print(f"  stdout: {sys.stdout}")
print(f"  stderr: {sys.stderr}")
print()
print("Normal output goes to stdout")
print("Errors go to stderr:", file=sys.stderr)
print()
print("Try: python this_script.py > output.txt 2> errors.txt")
