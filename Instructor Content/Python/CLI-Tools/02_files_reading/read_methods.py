#!/usr/bin/env python3
# Different read methods

"""
FILE READING METHODS:

1. read()       - Read entire file as single string
2. readline()   - Read one line at a time
3. readlines()  - Read all lines into a list
"""

# Create sample file
with open('demo.txt', 'w') as f:
    f.write("First line\n")
    f.write("Second line\n")
    f.write("Third line\n")
    f.write("Fourth line\n")

# Method 1: read() - entire file
print("Method 1: read() - entire file")
print("-" * 40)
with open('demo.txt', 'r') as f:
    content = f.read()
    print(f"Type: {type(content)}")
    print(f"Content:\n{content}")

# Method 2: read(n) - read n characters
print("\nMethod 2: read(n) - first 10 characters")
print("-" * 40)
with open('demo.txt', 'r') as f:
    content = f.read(10)
    print(f"Content: '{content}'")

# Method 3: readline() - one line
print("\nMethod 3: readline() - one line at a time")
print("-" * 40)
with open('demo.txt', 'r') as f:
    line1 = f.readline()
    line2 = f.readline()
    print(f"First line: {line1.strip()}")
    print(f"Second line: {line2.strip()}")

# Method 4: readlines() - all lines as list
print("\nMethod 4: readlines() - all lines as list")
print("-" * 40)
with open('demo.txt', 'r') as f:
    lines = f.readlines()
    print(f"Type: {type(lines)}")
    print(f"Number of lines: {len(lines)}")
    for i, line in enumerate(lines, 1):
        print(f"  Line {i}: {line.strip()}")

# Method 5: Iterate over file object (BEST for large files)
print("\nMethod 5: Iterate over file (memory efficient)")
print("-" * 40)
with open('demo.txt', 'r') as f:
    for line_num, line in enumerate(f, 1):
        print(f"  {line_num}: {line.strip()}")

print("\nComparison:")
print("  read()      → Single string, entire file")
print("  readline()  → One line, call multiple times")
print("  readlines() → List of lines, all at once")
print("  for line in f: → Iterator, memory efficient")
