#!/usr/bin/env python3
# Step 21: Functions with default parameters

# This is the DevOps Helper script
app_name = "DevOps Helper"
version = 1.1
status = "active"
ready = True

# List of valid commands
commands = ["status", "backup", "help", "exit"]

def print_header(char="=", length=20, lines=3):
    """Print decorative header lines with defaults"""
    for i in range(lines):
        print(char * length)

def print_message(message, prefix="INFO"):
    """Print a message with default prefix"""
    print(f"[{prefix}] {message}")

def greet_user(name="Guest"):
    """Greet user with default name"""
    print(f"Hello, {name}!")

# Use defaults
print_message(f"{app_name} v{version}")
print_message(f"Status: {status}")

# Override defaults
print_header(char="-", length=30)

# Get user input
user_name = input("Enter your name (or press Enter for 'Guest'): ")
if user_name:
    greet_user(user_name)
else:
    greet_user()  # Use default

# Loop until valid command or exit
while True:
    command = input("Enter command: ")
    
    # Skip empty input
    if command == "":
        continue
    
    if command == "backup" and ready:
        print_message("Starting backup", "ACTION")
    elif command == "backup" and not ready:
        print_message("System not ready for backup", "WARNING")
    elif command == "status":
        print_message("System is running")
    elif command == "help":
        print_message(f"Available commands ({len(commands)}):", "HELP")
        for cmd in commands:
            print(f"  - {cmd}")
    elif command == "exit":
        print_message("Goodbye!")
        break
    else:
        print_message("Unknown command", "ERROR")
