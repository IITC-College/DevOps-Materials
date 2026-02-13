#!/usr/bin/env python3
# Using if __name__ == "__main__" pattern

def calculate(x, y):
    """Calculate sum"""
    return x + y

def display_result(result):
    """Display result"""
    print(f"Result: {result}")

# This code only runs when script is executed directly
# Not when imported as a module
if __name__ == "__main__":
    print("Running as main script")
    result = calculate(10, 20)
    display_result(result)
    
    # Test more
    test_values = [(1, 2), (5, 10), (100, 200)]
    for a, b in test_values:
        print(f"{a} + {b} = {calculate(a, b)}")
else:
    print("Imported as a module")
