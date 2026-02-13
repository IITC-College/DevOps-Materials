#!/usr/bin/env python3
# Writing with context manager

"""
CONTEXT MANAGER FOR WRITING:

Always use 'with' statement:
- Automatically closes file
- Even if exception occurs
- Ensures data is flushed
- Clean and safe
"""

# Example 1: Basic write with context manager
print("Example 1: Basic write")
print("-" * 40)

with open('output.txt', 'w') as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")
# File automatically closed here

print("✓ File written and closed")

# Example 2: Exception still closes file
print("\nExample 2: Exception handling")
print("-" * 40)

try:
    with open('test.txt', 'w') as f:
        f.write("Before error\n")
        # Simulate error
        # x = 1 / 0  # Uncomment to test
        f.write("After error\n")
except ZeroDivisionError:
    print("Error occurred, but file was still closed")

print("✓ File properly handled")

# Example 3: Multiple files
print("\nExample 3: Writing multiple files")
print("-" * 40)

data = {
    "file1.txt": "Content for file 1",
    "file2.txt": "Content for file 2",
    "file3.txt": "Content for file 3"
}

for filename, content in data.items():
    with open(filename, 'w') as f:
        f.write(content + "\n")
    print(f"✓ Wrote {filename}")

# Example 4: Read from one, write to another
print("\nExample 4: Copy and transform")
print("-" * 40)

# Create source file
with open('source.txt', 'w') as f:
    f.write("hello world\n")
    f.write("python programming\n")
    f.write("file operations\n")

# Read and transform
with open('source.txt', 'r') as input_file:
    with open('destination.txt', 'w') as output_file:
        for line in input_file:
            output_file.write(line.upper())

print("✓ Copied and transformed file")

# Example 5: Safe write with backup
print("\nExample 5: Safe write with backup")
print("-" * 40)

import os

def safe_write(filename, content):
    """Write file with backup"""
    # Create backup if file exists
    if os.path.exists(filename):
        backup = filename + '.bak'
        with open(filename, 'r') as f:
            with open(backup, 'w') as b:
                b.write(f.read())
        print(f"✓ Created backup: {backup}")
    
    # Write new content
    with open(filename, 'w') as f:
        f.write(content)
    print(f"✓ Wrote {filename}")

safe_write('important.txt', 'First version\n')
safe_write('important.txt', 'Second version\n')

# Example 6: Atomic write pattern
print("\nExample 6: Atomic write")
print("-" * 40)

def atomic_write(filename, content):
    """Write to temp file, then rename"""
    temp_file = filename + '.tmp'
    
    # Write to temp file
    with open(temp_file, 'w') as f:
        f.write(content)
    
    # Rename (atomic operation on most systems)
    os.replace(temp_file, filename)
    print(f"✓ Atomically wrote {filename}")

atomic_write('atomic.txt', 'Safely written content\n')

# Example 7: Logging with context manager
print("\nExample 7: Simple logging class")
print("-" * 40)

class Logger:
    def __init__(self, filename):
        self.filename = filename
    
    def log(self, message):
        """Append log message"""
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, 'a') as f:
            f.write(f"[{timestamp}] {message}\n")

logger = Logger('app.log')
logger.log("Application started")
logger.log("Processing data")
logger.log("Task completed")

print("✓ Logged 3 messages")

# Example 8: Buffering demonstration
print("\nExample 8: Flush buffer")
print("-" * 40)

with open('buffered.txt', 'w') as f:
    f.write("Line 1\n")
    f.flush()  # Force write to disk
    f.write("Line 2\n")
    # Automatic flush on close

print("✓ Wrote with explicit flush")

print("\nKey points:")
print("  ✓ Always use 'with' for file writing")
print("  ✓ File closes automatically")
print("  ✓ Exception-safe")
print("  ✓ Data properly flushed")
