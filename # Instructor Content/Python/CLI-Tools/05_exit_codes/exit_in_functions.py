#!/usr/bin/env python3
# Using sys.exit() in functions

import sys

"""
EXIT FROM FUNCTIONS:

sys.exit() can be called from anywhere:
- Main code
- Functions
- Nested functions
- try/except blocks

It immediately terminates the entire program!
"""

# Example 1: Exit from function
print("Example 1: Exit from function")
print("-" * 40)

def validate_input(value):
    """Validate input, exit if invalid"""
    if not value:
        print("Error: Empty input")
        sys.exit(1)
    if len(value) < 3:
        print("Error: Input too short")
        sys.exit(2)
    print(f"✓ Valid input: {value}")

# validate_input("OK")     # Passes
# validate_input("X")      # Exits with 2
# validate_input("")       # Exits with 1

# Example 2: Exit from nested functions
print("\nExample 2: Exit from nested functions")
print("-" * 40)

def check_config(config):
    """Check configuration, exit if invalid"""
    if 'host' not in config:
        print("Error: Missing 'host' in config")
        sys.exit(3)
    if 'port' not in config:
        print("Error: Missing 'port' in config")
        sys.exit(3)
    print("✓ Config valid")

def load_and_check_config(filename):
    """Load and validate config"""
    try:
        import json
        with open(filename, 'r') as f:
            config = json.load(f)
        check_config(config)  # May exit
        return config
    except FileNotFoundError:
        print(f"Error: Config file not found")
        sys.exit(4)

# Test scenarios (uncomment to test):
# config = load_and_check_config('missing.json')  # Exits in try/except
# config = load_and_check_config('bad_config.json')  # Exits in check_config

# Example 3: Return vs exit
print("Example 3: Return vs Exit")
print("-" * 40)

def with_return(value):
    """Returns to caller"""
    if not value:
        print("Empty value, returning None")
        return None
    return value.upper()

def with_exit(value):
    """Exits entire program"""
    if not value:
        print("Empty value, exiting program")
        sys.exit(1)
    return value.upper()

result = with_return("")
print(f"After with_return: {result}")  # This prints

# with_exit("")  # This would exit, code below never runs
# print("This never prints")

# Example 4: Function that returns exit code
print("\nExample 4: Return code vs exit with code")
print("-" * 40)

def process_file_return_code(filename):
    """Process file and return status code"""
    try:
        with open(filename, 'r') as f:
            data = f.read()
        print(f"✓ Processed {filename}")
        return 0  # Success
    except FileNotFoundError:
        print(f"✗ File not found")
        return 3  # File error
    except Exception as e:
        print(f"✗ Error: {e}")
        return 1  # General error

def process_file_and_exit(filename):
    """Process file and exit with status code"""
    try:
        with open(filename, 'r') as f:
            data = f.read()
        print(f"✓ Processed {filename}")
        sys.exit(0)
    except FileNotFoundError:
        print(f"✗ File not found")
        sys.exit(3)
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)

# Returns allow continued execution
code = process_file_return_code('missing.txt')
print(f"Got code: {code}, program continues\n")

# Exit stops everything
# process_file_and_exit('missing.txt')  # Would exit here
# print("Never reaches this")

# Example 5: Main pattern
print("Example 5: Main function pattern")
print("-" * 40)

def do_work():
    """Do some work, return success/failure"""
    print("Doing work...")
    # ... work here ...
    return True  # or False

def main():
    """Main function that coordinates and exits"""
    print("Starting...")
    
    success = do_work()
    
    if success:
        print("✓ All done!")
        sys.exit(0)
    else:
        print("✗ Failed")
        sys.exit(1)

# main()  # Uncomment to test

print("\nBest practices:")
print("  ✓ Use return in functions (allows testing)")
print("  ✓ Use sys.exit() in main() only")
print("  ✓ Let main() decide final exit code")
print("  ✗ Avoid sys.exit() in utility functions")
