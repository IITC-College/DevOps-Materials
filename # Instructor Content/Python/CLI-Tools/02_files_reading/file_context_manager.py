#!/usr/bin/env python3
# Using 'with' statement (context manager)

"""
CONTEXT MANAGER (with statement):

Old way:
  file = open('file.txt', 'r')
  content = file.read()
  file.close()  # MUST remember to close!

New way (BETTER):
  with open('file.txt', 'r') as file:
      content = file.read()
  # Automatically closed!

ADVANTAGES:
- File is automatically closed
- Even if exception occurs
- Cleaner code
- Less chance of errors

ALWAYS USE 'with' STATEMENT!
"""

# Create sample file
with open('test.txt', 'w') as f:
    f.write("Python Context Manager\n")
    f.write("Automatically handles file closing\n")

# Example 1: Basic with statement
print("Example 1: Basic with statement")
print("-" * 40)

with open('test.txt', 'r') as f:
    content = f.read()
    print(content)

# File is automatically closed here
print("File is now closed\n")

# Example 2: Exception handling with context manager
print("Example 2: File closes even with exceptions")
print("-" * 40)

try:
    with open('test.txt', 'r') as f:
        content = f.read()
        # Simulate an error
        # result = 1 / 0  # Uncomment to test
        print(content)
except ZeroDivisionError:
    print("Error occurred!")
# File is still properly closed!

# Example 3: Multiple files
print("\nExample 3: Opening multiple files")
print("-" * 40)

with open('file1.txt', 'w') as f1, open('file2.txt', 'w') as f2:
    f1.write("Content of file 1\n")
    f2.write("Content of file 2\n")

print("Both files written and closed")

# Example 4: Nested with statements
print("\nExample 4: Reading one file, writing to another")
print("-" * 40)

with open('test.txt', 'r') as input_file:
    with open('output.txt', 'w') as output_file:
        for line in input_file:
            output_file.write(line.upper())

print("File copied with uppercase transformation")

# Verify the file is closed
with open('test.txt', 'r') as f:
    print(f"\nFile object inside with: {f.closed}")  # False

print(f"File object outside with: {f.closed}")  # True

print("\n✓ Always use 'with' statement for file operations!")
