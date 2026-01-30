#!/usr/bin/env python3
# Functions that return None

def print_greeting():
    print("Hello!")
    # No return statement = returns None

def do_something():
    x = 10
    y = 20
    # No return = returns None

def explicit_none():
    return None

# All return None
result1 = print_greeting()
result2 = do_something()
result3 = explicit_none()

print(f"Result1: {result1}")  # None
print(f"Result2: {result2}")  # None
print(f"Result3: {result3}")  # None

# Check for None
if result1 is None:
    print("Result1 is None")
