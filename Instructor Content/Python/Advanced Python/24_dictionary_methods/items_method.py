#!/usr/bin/env python3
# Using dict.items()

user = {
    "name": "Alice",
    "age": 25,
    "city": "Boston"
}

# Get all items (key-value pairs)
items = user.items()
print(f"Items: {items}")

# Iterate over items
print("All key-value pairs:")
for key, value in user.items():
    print(f"  {key}: {value}")

# Convert to list of tuples
items_list = list(user.items())
print(f"Items as list: {items_list}")
