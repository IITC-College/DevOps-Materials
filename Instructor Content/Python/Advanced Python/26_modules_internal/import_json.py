#!/usr/bin/env python3
# Using json module

import json

# Python dict to JSON string
data = {
    "name": "Alice",
    "age": 25,
    "city": "Boston",
    "active": True
}

json_string = json.dumps(data)
print(f"JSON string: {json_string}")

# Pretty print JSON
pretty_json = json.dumps(data, indent=2)
print(f"Pretty JSON:\n{pretty_json}")

# JSON string to Python dict
json_input = '{"host": "localhost", "port": 8080}'
config = json.loads(json_input)
print(f"Parsed config: {config}")
print(f"Host: {config['host']}")

# Nested structure
nested = {
    "user": {
        "name": "Bob",
        "details": {
            "age": 30,
            "email": "bob@example.com"
        }
    }
}
print(json.dumps(nested, indent=2))
