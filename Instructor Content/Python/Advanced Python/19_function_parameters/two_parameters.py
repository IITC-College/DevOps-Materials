#!/usr/bin/env python3
# Function with two parameters

def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

def greet_with_title(title, name):
    print(f"Hello, {title} {name}")

# Call with different arguments
add(5, 3)
add(10, 20)

greet_with_title("Dr.", "Smith")
greet_with_title("Ms.", "Johnson")
