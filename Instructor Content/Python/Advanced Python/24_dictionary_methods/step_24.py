#!/usr/bin/env python3
# Step 24: Using dictionary methods

# Configuration dictionary
config = {
    "app_name": "DevOps Helper",
    "version": 1.4,
    "status": "active",
    "ready": True,
    "max_retries": 3
}

# List of valid commands
commands = ["status", "backup", "help", "config", "exit"]

def format_message(message, prefix="INFO"):
    """Return a formatted message"""
    return f"[{prefix}] {message}"

def validate_command(cmd, valid_commands):
    """Return True if command is valid"""
    return cmd in valid_commands

# Use dictionary methods
print(format_message(f"{config.get('app_name', 'Unknown')} v{config.get('version', '0.0')}"))
print(format_message(f"Status: {config.get('status', 'unknown')}"))

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
        print(format_message("Configuration:", "INFO"))
        for key in config.keys():
            print(f"  {key}: {config[key]}")
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
