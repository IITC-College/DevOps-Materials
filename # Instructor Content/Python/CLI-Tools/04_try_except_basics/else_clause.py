#!/usr/bin/env python3
# try/except/else clause

"""
TRY/EXCEPT/ELSE:

try:
    risky_code()
except ErrorType:
    handle_error()
else:
    # Runs only if NO exception occurred
    success_code()

ELSE block runs when try succeeds!
"""

# Example 1: Basic else usage
print("Example 1: else clause")
print("-" * 40)

def divide(a, b):
    """Divide with else clause"""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    else:
        print("Division successful")
        return result

print(f"10 / 2 = {divide(10, 2)}")
print(f"10 / 0 = {divide(10, 0)}")

# Example 2: File processing with else
print("\nExample 2: File processing")
print("-" * 40)

def process_file(filename):
    """Process file with else for success case"""
    try:
        with open(filename, 'r') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    else:
        print(f"✓ Successfully read {filename}")
        print(f"  Length: {len(data)} characters")
        return data

# Create test file
with open('test.txt', 'w') as f:
    f.write("Hello World")

content = process_file('test.txt')
content = process_file('missing.txt')

# Example 3: Else for additional processing
print("\nExample 3: Post-processing in else")
print("-" * 40)

def load_and_validate_config(filename):
    """Load config and validate in else block"""
    try:
        import json
        with open(filename, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print("Config file not found")
        return None
    except json.JSONDecodeError:
        print("Invalid JSON")
        return None
    else:
        # Validation happens here (only if load succeeded)
        print("✓ Config loaded, validating...")
        if 'version' in config:
            print("  ✓ Version found")
        if 'app_name' in config:
            print("  ✓ App name found")
        return config

# Create config
import json
with open('config.json', 'w') as f:
    json.dump({"app_name": "Test", "version": 1.0}, f)

config = load_and_validate_config('config.json')

# Example 4: Try/except/else pattern
print("\nExample 4: Complete pattern")
print("-" * 40)

def safe_number_input(prompt):
    """Get number from user with else"""
    value = "42"  # Simulating input
    
    try:
        number = int(value)
    except ValueError:
        print(f"'{value}' is not a valid number")
        return None
    else:
        print(f"✓ Valid number: {number}")
        if number < 0:
            print("  Warning: negative number")
        return number

result = safe_number_input("Enter number: ")

# Example 5: Else vs putting code in try
print("\nExample 5: Why use else?")
print("-" * 40)

# BAD: Too much in try block
print("Bad practice:")
try:
    with open('test.txt', 'r') as f:
        data = f.read()
    # Processing here catches ALL exceptions
    processed = data.upper()
    count = len(processed)
    print(f"Processed: {count} chars")
except FileNotFoundError:
    print("File not found")

# GOOD: Only risky code in try
print("\nGood practice:")
try:
    with open('test.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")
else:
    # Safe processing here
    processed = data.upper()
    count = len(processed)
    print(f"✓ Processed: {count} chars")

print("\nKey points:")
print("  ✓ else runs only if try succeeds")
print("  ✓ Use for success-case code")
print("  ✓ Keeps try block minimal")
print("  ✓ Makes code more readable")
