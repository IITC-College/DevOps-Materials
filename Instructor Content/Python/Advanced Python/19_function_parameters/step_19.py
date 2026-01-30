#!/usr/bin/env python3
# Step 19: Functions with parameters

# This is the DevOps Helper script
app_name = "DevOps Helper"
version = 1.1
status = "active"
ready = True

# List of valid commands
commands = ["status", "backup", "help", "exit"]

def print_header():
    """Print decorative header lines"""
    for i in range(3):
        print("=" * 20)

def print_message(message, prefix=""):
    """Print a message with optional prefix"""
    if prefix:
        print(f"{prefix}: {message}")
    else:
        print(message)

print_message(f"{app_name} v{version}")
print_message(status, "Status")
print_message(f"You have {len(commands)} available commands", "Info")

print_header()

# Get user input
user_name = input("Enter your name: ")
print_message(f"Hello, {user_name}!")

# Loop until valid command or exit
while True:
    command = input("Enter command: ")
    
    # Skip empty input
    if command == "":
        continue
    
    if command == "backup" and ready:
        print_message("Starting backup", "Action")
    elif command == "backup" and not ready:
        print_message("System not ready for backup", "Warning")
    elif command == "status":
        print_message("System is running", "Status")
    elif command == "help":
        print_message(f"Available commands ({len(commands)}):", "Help")
        for cmd in commands:
            print(f"  - {cmd}")
    elif command == "exit":
        print_message("Goodbye!")
        break
    else:
        print_message("Unknown command", "Error")
        print("Valid commands are:")
        for cmd in commands:
            print(f"  - {cmd}")
