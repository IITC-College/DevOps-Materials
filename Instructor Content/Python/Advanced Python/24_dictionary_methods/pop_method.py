#!/usr/bin/env python3
# Using dict.pop()

user = {
    "name": "Alice",
    "age": 25,
    "city": "Boston",
    "temp": "delete_me"
}

print(f"Original: {user}")

# Remove and return value
temp_value = user.pop("temp")
print(f"Popped value: {temp_value}")
print(f"After pop: {user}")

# Pop with default (if key doesn't exist)
email = user.pop("email", "no_email@example.com")
print(f"Email (default): {email}")

# Pop another key
age = user.pop("age")
print(f"Popped age: {age}")
print(f"Final: {user}")
