#!/usr/bin/env python3
# Step 23: Using dictionaries for configuration

# Configuration dictionary
config = {
    "app_name": "DevOps Helper",
    "version": 1.3,
    "status": "active",
    "ready": True
}

# List of valid commands
commands = ["status", "backup", "help", "exit"]

def get_header_line(char="=", length=20):
    """Return a header line string"""
    return char * length

def format_message(message, prefix="INFO"):
    """Return a formatted message"""
    return f"[{prefix}] {message}"

def validate_command(cmd, valid_commands):
    """Return True if command is valid"""
    return cmd in valid_commands

# Use dictionary values
print(format_message(f"{config['app_name']} v{config['version']}"))
print(format_message(f"Status: {config['status']}"))

for i in range(3):
    print(get_header_line())

# Get user input
user_name = input("Enter your name: ")
if user_name:
    print(format_message(f"Hello, {user_name}!"))

# Loop until valid command or exit
while True:
    command = input("Enter command: ").strip()
    
    # Skip empty input
    if command == "":
        continue
    
    if command == "backup" and config["ready"]:
        print(format_message("Starting backup", "ACTION"))
    elif command == "backup" and not config["ready"]:
        print(format_message("System not ready for backup", "WARNING"))
    elif command == "status":
        print(format_message(f"{config['app_name']} is running", "STATUS"))
        print(f"  Version: {config['version']}")
        print(f"  Status: {config['status']}")
    elif command == "help":
        print(format_message(f"Available commands ({len(commands)}):", "HELP"))
        for cmd in commands:
            print(f"  - {cmd}")
    elif command == "exit":
        print(format_message("Goodbye!"))
        break
    else:
        if not validate_command(command, commands):
            print(format_message("Unknown command", "ERROR"))
