#!/usr/bin/env python3
# Step 13: Using lists

# This is the DevOps Helper script
app_name = "DevOps Helper"
version = 1.1
status = "active"
ready = True

# List of valid commands
commands = ["status", "backup", "help", "exit"]

print(f"{app_name} v{version}")
print(f"Status: {status}")
print(f"Available commands: {commands}")

# Print header multiple times
for i in range(3):
    print("=" * 20)

# Get user input
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

# Loop until valid command or exit
while True:
    command = input("Enter command: ")
    
    # Skip empty input
    if command == "":
        continue
    
    if command == "backup" and ready:
        print("Starting backup")
    elif command == "backup" and not ready:
        print("System not ready for backup")
    elif command == "status":
        print("System is running")
    elif command == "help":
        print(f"Available commands: {commands}")
    elif command == "exit":
        print("Goodbye!")
        break
    else:
        print("Unknown command")
