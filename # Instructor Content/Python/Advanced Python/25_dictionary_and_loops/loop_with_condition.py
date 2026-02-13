#!/usr/bin/env python3
# Looping with conditions

users = {
    "alice": {"age": 25, "active": True},
    "bob": {"age": 17, "active": False},
    "charlie": {"age": 30, "active": True},
    "david": {"age": 16, "active": True}
}

# Filter active users
print("Active users:")
for username, info in users.items():
    if info["active"]:
        print(f"  {username} (age: {info['age']})")

# Filter adults
print("\nAdults (18+):")
for username, info in users.items():
    if info["age"] >= 18:
        print(f"  {username}")

# Complex condition
print("\nActive adults:")
for username, info in users.items():
    if info["active"] and info["age"] >= 18:
        print(f"  {username}")
