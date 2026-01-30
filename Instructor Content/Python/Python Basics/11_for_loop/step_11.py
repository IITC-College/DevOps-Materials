#!/usr/bin/env python3
# Step 11: Using for loop

# This is the DevOps Helper script
app_name = "DevOps Helper"
version = 1.1
status = "active"
ready = True

print(f"{app_name} v{version}")
print(f"Status: {status}")

# Print header multiple times
for i in range(3):
    print("=" * 20)

# Get user input
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

# Loop until valid command or exit
while True:
    command = input("Enter command (status/backup/help/exit): ")
    
    if command == "backup" and ready:
        print("Starting backup")
    elif command == "backup" and not ready:
        print("System not ready for backup")
    elif command == "status":
        print("System is running")
    elif command == "help":
        print("Available commands: status, backup, help, exit")
    elif command == "exit":
        print("Goodbye!")
        break
    else:
        print("Unknown command")
