#!/usr/bin/env python3
# Step 28: Same as step 27 (venv is environment setup, not code change)

# Import from our custom module
from helper_functions import (
    format_message,
    validate_command,
    show_config,
    print_header
)

# Configuration dictionary
config = {
    "app_name": "DevOps Helper",
    "version": 1.7,
    "status": "active",
    "ready": True,
    "max_retries": 3,
    "log_level": "INFO"
}

# List of valid commands
commands = ["status", "backup", "help", "config", "exit"]

# Use imported functions
print_header()
print(format_message(f"{config['app_name']} v{config['version']}"))
print(format_message(f"Status: {config['status']}"))
print_header()

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
    
    if command == "backup" and config.get("ready", False):
        print(format_message("Starting backup", "ACTION"))
    elif command == "backup" and not config.get("ready", False):
        print(format_message("System not ready for backup", "WARNING"))
    elif command == "status":
        print(format_message(f"{config['app_name']} is running", "STATUS"))
        print(f"  Version: {config['version']}")
        print(f"  Status: {config['status']}")
    elif command == "config":
        show_config(config)
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
