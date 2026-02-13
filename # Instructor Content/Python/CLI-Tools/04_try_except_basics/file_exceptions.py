#!/usr/bin/env python3
# File-related exceptions

"""
FILE EXCEPTIONS:

FileNotFoundError     - File doesn't exist
PermissionError       - No permission to access
IsADirectoryError     - Expected file, got directory
FileExistsError       - File already exists (with 'x' mode)
IOError               - General I/O error
OSError               - OS-level error

All file operations should be wrapped in try/except!
"""

import os

# Example 1: FileNotFoundError
print("Example 1: File not found")
print("-" * 40)

try:
    with open('nonexistent.txt', 'r') as f:
        data = f.read()
except FileNotFoundError as e:
    print(f"✗ File not found: {e}")
    print("Action: Check if file exists before opening")

# Example 2: PermissionError
print("\nExample 2: Permission denied")
print("-" * 40)

# Create a file
with open('test_perms.txt', 'w') as f:
    f.write("test")

# Try to open protected location (simulated)
try:
    with open('/root/protected.txt', 'w') as f:
        f.write("data")
except (PermissionError, OSError) as e:
    print(f"✗ Permission denied: {e}")
    print("Action: Check file permissions or use different location")

# Example 3: IsADirectoryError
print("\nExample 3: Is a directory")
print("-" * 40)

# Create a directory
os.makedirs('test_dir', exist_ok=True)

try:
    with open('test_dir', 'r') as f:
        data = f.read()
except IsADirectoryError as e:
    print(f"✗ Cannot read directory as file: {e}")
    print("Action: Use os.listdir() for directories")

# Example 4: FileExistsError
print("\nExample 4: File already exists")
print("-" * 40)

# Create file
with open('existing.txt', 'w') as f:
    f.write("content")

# Try to create with 'x' mode
try:
    with open('existing.txt', 'x') as f:
        f.write("new content")
except FileExistsError as e:
    print(f"✗ File already exists: {e}")
    print("Action: Use 'w' to overwrite or check existence first")

# Example 5: Complete file operation handler
print("\nExample 5: Complete error handling")
print("-" * 40)

def safe_read_file(filename):
    """Read file with comprehensive error handling"""
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"✓ Read {len(content)} characters from {filename}")
            return content
    except FileNotFoundError:
        print(f"✗ File '{filename}' not found")
        print(f"  Suggestion: Check filename and path")
    except PermissionError:
        print(f"✗ Permission denied for '{filename}'")
        print(f"  Suggestion: Check file permissions")
    except IsADirectoryError:
        print(f"✗ '{filename}' is a directory, not a file")
        print(f"  Suggestion: Use os.listdir() for directories")
    except UnicodeDecodeError:
        print(f"✗ '{filename}' contains non-text data")
        print(f"  Suggestion: Open in binary mode ('rb')")
    except IOError as e:
        print(f"✗ I/O error: {e}")
        print(f"  Suggestion: Check disk space and permissions")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
    
    return None

# Test various scenarios
safe_read_file('existing.txt')
safe_read_file('missing.txt')
safe_read_file('test_dir')

# Example 6: Write operations
print("\nExample 6: Write operation errors")
print("-" * 40)

def safe_write_file(filename, content):
    """Write file with error handling"""
    try:
        with open(filename, 'w') as f:
            f.write(content)
            print(f"✓ Wrote {len(content)} characters to {filename}")
            return True
    except PermissionError:
        print(f"✗ Cannot write to '{filename}' (permission denied)")
    except IsADirectoryError:
        print(f"✗ '{filename}' is a directory")
    except OSError as e:
        print(f"✗ OS error: {e}")
    
    return False

safe_write_file('output.txt', "Hello, World!")
safe_write_file('/root/output.txt', "Hello")

# Example 7: Check before operation
print("\nExample 7: Defensive file operations")
print("-" * 40)

def defensive_read(filename):
    """Check conditions before reading"""
    # Check exists
    if not os.path.exists(filename):
        print(f"✗ File doesn't exist: {filename}")
        return None
    
    # Check is file
    if not os.path.isfile(filename):
        print(f"✗ Not a file: {filename}")
        return None
    
    # Check readable
    if not os.access(filename, os.R_OK):
        print(f"✗ No read permission: {filename}")
        return None
    
    # Now safe to read
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"✓ Read {filename} successfully")
            return content
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return None

defensive_read('existing.txt')
defensive_read('missing.txt')

# Example 8: Practical logging
print("\nExample 8: Error logging to file")
print("-" * 40)

import datetime

def log_file_error(operation, filename, error):
    """Log file errors"""
    try:
        with open('file_errors.log', 'a') as f:
            timestamp = datetime.datetime.now().isoformat()
            log_entry = f"[{timestamp}] {operation} on '{filename}': {type(error).__name__} - {error}\n"
            f.write(log_entry)
            print("✓ Error logged")
    except Exception as e:
        print(f"Could not log error: {e}")

try:
    with open('missing.txt', 'r') as f:
        data = f.read()
except FileNotFoundError as e:
    print(f"Error: {e}")
    log_file_error("read", "missing.txt", e)

print("\nBest practices:")
print("  ✓ Always wrap file operations in try/except")
print("  ✓ Handle specific file exceptions")
print("  ✓ Provide actionable error messages")
print("  ✓ Check conditions before operations")
print("  ✓ Log errors for debugging")
