#!/usr/bin/env python3
# try/except basics

"""
TRY/EXCEPT STRUCTURE:

try:
    # Code that might fail
    risky_operation()
except ExceptionType:
    # Handle the error
    handle_error()

WHY USE TRY/EXCEPT:
- Graceful error handling
- User-friendly error messages
- Prevent crashes
- Log errors
- Continue execution
"""

# Example 1: Basic try/except
print("Example 1: Basic try/except")
print("-" * 40)

try:
    result = 10 / 2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# Example 2: Catching errors
print("\nExample 2: Catching division by zero")
print("-" * 40)

try:
    result = 10 / 0  # This will fail
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

print("Program continues...")

# Example 3: File operations
print("\nExample 3: File not found")
print("-" * 40)

try:
    with open('missing.txt', 'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found")

# Example 4: Getting error message
print("\nExample 4: Error message details")
print("-" * 40)

try:
    with open('/invalid/path/file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"Error occurred: {e}")

# Example 5: Multiple operations
print("\nExample 5: Multiple risky operations")
print("-" * 40)

def divide_numbers(a, b):
    """Divide two numbers safely"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print(f"Cannot divide {a} by {b}")
        return None

print(f"10 / 2 = {divide_numbers(10, 2)}")
print(f"10 / 0 = {divide_numbers(10, 0)}")

# Example 6: User input validation
print("\nExample 6: Safe user input")
print("-" * 40)

def get_number():
    """Get number from user safely"""
    try:
        value = "42"  # Simulating input
        number = int(value)
        return number
    except ValueError:
        print("Error: Not a valid number")
        return None

number = get_number()
if number:
    print(f"You entered: {number}")

# Example 7: Without try/except (crashes)
print("\nExample 7: What happens without try/except")
print("-" * 40)

print("Without error handling, this would crash:")
print("  result = 10 / 0  # Program stops here")
print("  print('Never reaches this line')")
print()
print("With try/except:")
try:
    result = 10 / 0
    print("This won't print")
except ZeroDivisionError:
    print("  Error caught! Program continues.")

print("  Program still running!")

print("\nKey points:")
print("  ✓ Wrap risky code in try block")
print("  ✓ Catch specific exceptions")
print("  ✓ Provide helpful error messages")
print("  ✓ Program continues after exception")
