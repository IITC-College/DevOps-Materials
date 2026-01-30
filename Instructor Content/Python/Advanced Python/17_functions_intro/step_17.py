#!/usr/bin/env python3
# Step 17: Identifying code that could be functions

# This is the DevOps Helper script
app_name = "DevOps Helper"
version = 1.1
status = "active"
ready = True

# List of valid commands
commands = ["status", "backup", "help", "exit"]

print(f"{app_name} v{version}")
print(f"Status: {status}")
print(f"You have {len(commands)} available commands")

# TODO: This repeating pattern could be a print_header() function
for i in range(3):
    print("=" * 20)

# Get user input
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

# TODO: The main loop logic could be organized into functions
# Loop until valid command or exit
while True:
    command = input("Enter command: ")
    
    # Skip empty input
    if command == "":
        continue
    
    # TODO: Each command handler could be a separate function
    if command == "backup" and ready:
        print("Starting backup")
    elif command == "backup" and not ready:
        print("System not ready for backup")
    elif command == "status":
        print("System is running")
    elif command == "help":
        # TODO: This menu display could be a show_menu() function
        print(f"Available commands ({len(commands)}):")
        for cmd in commands:
            print(f"  - {cmd}")
    elif command == "exit":
        print("Goodbye!")
        break
    else:
        # TODO: Repeating the menu display - definitely needs a function!
        print("Unknown command")
        print("Valid commands are:")
        for cmd in commands:
            print(f"  - {cmd}")
