#!/usr/bin/env python3
# Multiple except blocks

"""
MULTIPLE EXCEPT BLOCKS:

try:
    risky_code()
except FileNotFoundError:
    handle_file_not_found()
except PermissionError:
    handle_permission_error()
except ValueError:
    handle_value_error()
except Exception as e:
    handle_other_errors(e)

Each exception gets its own handler!
"""

# Example 1: Multiple except blocks
print("Example 1: Multiple except handlers")
print("-" * 40)

def read_number_from_file(filename):
    """Read and convert number with multiple error handlers"""
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
            number = int(content)
            return number
    except FileNotFoundError:
        print(f"✗ File '{filename}' not found")
        return None
    except ValueError:
        print(f"✗ File doesn't contain a valid number")
        return None
    except PermissionError:
        print(f"✗ No permission to read '{filename}'")
        return None

# Create test file
with open('value.txt', 'w') as f:
    f.write("42")

result = read_number_from_file('value.txt')
print(f"✓ Read number: {result}")

result = read_number_from_file('missing.txt')
print(f"Result: {result}")

# Example 2: Order matters
print("\nExample 2: Exception order (specific first)")
print("-" * 40)

def process_data(data):
    """Process data with ordered exception handling"""
    try:
        # Multiple potential errors
        result = int(data)  # ValueError
        output = 100 / result  # ZeroDivisionError
        return output
    except ValueError:
        print("Error: Data must be a number")
        return None
    except ZeroDivisionError:
        print("Error: Number cannot be zero")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

print(f"Process '50': {process_data('50')}")
print(f"Process 'abc': {process_data('abc')}")
print(f"Process '0': {process_data('0')}")

# Example 3: Different responses
print("\nExample 3: Different error responses")
print("-" * 40)

def load_config(filename):
    """Load config with detailed error handling"""
    import json
    
    try:
        with open(filename, 'r') as f:
            config = json.load(f)
            print("✓ Config loaded successfully")
            return config
    except FileNotFoundError:
        print("Creating default config...")
        default = {"app": "default", "version": 1.0}
        with open(filename, 'w') as f:
            json.dump(default, f, indent=2)
        return default
    except json.JSONDecodeError:
        print("Config file corrupted, backing up and recreating...")
        import shutil
        shutil.copy(filename, filename + '.bak')
        default = {"app": "default", "version": 1.0}
        with open(filename, 'w') as f:
            json.dump(default, f, indent=2)
        return default
    except PermissionError:
        print("Permission denied, using in-memory config")
        return {"app": "temp", "version": 1.0}

config = load_config('app_config.json')
print(f"Config: {config}")

# Example 4: Logging different errors
print("\nExample 4: Logging errors differently")
print("-" * 40)

def logged_file_operation(filename):
    """File operation with detailed logging"""
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            print(f"✓ Read {len(lines)} lines")
            return lines
    except FileNotFoundError:
        print("[ERROR] File not found - user error")
        return []
    except PermissionError:
        print("[CRITICAL] Permission denied - system error")
        return []
    except IOError as e:
        print(f"[ERROR] I/O error - hardware issue: {e}")
        return []
    except Exception as e:
        print(f"[CRITICAL] Unexpected error - investigate: {e}")
        return []

lines = logged_file_operation('value.txt')

# Example 5: Combining exceptions
print("\nExample 5: Group similar exceptions")
print("-" * 40)

def safe_operation(filename, operation):
    """Perform operation with grouped error handling"""
    try:
        with open(filename, 'r') as f:
            data = f.read()
            result = operation(data)
            return result
    except (FileNotFoundError, IsADirectoryError):
        print("File access error")
        return None
    except (ValueError, TypeError):
        print("Data processing error")
        return None
    except (PermissionError, OSError):
        print("System error")
        return None

result = safe_operation('value.txt', lambda x: len(x))
print(f"Result: {result}")

print("\nKey patterns:")
print("  ✓ Specific exceptions first")
print("  ✓ General Exception last (catch-all)")
print("  ✓ Different actions for different errors")
print("  ✓ Group similar exceptions when appropriate")
