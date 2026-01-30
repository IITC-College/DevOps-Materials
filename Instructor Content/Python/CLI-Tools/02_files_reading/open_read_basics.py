#!/usr/bin/env python3
# File reading basics with open()

"""
OPENING AND READING FILES:

Basic syntax:
  file = open('filename.txt', 'r')  # 'r' = read mode
  content = file.read()
  file.close()

MODES:
  'r'  = read (default)
  'w'  = write (overwrites)
  'a'  = append
  'r+' = read and write

ALWAYS CLOSE FILES!
Either manually or with 'with' statement
"""

# Example 1: Basic file reading
print("Example 1: Basic file reading")
print("-" * 40)

# Create a sample file first
with open('sample.txt', 'w') as f:
    f.write("Line 1: Hello\n")
    f.write("Line 2: World\n")
    f.write("Line 3: Python\n")

# Read the file
file = open('sample.txt', 'r')
content = file.read()
file.close()

print("File content:")
print(content)

# Example 2: Check if file exists before opening
print("\nExample 2: Safe file opening")
print("-" * 40)

import os

filename = 'data.txt'
if os.path.exists(filename):
    file = open(filename, 'r')
    content = file.read()
    file.close()
    print(f"Read {len(content)} characters from {filename}")
else:
    print(f"File {filename} does not exist")

# Example 3: Better approach with try/except
print("\nExample 3: Error handling")
print("-" * 40)

try:
    file = open('nonexistent.txt', 'r')
    content = file.read()
    file.close()
    print(content)
except FileNotFoundError:
    print("Error: File not found")

print("\nKey points:")
print("  1. open() returns a file object")
print("  2. Always close files after opening")
print("  3. Use 'r' mode for reading")
print("  4. Check if file exists first")
