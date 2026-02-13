#!/usr/bin/env python3
# sys.exit() vs return

import sys

"""
sys.exit() vs return:

return:
- Returns from current function
- Allows caller to handle result
- Program continues
- Testable functions

sys.exit():
- Terminates entire program immediately
- Returns exit code to shell
- No further code executes
- Use in main() or top-level error handling

BEST PRACTICE:
- Use return in functions
- Use sys.exit() only in main()
"""

# Example 1: Return from function
print("Example 1: Using return")
print("-" * 40)

def process_with_return(data):
    """Process data, return result"""
    if not data:
        print("No data, returning None")
        return None
    
    result = len(data)
    print(f"Processed {result} items")
    return result

result1 = process_with_return([1, 2, 3])
print(f"Result: {result1}")
print("Program continues...\n")

result2 = process_with_return([])
print(f"Result: {result2}")
print("Program still continues!\n")

# Example 2: Exit from function
print("Example 2: Using sys.exit()")
print("-" * 40)

def process_with_exit(data):
    """Process data, exit on error"""
    if not data:
        print("No data, exiting program")
        sys.exit(1)
    
    result = len(data)
    print(f"Processed {result} items")
    return result

result = process_with_exit([1, 2, 3])
print(f"Result: {result}")
# process_with_exit([])  # Would exit here
# print("Never reaches this line")

# Example 3: Testable functions
print("\nExample 3: Testable vs non-testable")
print("-" * 40)

# GOOD: Testable function
def validate_config_testable(config):
    """Validate config, return True/False"""
    if 'host' not in config:
        return False, "Missing host"
    if 'port' not in config:
        return False, "Missing port"
    return True, "Valid"

# Can test this
config1 = {'host': 'localhost', 'port': 8080}
valid, msg = validate_config_testable(config1)
print(f"Config 1: {msg} ({valid})")

config2 = {'host': 'localhost'}
valid, msg = validate_config_testable(config2)
print(f"Config 2: {msg} ({valid})")

# BAD: Not testable (exits program)
def validate_config_exits(config):
    """Validate config, exits on error"""
    if 'host' not in config:
        sys.exit(1)
    if 'port' not in config:
        sys.exit(1)
    return True

# Can't easily test this - it would exit!
# validate_config_exits(config2)  # Would exit

# Example 4: Proper pattern
print("\nExample 4: Recommended pattern")
print("-" * 40)

def load_config(filename):
    """Load config, return None on error"""
    try:
        import json
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading config: {e}")
        return None

def validate_config(config):
    """Validate config, return True/False"""
    if not config:
        return False
    if 'host' not in config:
        return False
    if 'port' not in config:
        return False
    return True

def main():
    """Main function handles exit codes"""
    # Load config
    config = load_config('config.json')
    if not config:
        print("Failed to load config")
        sys.exit(1)
    
    # Validate
    if not validate_config(config):
        print("Invalid config")
        sys.exit(2)
    
    # Process
    print("✓ Config loaded and validated")
    sys.exit(0)

# main()  # Uncomment to test

# Example 5: Comparison table
print("\nExample 5: Comparison")
print("-" * 40)

comparison = """
Feature           | return          | sys.exit()
------------------+-----------------+-------------------
Scope             | Current function| Entire program
Testable          | Yes             | No (hard to test)
Caller continues  | Yes             | No
Use in libraries  | Yes             | No
Use in main()     | Indirect        | Yes
Error handling    | Flexible        | Final
"""

print(comparison)

print("\nWhen to use each:")
print("-" * 40)
print("""
USE RETURN:
  ✓ In utility functions
  ✓ In library code
  ✓ When caller needs to handle result
  ✓ For testable functions
  ✓ For reusable code

USE SYS.EXIT():
  ✓ In main() function
  ✓ For final program termination
  ✓ In CLI tool top level
  ✓ After logging/cleanup complete
  ✓ To return exit code to shell

PATTERN:
  def utility_function():
      return result_or_none
  
  def main():
      result = utility_function()
      if result:
          sys.exit(0)
      else:
          sys.exit(1)
""")
