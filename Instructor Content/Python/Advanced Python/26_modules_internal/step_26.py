#!/usr/bin/env python3
# Step 26: Using built-in modules

import datetime

# Configuration dictionary
config = {
    "app_name": "DevOps Helper",
    "version": 1.6,
    "status": "active",
    "ready": True,
    "max_retries": 3,
    "log_level": "INFO"
}

# List of valid commands
commands = ["status", "backup", "help", "config", "exit"]

def get_timestamp():
    """Return current timestamp"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def format_message(message, prefix="INFO"):
    """Return a formatted message with timestamp"""
    timestamp = get_timestamp()
    return f"[{timestamp}] [{prefix}] {message}"

def validate_command(cmd, valid_commands):
    """Return True if command is valid"""
    return cmd in valid_commands

def show_config(cfg):
    """Display configuration using loop"""
    print("Configuration:")
    for key, value in cfg.items():
        print(f"  {key}: {value}")

# Use dictionary with timestamp
print(format_message(f"{config['app_name']} v{config['version']}"))
print(format_message(f"Status: {config['status']}"))
print(format_message(f"Started at {get_timestamp()}"))

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
        print(f"  Current time: {get_timestamp()}")
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
