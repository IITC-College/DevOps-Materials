#!/usr/bin/env python3
# Return vs print - important difference!

def add_with_print(a, b):
    result = a + b
    print(result)  # Just prints, returns None

def add_with_return(a, b):
    result = a + b
    return result  # Returns the value

# With print - can't use the value
add_with_print(5, 3)  # Prints 8
value1 = add_with_print(5, 3)  # Prints 8, value1 is None
print(f"Value1: {value1}")  # None

print("---")

# With return - can use the value
value2 = add_with_return(5, 3)  # Returns 8
print(f"Value2: {value2}")  # 8
double = value2 * 2
print(f"Double: {double}")  # 16
