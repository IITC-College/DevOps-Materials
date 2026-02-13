#!/usr/bin/env python3
# Function with multiple parameters

def calculate_total(price, quantity, tax_rate):
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    print(f"Price: ${price}, Qty: {quantity}, Tax: {tax_rate}")
    print(f"Total: ${total}")

def create_user(username, email, age, country):
    print(f"Creating user:")
    print(f"  Username: {username}")
    print(f"  Email: {email}")
    print(f"  Age: {age}")
    print(f"  Country: {country}")

# Call with multiple arguments
calculate_total(10.00, 3, 0.08)
print("---")
create_user("alice", "alice@example.com", 25, "USA")
