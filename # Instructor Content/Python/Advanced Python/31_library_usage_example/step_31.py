#!/usr/bin/env python3
# Step 31: Using external library (colorama for colored output)

# Note: This requires: pip install colorama
try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)  # Auto-reset colors after each print
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False
    print("Note: colorama not installed. Install with: pip install colorama")
    print("Running without colors...\n")

# Import from our custom module
from helper_functions import (
    validate_command,
    show_config,
    print_header
)

# Configuration dictionary
config = {
    "app_name": "DevOps Helper",
    "version": 2.0,
    "status": "active",
    "ready": True,
    "max_retries": 3,
    "log_level": "INFO"
}

# List of valid commands
commands = ["status", "backup", "help", "config", "exit"]

def format_message_colored(message, prefix="INFO"):
    """Return a formatted message with color"""
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if not COLORAMA_AVAILABLE:
        return f"[{timestamp}] [{prefix}] {message}"
    
    # Color based on prefix
    if prefix == "ERROR":
        color = Fore.RED
    elif prefix == "WARNING":
        color = Fore.YELLOW
    elif prefix == "ACTION":
        color = Fore.GREEN
    elif prefix == "STATUS":
        color = Fore.CYAN
    elif prefix == "HELP":
        color = Fore.MAGENTA
    else:
        color = Fore.WHITE
    
    return f"[{timestamp}] {color}[{prefix}]{Style.RESET_ALL} {message}"

# Use colored output
if COLORAMA_AVAILABLE:
    print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)
    print(Fore.GREEN + f"{config['app_name']} v{config['version']}" + Style.RESET_ALL)
else:
    print("=" * 50)
    print(f"{config['app_name']} v{config['version']}")

print(format_message_colored(f"Status: {config['status']}"))

# Get user input
user_name = input("Enter your name: ")
if user_name:
    if COLORAMA_AVAILABLE:
        print(Fore.YELLOW + f"Hello, {user_name}!" + Style.RESET_ALL)
    else:
        print(f"Hello, {user_name}!")

# Loop until valid command or exit
while True:
    if COLORAMA_AVAILABLE:
        command = input(Fore.WHITE + "Enter command: " + Style.RESET_ALL).strip()
    else:
        command = input("Enter command: ").strip()
    
    # Skip empty input
    if command == "":
        continue
    
    if command == "backup" and config.get("ready", False):
        print(format_message_colored("Starting backup", "ACTION"))
    elif command == "backup" and not config.get("ready", False):
        print(format_message_colored("System not ready for backup", "WARNING"))
    elif command == "status":
        print(format_message_colored(f"{config['app_name']} is running", "STATUS"))
        if COLORAMA_AVAILABLE:
            print(Fore.CYAN + f"  Version: {config['version']}" + Style.RESET_ALL)
            print(Fore.CYAN + f"  Status: {config['status']}" + Style.RESET_ALL)
        else:
            print(f"  Version: {config['version']}")
            print(f"  Status: {config['status']}")
    elif command == "config":
        show_config(config)
    elif command == "help":
        print(format_message_colored(f"Available commands ({len(commands)}):", "HELP"))
        for cmd in commands:
            if COLORAMA_AVAILABLE:
                print(Fore.MAGENTA + f"  - {cmd}" + Style.RESET_ALL)
            else:
                print(f"  - {cmd}")
    elif command == "exit":
        print(format_message_colored("Goodbye!"))
        break
    else:
        if not validate_command(command, commands):
            print(format_message_colored("Unknown command", "ERROR"))
