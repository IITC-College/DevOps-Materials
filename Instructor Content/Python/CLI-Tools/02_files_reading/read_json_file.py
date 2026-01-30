#!/usr/bin/env python3
# Reading JSON files

import json

"""
JSON FILES:

JSON = JavaScript Object Notation
Common for configuration and data storage

Python → JSON:
  dict   → object
  list   → array
  str    → string
  int    → number
  float  → number
  True   → true
  False  → false
  None   → null
"""

# Create sample JSON config file
config_data = {
    "app_name": "DevOps Helper",
    "version": 2.0,
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "devops_db"
    },
    "features": ["backup", "deploy", "monitor"],
    "debug": True,
    "max_retries": 3
}

with open('config.json', 'w') as f:
    json.dump(config_data, f, indent=2)

print("Created config.json\n")

# Example 1: Read JSON file
print("Example 1: Read JSON file")
print("-" * 40)

with open('config.json', 'r') as f:
    config = json.load(f)

print(f"Type: {type(config)}")
print(f"App name: {config['app_name']}")
print(f"Version: {config['version']}")
print(f"Debug: {config['debug']}")

# Example 2: Access nested data
print("\nExample 2: Access nested data")
print("-" * 40)

print("Database configuration:")
print(f"  Host: {config['database']['host']}")
print(f"  Port: {config['database']['port']}")
print(f"  Name: {config['database']['name']}")

# Example 3: Loop over array in JSON
print("\nExample 3: Features list")
print("-" * 40)

print("Available features:")
for feature in config['features']:
    print(f"  - {feature}")

# Example 4: Handle JSON errors
print("\nExample 4: Error handling")
print("-" * 40)

# Create invalid JSON file
with open('invalid.json', 'w') as f:
    f.write('{"name": "test", invalid}')

try:
    with open('invalid.json', 'r') as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    print(f"JSON Error: {e}")

# Example 5: Read JSON string
print("\nExample 5: Parse JSON string")
print("-" * 40)

json_string = '{"status": "active", "count": 42}'
data = json.loads(json_string)  # loads() for string, load() for file
print(f"Parsed: {data}")
print(f"Status: {data['status']}")
print(f"Count: {data['count']}")

# Example 6: Practical config loading
print("\nExample 6: Load config with defaults")
print("-" * 40)

def load_config(filename, defaults=None):
    """Load config with fallback to defaults"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Config file not found, using defaults")
        return defaults or {}
    except json.JSONDecodeError:
        print(f"Invalid JSON, using defaults")
        return defaults or {}

# Try to load non-existent file
app_config = load_config('missing.json', {"app_name": "Default App"})
print(f"App name: {app_config['app_name']}")

print("\nJSON best practices:")
print("  ✓ Use json.load() for files")
print("  ✓ Use json.loads() for strings")
print("  ✓ Handle JSONDecodeError")
print("  ✓ Provide default values")
