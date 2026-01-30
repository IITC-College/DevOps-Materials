#!/usr/bin/env python3
# Using returned values in different ways

def calculate_total(price, quantity):
    return price * quantity

def is_adult(age):
    return age >= 18

def get_discount(is_member):
    if is_member:
        return 0.10
    else:
        return 0.0

# Store in variable
total = calculate_total(10.50, 3)
print(f"Total: ${total}")

# Use in condition
age = 25
if is_adult(age):
    print(f"{age} is an adult")

# Use in calculation
member = True
discount = get_discount(member)
final_price = total * (1 - discount)
print(f"Final price with discount: ${final_price:.2f}")

# Use directly in expression
print(f"Is 15 an adult? {is_adult(15)}")
