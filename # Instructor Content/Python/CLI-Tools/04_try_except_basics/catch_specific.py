#!/usr/bin/env python3
# Catching specific exceptions

"""
CATCH SPECIFIC EXCEPTIONS:

DON'T:
  except:              # Catches everything (bad!)
  except Exception:    # Too broad

DO:
  except FileNotFoundError:     # Specific
  except ValueError:             # Specific
  except (TypeError, KeyError):  # Multiple specific
"""

# Example 1: Catching specific vs general
print("Example 1: Specific vs general exceptions")
print("-" * 40)

# Bad: Too general
try:
    number = int("abc")
except:  # Don't do this!
    print("Something went wrong (but what?)")

# Good: Specific
try:
    number = int("abc")
except ValueError:
    print("Error: Invalid number format")

# Example 2: Different errors need different handling
print("\nExample 2: Different error handling")
print("-" * 40)

def read_and_process(filename):
    """Read file and process data"""
    try:
        with open(filename, 'r') as f:
            data = f.read()
            number = int(data)
            return number * 2
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        print("Action: Please create the file")
        return None
    except ValueError:
        print(f"Error: File contains invalid data")
        print("Action: File should contain a number")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        print("Action: Check file permissions")
        return None

# Create test file
with open('number.txt', 'w') as f:
    f.write("42")

result = read_and_process('number.txt')
print(f"Result: {result}")

result = read_and_process('missing.txt')

# Example 3: Catching multiple exceptions
print("\nExample 3: Multiple exceptions with same handling")
print("-" * 40)

def safe_divide(a, b):
    """Divide numbers safely"""
    try:
        result = a / b
        return result
    except (ZeroDivisionError, TypeError):
        # Handle both the same way
        print(f"Cannot divide {a} by {b}")
        return None

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / 'x' = {safe_divide(10, 'x')}")

# Example 4: Catch and re-raise
print("\nExample 4: Logging then re-raising")
print("-" * 40)

def logged_operation():
    """Operation with logging"""
    try:
        result = 10 / 0
        return result
    except ZeroDivisionError as e:
        print("Logging error to file...")
        # Could re-raise if needed:
        # raise
        return None

result = logged_operation()

# Example 5: Specific exceptions in order
print("\nExample 5: Order matters (specific before general)")
print("-" * 40)

def process_config(filename):
    """Load and validate config"""
    try:
        import json
        with open(filename, 'r') as f:
            config = json.load(f)
            return config
    except FileNotFoundError:
        print("Config file not found")
    except json.JSONDecodeError:
        print("Invalid JSON in config file")
    except PermissionError:
        print("No permission to read config")
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"Unexpected error: {e}")
    
    return {}

config = process_config('config.json')

# Example 6: Accessing error details
print("\nExample 6: Error details")
print("-" * 40)

try:
    data = {"name": "app"}
    port = data["port"]
except KeyError as e:
    print(f"Missing key: {e}")
    print(f"Error type: {type(e).__name__}")
    print(f"Available keys: {list(data.keys())}")

print("\nBest practices:")
print("  ✓ Catch specific exceptions")
print("  ✓ Provide actionable error messages")
print("  ✓ Order from specific to general")
print("  ✗ Avoid bare 'except:'")
