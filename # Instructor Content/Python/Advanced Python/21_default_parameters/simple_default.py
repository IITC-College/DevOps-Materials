#!/usr/bin/env python3
# Simple default parameter

def greet(name="World"):
    print(f"Hello, {name}!")

# Use default
greet()

# Override default
greet("Alice")
greet("Bob")
