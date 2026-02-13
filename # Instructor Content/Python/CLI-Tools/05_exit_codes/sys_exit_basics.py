#!/usr/bin/env python3
# sys.exit() basics

import sys

"""
EXIT CODES:

sys.exit(0)    - Success
sys.exit(1)    - General error
sys.exit(N)    - Specific error codes

WHY EXIT CODES:
- Scripts can check if operation succeeded
- Automation can handle failures
- Standard communication with shell
- CI/CD pipelines use them

CHECK EXIT CODE IN BASH:
  python script.py
  echo $?    # Shows exit code
"""

# Example 1: Successful exit
print("Example 1: Successful exit")
print("-" * 40)

def example_success():
    """Function that exits successfully"""
    print("Operation completed successfully")
    sys.exit(0)  # Exit with success code

# Uncomment to test:
# example_success()
# print("This won't print")

# Example 2: Error exit
print("Example 2: Error exit")
print("-" * 40)

def example_error():
    """Function that exits with error"""
    print("Error occurred!")
    sys.exit(1)  # Exit with error code

# Uncomment to test:
# example_error()
# print("This won't print either")

# Example 3: Different exit codes
print("Example 3: Specific exit codes")
print("-" * 40)

EXIT_SUCCESS = 0
EXIT_GENERAL_ERROR = 1
EXIT_USAGE_ERROR = 2
EXIT_FILE_ERROR = 3
EXIT_PERMISSION_ERROR = 4

print(f"Success: {EXIT_SUCCESS}")
print(f"General error: {EXIT_GENERAL_ERROR}")
print(f"Usage error: {EXIT_USAGE_ERROR}")
print(f"File error: {EXIT_FILE_ERROR}")
print(f"Permission error: {EXIT_PERMISSION_ERROR}")

# Example 4: Conditional exit
print("\nExample 4: Conditional exit")
print("-" * 40)

def process_data(data):
    """Process data and exit based on result"""
    if not data:
        print("Error: No data provided")
        sys.exit(1)
    
    if len(data) < 5:
        print("Warning: Data too short")
        sys.exit(2)
    
    print(f"Processing {len(data)} items...")
    print("Success!")
    sys.exit(0)

# Test (uncomment one):
# process_data([])           # Exits with 1
# process_data([1, 2])       # Exits with 2
# process_data([1,2,3,4,5])  # Exits with 0

# Example 5: Exit from nested function
print("Example 5: Exit from anywhere")
print("-" * 40)

def level3():
    print("Level 3: Error detected!")
    sys.exit(1)

def level2():
    print("Level 2")
    level3()
    print("Never reaches here")

def level1():
    print("Level 1")
    level2()
    print("Never reaches here either")

# Uncomment to test:
# level1()

print("\nKey points:")
print("  • sys.exit(0) = Success")
print("  • sys.exit(1) = Error")
print("  • sys.exit(N) = Specific errors")
print("  • Stops program immediately")
print("  • Returns code to shell")
