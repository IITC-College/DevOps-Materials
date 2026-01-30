#!/usr/bin/env python3
# Looping over dictionary keys

user = {
    "name": "Alice",
    "age": 25,
    "city": "Boston",
    "email": "alice@example.com"
}

# Loop over keys (default behavior)
print("Method 1 - Direct iteration:")
for key in user:
    print(f"  {key}")

# Loop over keys explicitly
print("\nMethod 2 - Using .keys():")
for key in user.keys():
    print(f"  {key}: {user[key]}")
