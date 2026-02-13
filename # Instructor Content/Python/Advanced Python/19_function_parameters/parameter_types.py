#!/usr/bin/env python3
# Functions with different parameter types

def process_string(text):
    print(f"Text: {text}")
    print(f"Length: {len(text)}")

def process_number(value):
    print(f"Number: {value}")
    print(f"Doubled: {value * 2}")

def process_boolean(flag):
    if flag:
        print("Flag is True")
    else:
        print("Flag is False")

def process_list(items):
    print(f"Items: {items}")
    print(f"Count: {len(items)}")

# Different types as parameters
process_string("Hello")
process_number(42)
process_boolean(True)
process_list([1, 2, 3])
