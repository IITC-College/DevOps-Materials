#!/usr/bin/env python3
# Function with one parameter

def greet(name):
    print(f"Hello, {name}!")

def square(number):
    result = number * number
    print(f"Square of {number} is {result}")

# Call with different arguments
greet("Alice")
greet("Bob")

square(5)
square(10)
