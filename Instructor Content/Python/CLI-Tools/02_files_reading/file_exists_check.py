#!/usr/bin/env python3
# Checking if files exist before reading

import os
from pathlib import Path

"""
CHECK FILE EXISTENCE:

Method 1: os.path.exists()
Method 2: Path.exists() (pathlib)
Method 3: try/except FileNotFoundError

Always check before reading to avoid errors!
"""

# Create test files
with open('exists.txt', 'w') as f:
    f.write("This file exists\n")

# Method 1: Using os.path
print("Method 1: os.path.exists()")
print("-" * 40)

if os.path.exists('exists.txt'):
    print("✓ exists.txt found")
    with open('exists.txt', 'r') as f:
        print(f"  Content: {f.read().strip()}")
else:
    print("✗ File not found")

if os.path.exists('missing.txt'):
    print("✓ missing.txt found")
else:
    print("✗ missing.txt not found")

# Method 2: Using pathlib
print("\nMethod 2: pathlib.Path.exists()")
print("-" * 40)

file_path = Path('exists.txt')
if file_path.exists():
    print(f"✓ {file_path} exists")
    print(f"  Is file: {file_path.is_file()}")
    print(f"  Is directory: {file_path.is_dir()}")
    print(f"  Size: {file_path.stat().st_size} bytes")

# Method 3: try/except (Pythonic way)
print("\nMethod 3: try/except (EAFP - Easier to Ask for Forgiveness)")
print("-" * 40)

try:
    with open('exists.txt', 'r') as f:
        content = f.read()
        print("✓ File opened successfully")
except FileNotFoundError:
    print("✗ File not found")

# Example 4: Check multiple file properties
print("\nExample 4: File properties")
print("-" * 40)

filename = 'exists.txt'

if os.path.exists(filename):
    print(f"File: {filename}")
    print(f"  Exists: {os.path.exists(filename)}")
    print(f"  Is file: {os.path.isfile(filename)}")
    print(f"  Is directory: {os.path.isdir(filename)}")
    print(f"  Readable: {os.access(filename, os.R_OK)}")
    print(f"  Writable: {os.access(filename, os.W_OK)}")
    print(f"  Size: {os.path.getsize(filename)} bytes")

# Example 5: Practical function
print("\nExample 5: Safe file reader")
print("-" * 40)

def read_file_safely(filename):
    """Safely read file with existence check"""
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found")
        return None
    
    if not os.path.isfile(filename):
        print(f"Error: '{filename}' is not a file")
        return None
    
    if not os.access(filename, os.R_OK):
        print(f"Error: No read permission for '{filename}'")
        return None
    
    try:
        with open(filename, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Test the function
content = read_file_safely('exists.txt')
if content:
    print(f"Read {len(content)} characters")

content = read_file_safely('missing.txt')
if not content:
    print("Could not read file")

print("\nBest practice:")
print("  Use try/except for file operations (EAFP)")
print("  Or check existence first (LBYL)")
print("  EAFP = Easier to Ask for Forgiveness than Permission")
print("  LBYL = Look Before You Leap")
