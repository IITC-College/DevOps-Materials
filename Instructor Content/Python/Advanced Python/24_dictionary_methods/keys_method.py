#!/usr/bin/env python3
# Using dict.keys()

user = {
    "name": "Alice",
    "age": 25,
    "city": "Boston",
    "email": "alice@example.com"
}

# Get all keys
keys = user.keys()
print(f"Keys: {keys}")

# Convert to list
keys_list = list(user.keys())
print(f"Keys as list: {keys_list}")

# Iterate over keys
print("All keys:")
for key in user.keys():
    print(f"  - {key}")
