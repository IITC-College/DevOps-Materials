#!/usr/bin/env python3
# Step 8: Using conditions

# This is the DevOps Helper script
app_name = "DevOps Helper"
version = 1.1
status = "active"

print(f"{app_name} v{version}")
print(f"Status: {status}")

# Get user input
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

# Get command
command = input("Enter command (status/backup/help): ")

if command == "status":
    print("System is running")
elif command == "backup":
    print("Starting backup")
elif command == "help":
    print("Available commands: status, backup, help")
else:
    print("Unknown command")
