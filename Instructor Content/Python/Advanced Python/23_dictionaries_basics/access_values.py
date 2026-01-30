#!/usr/bin/env python3
# Accessing dictionary values

user = {
    "name": "Alice",
    "age": 25,
    "city": "Boston",
    "active": True
}

# Access by key
print(user["name"])
print(user["age"])
print(user["city"])
print(user["active"])

# Use in expressions
print(f"User {user['name']} is {user['age']} years old")
print(f"Lives in {user['city']}")
