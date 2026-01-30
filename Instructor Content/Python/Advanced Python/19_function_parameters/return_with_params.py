#!/usr/bin/env python3
# Functions with parameters that return values

def add(a, b):
    return a + b

def multiply(x, y):
    return x * y

def get_full_name(first, last):
    return f"{first} {last}"

def is_even(number):
    return number % 2 == 0

# Use the returned values
result1 = add(5, 3)
print(f"5 + 3 = {result1}")

result2 = multiply(4, 7)
print(f"4 * 7 = {result2}")

name = get_full_name("John", "Doe")
print(f"Full name: {name}")

print(f"Is 10 even? {is_even(10)}")
print(f"Is 7 even? {is_even(7)}")
