#!/usr/bin/env python3
# Nested dictionaries

user = {
    "name": "Alice",
    "age": 25,
    "address": {
        "street": "123 Main St",
        "city": "Boston",
        "zip": "02101"
    },
    "contact": {
        "email": "alice@example.com",
        "phone": "555-1234"
    }
}

# Access nested values
print(f"Name: {user['name']}")
print(f"City: {user['address']['city']}")
print(f"Email: {user['contact']['email']}")

# Modify nested values
user["address"]["zip"] = "02102"
print(f"Updated zip: {user['address']['zip']}")
