#!/usr/bin/env python3
# Demonstrating function reusability

def greet(name):
    print(f"Hello, {name}!")
    print("Welcome to our system")
    print("-" * 30)

# Use the same function multiple times
greet("Alice")
greet("Bob")
greet("Charlie")
greet("David")

# One function definition, many uses
