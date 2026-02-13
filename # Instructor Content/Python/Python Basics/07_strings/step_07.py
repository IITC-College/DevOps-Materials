#!/usr/bin/env python3
# Step 7: String formatting

# This is the DevOps Helper script
app_name = "DevOps Helper"
version = 1.1
status = "active"

# Using f-strings for better output
print(f"{app_name} v{version}")
print(f"Status: {status}")

# Get user input
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")
print(f"Welcome to {app_name}")
