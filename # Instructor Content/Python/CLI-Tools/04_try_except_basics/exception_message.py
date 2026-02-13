#!/usr/bin/env python3
# Getting exception messages

"""
ACCESSING EXCEPTION DETAILS:

except ExceptionType as e:
    print(e)              # Error message
    print(type(e))        # Exception type
    print(str(e))         # String representation
    print(repr(e))        # Full representation

USEFUL FOR:
- Logging
- Debugging
- User feedback
"""

# Example 1: Basic error message
print("Example 1: Accessing error message")
print("-" * 40)

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error message: {e}")
    print(f"Error type: {type(e).__name__}")

# Example 2: File error details
print("\nExample 2: File operation errors")
print("-" * 40)

try:
    with open('/invalid/path/file.txt', 'r') as f:
        data = f.read()
except FileNotFoundError as e:
    print(f"Error occurred: {e}")
    print(f"Error type: {type(e).__name__}")

# Example 3: Value error details
print("\nExample 3: Conversion errors")
print("-" * 40)

test_values = ["42", "abc", "3.14", "not_a_number"]

for value in test_values:
    try:
        number = int(value)
        print(f"✓ '{value}' → {number}")
    except ValueError as e:
        print(f"✗ '{value}' → Error: {e}")

# Example 4: JSON error details
print("\nExample 4: JSON parsing errors")
print("-" * 40)

import json

invalid_json = '{"name": "test", invalid}'

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"JSON Error: {e}")
    print(f"Position: line {e.lineno}, column {e.colno}")
    print(f"Message: {e.msg}")

# Example 5: Detailed error logging
print("\nExample 5: Error logging function")
print("-" * 40)

import datetime

def log_error(operation, error):
    """Log error with full details"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    error_log = f"""
[{timestamp}] ERROR in {operation}
  Type: {type(error).__name__}
  Message: {str(error)}
  Details: {repr(error)}
"""
    print(error_log)
    # Could write to file here

try:
    with open('missing.txt', 'r') as f:
        data = f.read()
except FileNotFoundError as e:
    log_error("read_config_file", e)

# Example 6: Custom error messages
print("Example 6: User-friendly error messages")
print("-" * 40)

def safe_file_read(filename):
    """Read file with user-friendly errors"""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError as e:
        user_msg = f"File '{filename}' not found"
        tech_msg = f"Technical: {e}"
        print(f"✗ {user_msg}")
        print(f"  {tech_msg}")
        return None
    except PermissionError as e:
        user_msg = f"Cannot access '{filename}' (permission denied)"
        tech_msg = f"Technical: {e}"
        print(f"✗ {user_msg}")
        print(f"  {tech_msg}")
        return None

content = safe_file_read('/root/protected.txt')

# Example 7: Error context
print("\nExample 7: Error with context")
print("-" * 40)

def divide_with_context(a, b):
    """Division with context"""
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        print(f"Context: Tried to divide {a} by {b}")
        print(f"Suggestion: Make sure denominator is not zero")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        print(f"Context: a={a} (type: {type(a).__name__}), b={b} (type: {type(b).__name__})")
        print(f"Suggestion: Both arguments must be numbers")
        return None

result = divide_with_context(10, 0)
result = divide_with_context(10, "x")

# Example 8: Stack trace
print("\nExample 8: Full stack trace (debugging)")
print("-" * 40)

import traceback

def level3():
    return 10 / 0

def level2():
    return level3()

def level1():
    return level2()

try:
    level1()
except ZeroDivisionError as e:
    print("Error caught:")
    print(f"  Message: {e}")
    print("\nFull traceback:")
    traceback.print_exc()

print("\nKey points:")
print("  ✓ Use 'as e' to capture exception")
print("  ✓ str(e) for error message")
print("  ✓ type(e).__name__ for exception type")
print("  ✓ Provide context with error")
print("  ✓ User-friendly vs technical messages")
