#!/usr/bin/env python3
# File operations summary

"""
FILE OPERATIONS SUMMARY

READING:
  with open('file.txt', 'r') as f:
      content = f.read()          # Entire file
      line = f.readline()         # One line
      lines = f.readlines()       # List of lines
      for line in f:              # Iterator (best for large files)

WRITING:
  with open('file.txt', 'w') as f:
      f.write('content')          # Overwrites file
      f.writelines(list)          # Write list of strings

APPENDING:
  with open('file.txt', 'a') as f:
      f.write('content')          # Add to end

MODES:
  'r'   Read (default)
  'w'   Write (overwrite)
  'a'   Append
  'x'   Exclusive create
  'r+'  Read and write
  'b'   Binary mode
  't'   Text mode (default)

FILE EXISTENCE:
  os.path.exists(file)
  Path(file).exists()

FILE INFO:
  os.path.getsize(file)
  os.path.isfile(file)
  os.path.isdir(file)
"""

import os
import json
from pathlib import Path

print("COMPREHENSIVE FILE OPERATIONS DEMO")
print("=" * 50)

# 1. CREATE AND WRITE
print("\n1. Creating files")
print("-" * 40)

with open('demo.txt', 'w') as f:
    f.write("This is a text file\n")
    f.write("Second line\n")

print("✓ Created demo.txt")

# 2. READ
print("\n2. Reading files")
print("-" * 40)

with open('demo.txt', 'r') as f:
    content = f.read()
    print(f"Content ({len(content)} chars):\n{content}")

# 3. APPEND
print("3. Appending to file")
print("-" * 40)

with open('demo.txt', 'a') as f:
    f.write("Third line (appended)\n")

print("✓ Appended to demo.txt")

# 4. CHECK EXISTENCE
print("\n4. Checking file existence")
print("-" * 40)

files = ['demo.txt', 'missing.txt']
for filename in files:
    exists = os.path.exists(filename)
    print(f"  {filename}: {'✓ exists' if exists else '✗ not found'}")

# 5. FILE INFO
print("\n5. File information")
print("-" * 40)

if os.path.exists('demo.txt'):
    size = os.path.getsize('demo.txt')
    is_file = os.path.isfile('demo.txt')
    print(f"  Size: {size} bytes")
    print(f"  Is file: {is_file}")

# 6. JSON OPERATIONS
print("\n6. JSON file operations")
print("-" * 40)

config = {
    "app": "DevOps Helper",
    "version": 2.0,
    "settings": {
        "debug": False,
        "port": 8080
    }
}

# Write JSON
with open('config.json', 'w') as f:
    json.dump(config, f, indent=2)

print("✓ Wrote JSON file")

# Read JSON
with open('config.json', 'r') as f:
    loaded_config = json.load(f)
    print(f"  Loaded: {loaded_config['app']} v{loaded_config['version']}")

# 7. LINE-BY-LINE PROCESSING
print("\n7. Line-by-line processing")
print("-" * 40)

line_count = 0
with open('demo.txt', 'r') as f:
    for line in f:
        line_count += 1
        print(f"  Line {line_count}: {line.strip()}")

# 8. SAFE OPERATIONS
print("\n8. Safe file operations")
print("-" * 40)

def safe_read(filename):
    """Safely read file"""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

content = safe_read('demo.txt')
print(f"✓ Read {len(content)} chars" if content else "✗ Failed")

content = safe_read('missing.txt')
print("✓ Read success" if content else "✗ File not found")

# 9. PATHLIB USAGE
print("\n9. Using pathlib")
print("-" * 40)

path = Path('demo.txt')
print(f"  Exists: {path.exists()}")
print(f"  Is file: {path.is_file()}")
print(f"  Name: {path.name}")
print(f"  Suffix: {path.suffix}")
print(f"  Parent: {path.parent}")

# 10. PRACTICAL LOGGING FUNCTION
print("\n10. Practical logging")
print("-" * 40)

import datetime

def log(message, level="INFO", logfile="app.log"):
    """Simple logging function"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] [{level}] {message}\n"
    with open(logfile, 'a') as f:
        f.write(log_line)

log("System started")
log("Processing data")
log("Warning: High memory", level="WARNING")
log("Operation completed")

print("✓ Logged 4 messages")

# SUMMARY
print("\n" + "=" * 50)
print("FILE OPERATIONS QUICK REFERENCE")
print("=" * 50)
print("""
READ:     with open('file.txt', 'r') as f: content = f.read()
WRITE:    with open('file.txt', 'w') as f: f.write(content)
APPEND:   with open('file.txt', 'a') as f: f.write(content)
JSON:     json.dump(data, f) / json.load(f)
EXISTS:   os.path.exists('file.txt')
SIZE:     os.path.getsize('file.txt')

✓ Always use 'with' statement
✓ Handle exceptions
✓ Close files (automatic with 'with')
""")
