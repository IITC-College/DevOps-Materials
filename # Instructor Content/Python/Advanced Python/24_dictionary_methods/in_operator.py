#!/usr/bin/env python3
# Using 'in' operator with dictionaries

user = {
    "name": "Alice",
    "age": 25,
    "city": "Boston"
}

# Check if key exists
if "name" in user:
    print(f"Name exists: {user['name']}")

if "email" in user:
    print("Email exists")
else:
    print("Email does not exist")

# Check before accessing
key = "age"
if key in user:
    print(f"{key}: {user[key]}")

# Use with get as alternative
email = user.get("email") if "email" in user else "N/A"
print(f"Email: {email}")

# Check multiple keys
required_keys = ["name", "age", "email"]
for key in required_keys:
    if key in user:
        print(f"✓ {key} exists")
    else:
        print(f"✗ {key} missing")
