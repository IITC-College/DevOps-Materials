#!/usr/bin/env python3
# Writing files basics

"""
WRITING FILES:

Basic syntax:
  with open('filename.txt', 'w') as f:
      f.write('content')

MODES:
  'w'  = write (creates new or overwrites)
  'a'  = append (adds to end)
  'x'  = exclusive create (fails if exists)
"""

# Example 1: Basic write
print("Example 1: Basic file writing")
print("-" * 40)

with open('output.txt', 'w') as f:
    f.write("Hello, World!\n")
    f.write("This is line 2\n")
    f.write("This is line 3\n")

print("✓ Created output.txt")

# Read it back to verify
with open('output.txt', 'r') as f:
    content = f.read()
    print("Content:")
    print(content)

# Example 2: write() returns number of characters written
print("\nExample 2: write() return value")
print("-" * 40)

with open('test.txt', 'w') as f:
    chars_written = f.write("Python")
    print(f"Wrote {chars_written} characters")

# Example 3: Writing multiple lines with writelines()
print("\nExample 3: writelines()")
print("-" * 40)

lines = [
    "Line 1\n",
    "Line 2\n",
    "Line 3\n"
]

with open('lines.txt', 'w') as f:
    f.writelines(lines)

print("✓ Wrote multiple lines")

# Example 4: Writing overwrites existing content
print("\nExample 4: 'w' mode overwrites")
print("-" * 40)

with open('overwrite.txt', 'w') as f:
    f.write("First content\n")

print("First write: 'First content'")

with open('overwrite.txt', 'w') as f:
    f.write("Second content\n")

print("Second write: 'Second content'")

with open('overwrite.txt', 'r') as f:
    print(f"Final content: {f.read().strip()}")

# Example 5: Write formatted strings
print("\nExample 5: Write formatted data")
print("-" * 40)

name = "DevOps"
version = 2.0
count = 42

with open('formatted.txt', 'w') as f:
    f.write(f"Application: {name}\n")
    f.write(f"Version: {version}\n")
    f.write(f"Count: {count}\n")

print("✓ Wrote formatted data")

with open('formatted.txt', 'r') as f:
    print("Content:")
    print(f.read())

print("Key points:")
print("  ✓ 'w' mode creates or overwrites")
print("  ✓ write() for single string")
print("  ✓ writelines() for list of strings")
print("  ✓ Always use 'with' statement")
