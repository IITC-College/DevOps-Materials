#!/usr/bin/env python3
# Adding new key-value pairs

user = {
    "name": "Alice",
    "age": 25
}

print(f"Original: {user}")

# Add new keys
user["city"] = "Boston"
user["email"] = "alice@example.com"
user["active"] = True

print(f"After adding keys: {user}")

# Add multiple keys
user["role"] = "admin"
user["last_login"] = "2026-01-30"

print(f"Final: {user}")
