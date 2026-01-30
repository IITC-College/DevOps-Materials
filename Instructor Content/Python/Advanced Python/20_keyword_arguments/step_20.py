#!/usr/bin/env python3
# Step 20: Using keyword arguments

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

def show_status(app, ver, active=True):
    """Display application status information"""
    print(f"App: {app}")
    print(f"Version: {ver}")
    if active:
        print("Status: Active")
    else:
        print("Status: Inactive")

# Using keyword arguments for clarity
show_status(app=app_name, ver=version, active=(status == "active"))

print_header()

# Get user input
user_name = input("Enter your name: ")
print_message(message=f"Hello, {user_name}!")

# Loop until valid command or exit
while True:
    command = input("Enter command: ")
    
    # Skip empty input
    if command == "":
        continue
    
    if command == "backup" and ready:
        print_message(message="Starting backup", prefix="Action")
    elif command == "backup" and not ready:
        print_message(prefix="Warning", message="System not ready for backup")
    elif command == "status":
        show_status(app=app_name, ver=version)
    elif command == "help":
        print_message(f"Available commands ({len(commands)}):", "Help")
        for cmd in commands:
            print(f"  - {cmd}")
    elif command == "exit":
        print_message("Goodbye!")
        break
    else:
        print_message(message="Unknown command", prefix="Error")
        print("Valid commands are:")
        for cmd in commands:
            print(f"  - {cmd}")
