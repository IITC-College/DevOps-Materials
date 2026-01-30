#!/usr/bin/env python3
# Step 9: Using logical operators

# This is the DevOps Helper script
app_name = "DevOps Helper"
version = 1.1
status = "active"
ready = True

print(f"{app_name} v{version}")
print(f"Status: {status}")

# Get user input
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

# Get command
command = input("Enter command (status/backup/help): ")

# Using logical operators
if command == "backup" and ready:
    print("Starting backup")
elif command == "backup" and not ready:
    print("System not ready for backup")
elif command == "status":
    print("System is running")
elif command == "help":
    print("Available commands: status, backup, help")
else:
    print("Unknown command")
