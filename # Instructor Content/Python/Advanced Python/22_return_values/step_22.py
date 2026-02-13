#!/usr/bin/env python3
# Step 22: Using return values

# This is the DevOps Helper script
app_name = "DevOps Helper"
version = 1.2
status = "active"
ready = True

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

def get_user_command():
    """Get and return user command"""
    return input("Enter command: ").strip()

# Use return values
header = get_header_line()
print(format_message(f"{app_name} v{version}"))
print(format_message(f"Status: {status}"))

for i in range(3):
    print(header)

# Get user input
user_name = input("Enter your name: ")
if user_name:
    print(format_message(f"Hello, {user_name}!"))

# Loop until valid command or exit
while True:
    command = get_user_command()
    
    # Skip empty input
    if command == "":
        continue
    
    # Check if command is valid
    is_valid = validate_command(command, commands)
    
    if command == "backup" and ready:
        print(format_message("Starting backup", "ACTION"))
    elif command == "backup" and not ready:
        print(format_message("System not ready for backup", "WARNING"))
    elif command == "status":
        print(format_message("System is running", "STATUS"))
    elif command == "help":
        print(format_message(f"Available commands ({len(commands)}):", "HELP"))
        for cmd in commands:
            print(f"  - {cmd}")
    elif command == "exit":
        print(format_message("Goodbye!"))
        break
    else:
        if not is_valid:
            print(format_message("Unknown command", "ERROR"))
            print("Valid commands are:")
            for cmd in commands:
                print(f"  - {cmd}")
