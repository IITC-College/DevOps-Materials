#!/usr/bin/env python3
# Functions must be defined before calling

def first_function():
    print("This is defined first")

def second_function():
    print("This is defined second")

# Call them - order of definition doesn't matter
# as long as they're defined before we call them
second_function()
first_function()

# This would cause an error:
# third_function()  # NameError: name 'third_function' is not defined
