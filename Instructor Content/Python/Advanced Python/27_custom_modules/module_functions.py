#!/usr/bin/env python3
# Module with multiple functions

def calculate_area(length, width):
    """Calculate rectangle area"""
    return length * width

def calculate_perimeter(length, width):
    """Calculate rectangle perimeter"""
    return 2 * (length + width)

def calculate_circle_area(radius):
    """Calculate circle area"""
    pi = 3.14159
    return pi * radius ** 2

def format_currency(amount):
    """Format number as currency"""
    return f"${amount:.2f}"

# Test functions if running directly
if __name__ == "__main__":
    area = calculate_area(10, 5)
    print(f"Area: {area}")
    
    perimeter = calculate_perimeter(10, 5)
    print(f"Perimeter: {perimeter}")
    
    circle = calculate_circle_area(7)
    print(f"Circle area: {circle:.2f}")
    
    price = format_currency(19.99)
    print(f"Price: {price}")
