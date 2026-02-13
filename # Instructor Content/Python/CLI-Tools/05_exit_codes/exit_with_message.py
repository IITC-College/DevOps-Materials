#!/usr/bin/env python3
# Exiting with messages

import sys

"""
EXIT WITH MESSAGE:

sys.exit("Error message")    # Prints message and exits with code 1
sys.exit(0)                   # Silent success exit
sys.exit(1)                   # Silent error exit

BEST PRACTICE:
- Print message before exiting
- Use sys.exit(code) for numeric exit code
- Use sys.exit("message") for quick error with message
"""

# Example 1: Exit with string message
print("Example 1: sys.exit with message string")
print("-" * 40)

def check_file_exists(filename):
    """Check if file exists, exit if not"""
    import os
    if not os.path.exists(filename):
        sys.exit(f"Error: File '{filename}' not found")  # Exits with code 1
    print(f"✓ File {filename} exists")

# Uncomment to test:
# check_file_exists('missing.txt')

# Example 2: Print then exit with code
print("Example 2: Print message then exit")
print("-" * 40)

def validate_args():
    """Validate command-line arguments"""
    if len(sys.argv) < 2:
        print("Error: No command provided", file=sys.stderr)
        print(f"Usage: python {sys.argv[0]} <command>", file=sys.stderr)
        sys.exit(2)  # Exit with specific code
    print(f"Command: {sys.argv[1]}")

# validate_args()  # Uncomment to test

# Example 3: Structured error messages
print("Example 3: Structured error messages")
print("-" * 40)

def structured_exit(message, code=1):
    """Exit with structured error message"""
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    error_msg = f"[{timestamp}] ERROR: {message}"
    print(error_msg, file=sys.stderr)
    sys.exit(code)

# structured_exit("Database connection failed", 3)  # Uncomment to test

# Example 4: Different exit scenarios
print("Example 4: Different scenarios")
print("-" * 40)

def process_command(command):
    """Process command with appropriate exits"""
    if command == "help":
        print("Available commands: start, stop, status")
        sys.exit(0)  # Success exit for help
    
    if command not in ["start", "stop", "status"]:
        print(f"Error: Unknown command '{command}'", file=sys.stderr)
        sys.exit(2)  # Invalid argument
    
    print(f"Executing: {command}")
    # ... do work ...
    sys.exit(0)  # Success

# Test with different commands
if len(sys.argv) > 1:
    # process_command(sys.argv[1])  # Uncomment to test
    pass

# Example 5: Error handling with exits
print("Example 5: Error handling")
print("-" * 40)

def safe_file_read(filename):
    """Read file with proper exit codes"""
    try:
        with open(filename, 'r') as f:
            content = f.read()
        print(f"✓ Read {len(content)} characters")
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found", file=sys.stderr)
        sys.exit(3)  # File error
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'", file=sys.stderr)
        sys.exit(4)  # Permission error
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)  # General error

# safe_file_read('data.txt')  # Uncomment to test

print("\nBest practices:")
print("  ✓ Print error to stderr before exit")
print("  ✓ Use descriptive error messages")
print("  ✓ Include context in error messages")
print("  ✓ Use appropriate exit codes")
print("  ✓ sys.exit('message') for quick errors")
