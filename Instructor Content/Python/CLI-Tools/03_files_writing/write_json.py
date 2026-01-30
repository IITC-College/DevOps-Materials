#!/usr/bin/env python3
# Writing JSON files

import json

"""
WRITING JSON:

json.dump(data, file)   → Write to file
json.dumps(data)        → Convert to string

PARAMETERS:
- indent: Pretty print with indentation
- sort_keys: Sort dictionary keys
"""

# Example 1: Basic JSON write
print("Example 1: Basic JSON write")
print("-" * 40)

data = {
    "app_name": "DevOps Helper",
    "version": 2.0,
    "enabled": True,
    "max_retries": 3
}

with open('config.json', 'w') as f:
    json.dump(data, f)

print("✓ Wrote JSON file")

# Read it back
with open('config.json', 'r') as f:
    print(f"Content: {f.read()}")

# Example 2: Pretty print with indent
print("\nExample 2: Pretty formatted JSON")
print("-" * 40)

data = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "credentials": {
            "username": "admin",
            "password": "secret"
        }
    },
    "features": ["backup", "deploy", "monitor"],
    "debug": False
}

with open('config_pretty.json', 'w') as f:
    json.dump(data, f, indent=2)

print("✓ Wrote formatted JSON")
with open('config_pretty.json', 'r') as f:
    print(f.read())

# Example 3: Sort keys
print("\nExample 3: Sorted keys")
print("-" * 40)

data = {
    "zebra": 1,
    "apple": 2,
    "mango": 3,
    "banana": 4
}

with open('sorted.json', 'w') as f:
    json.dump(data, f, indent=2, sort_keys=True)

print("✓ Wrote JSON with sorted keys")
with open('sorted.json', 'r') as f:
    print(f.read())

# Example 4: Writing list of objects
print("\nExample 4: Array of objects")
print("-" * 40)

users = [
    {"name": "Alice", "age": 30, "active": True},
    {"name": "Bob", "age": 25, "active": False},
    {"name": "Charlie", "age": 35, "active": True}
]

with open('users.json', 'w') as f:
    json.dump(users, f, indent=2)

print("✓ Wrote array of users")

# Example 5: Update JSON file
print("\nExample 5: Update existing JSON")
print("-" * 40)

# Read existing
with open('config.json', 'r') as f:
    config = json.load(f)

# Modify
config['version'] = 2.1
config['new_feature'] = True

# Write back
with open('config.json', 'w') as f:
    json.dump(config, f, indent=2)

print("✓ Updated config.json")
with open('config.json', 'r') as f:
    print(f.read())

# Example 6: JSON string (dumps)
print("\nExample 6: JSON to string")
print("-" * 40)

data = {"status": "active", "count": 42}

json_string = json.dumps(data)
print(f"JSON string: {json_string}")

json_pretty = json.dumps(data, indent=2)
print(f"Pretty JSON:\n{json_pretty}")

# Example 7: Saving application state
print("\nExample 7: Save application state")
print("-" * 40)

import datetime

app_state = {
    "last_run": datetime.datetime.now().isoformat(),
    "user": "admin",
    "settings": {
        "theme": "dark",
        "notifications": True
    },
    "recent_actions": [
        "deployed_app",
        "ran_backup",
        "checked_status"
    ]
}

with open('app_state.json', 'w') as f:
    json.dump(app_state, f, indent=2)

print("✓ Saved application state")

# Example 8: Handle non-serializable types
print("\nExample 8: Custom JSON encoder")
print("-" * 40)

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return super().default(obj)

data = {
    "timestamp": datetime.datetime.now(),
    "value": 100
}

with open('custom.json', 'w') as f:
    json.dump(data, f, indent=2, cls=CustomEncoder)

print("✓ Wrote JSON with custom types")

print("\nBest practices:")
print("  ✓ Use indent=2 for readability")
print("  ✓ Use sort_keys for consistency")
print("  ✓ json.dump() for files")
print("  ✓ json.dumps() for strings")
