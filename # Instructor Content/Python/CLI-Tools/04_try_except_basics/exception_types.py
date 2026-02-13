#!/usr/bin/env python3
# Common exception types

"""
COMMON EXCEPTIONS:

FileNotFoundError    - File doesn't exist
PermissionError      - No permission to access
ValueError           - Invalid value/type conversion
TypeError            - Wrong type
KeyError             - Dictionary key doesn't exist
IndexError           - List index out of range
ZeroDivisionError    - Division by zero
ImportError          - Cannot import module
AttributeError       - Attribute doesn't exist
IOError              - Input/Output error
"""

# Example 1: FileNotFoundError
print("1. FileNotFoundError")
print("-" * 40)

try:
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("✗ File not found")

# Example 2: PermissionError
print("\n2. PermissionError")
print("-" * 40)

try:
    with open('/root/protected.txt', 'w') as f:
        f.write("data")
except PermissionError:
    print("✗ Permission denied")

# Example 3: ValueError
print("\n3. ValueError")
print("-" * 40)

try:
    number = int("not_a_number")
except ValueError as e:
    print(f"✗ Value error: {e}")

# Example 4: TypeError
print("\n4. TypeError")
print("-" * 40)

try:
    result = "string" + 5
except TypeError as e:
    print(f"✗ Type error: {e}")

# Example 5: KeyError
print("\n5. KeyError")
print("-" * 40)

config = {"name": "app", "version": 1.0}
try:
    port = config["port"]  # Key doesn't exist
except KeyError as e:
    print(f"✗ Key error: {e}")
    print("Using default port: 8080")

# Example 6: IndexError
print("\n6. IndexError")
print("-" * 40)

items = ["a", "b", "c"]
try:
    item = items[10]  # Index out of range
except IndexError as e:
    print(f"✗ Index error: {e}")

# Example 7: ZeroDivisionError
print("\n7. ZeroDivisionError")
print("-" * 40)

try:
    result = 100 / 0
except ZeroDivisionError:
    print("✗ Cannot divide by zero")

# Example 8: ImportError
print("\n8. ImportError")
print("-" * 40)

try:
    import nonexistent_module
except ImportError:
    print("✗ Module not found")

# Example 9: AttributeError
print("\n9. AttributeError")
print("-" * 40)

class MyClass:
    pass

obj = MyClass()
try:
    value = obj.nonexistent_attribute
except AttributeError as e:
    print(f"✗ Attribute error: {e}")

# Example 10: All together
print("\n10. Handling different exceptions")
print("-" * 40)

def process_file(filename):
    """Process file with multiple error handlers"""
    try:
        with open(filename, 'r') as f:
            data = f.read()
            number = int(data)
            result = 100 / number
            return result
    except FileNotFoundError:
        print("Error: File not found")
    except ValueError:
        print("Error: File doesn't contain a valid number")
    except ZeroDivisionError:
        print("Error: Number cannot be zero")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    return None

# Test with different scenarios
result = process_file('missing.txt')

print("\nCommon exceptions reference:")
for exc in ['FileNotFoundError', 'PermissionError', 'ValueError', 
            'TypeError', 'KeyError', 'IndexError', 'ZeroDivisionError']:
    print(f"  - {exc}")
