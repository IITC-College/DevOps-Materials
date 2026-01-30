#!/usr/bin/env python3
# Returning multiple values (tuple)

def get_user_info():
    name = "Alice"
    age = 25
    city = "Boston"
    return name, age, city  # Returns tuple

def divide_with_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

# Unpack multiple return values
user_name, user_age, user_city = get_user_info()
print(f"Name: {user_name}")
print(f"Age: {user_age}")
print(f"City: {user_city}")

print("---")

q, r = divide_with_remainder(17, 5)
print(f"17 divided by 5: quotient={q}, remainder={r}")

# Can also get as tuple
result = divide_with_remainder(23, 7)
print(f"Result tuple: {result}")
