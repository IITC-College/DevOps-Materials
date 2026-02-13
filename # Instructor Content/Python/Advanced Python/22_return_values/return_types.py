#!/usr/bin/env python3
# Returning different types

def get_count():
    return 42  # int

def get_price():
    return 19.99  # float

def get_name():
    return "Alice"  # str

def is_valid():
    return True  # bool

def get_items():
    return [1, 2, 3, 4, 5]  # list

def get_config():
    return {"host": "localhost", "port": 8080}  # dict

# Use different return types
count = get_count()
price = get_price()
name = get_name()
valid = is_valid()
items = get_items()
config = get_config()

print(f"Count: {count}")
print(f"Price: ${price}")
print(f"Name: {name}")
print(f"Valid: {valid}")
print(f"Items: {items}")
print(f"Config: {config}")
