#!/usr/bin/env python3
# Step 1: Adding command-line argument support with sys.argv

import sys

# Note: This requires: pip install colorama
try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

# Import from our custom module
from helper_functions import (
    validate_command,
    show_config,
    print_header
)

# Configuration dictionary
config = {
    "app_name": "DevOps Helper",
    "version": 2.1,
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

def show_usage():
    """Show usage information"""
    print(f"Usage: python {sys.argv[0]} <command>")
    print(f"\nAvailable commands:")
    for cmd in commands:
        print(f"  - {cmd}")
    print(f"\nExamples:")
    print(f"  python {sys.argv[0]} status")
    print(f"  python {sys.argv[0]} backup")
    print(f"  python {sys.argv[0]} help")

# Check if command provided as argument
if len(sys.argv) > 1:
    command = sys.argv[1].lower()
    
    if COLORAMA_AVAILABLE:
        print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)
        print(Fore.GREEN + f"{config['app_name']} v{config['version']}" + Style.RESET_ALL)
    else:
        print("=" * 50)
        print(f"{config['app_name']} v{config['version']}")
    
    print(format_message_colored(f"Command from CLI: {command}"))
    
    if command == "backup" and config.get("ready", False):
        print(format_message_colored("Starting backup", "ACTION"))
    elif command == "backup" and not config.get("ready", False):
        print(format_message_colored("System not ready for backup", "WARNING"))
    elif command == "status":
        print(format_message_colored(f"{config['app_name']} is running", "STATUS"))
        print(f"  Version: {config['version']}")
        print(f"  Status: {config['status']}")
    elif command == "config":
        show_config(config)
    elif command == "help":
        show_usage()
    elif command == "exit":
        print(format_message_colored("Exiting..."))
    else:
        if not validate_command(command, commands):
            print(format_message_colored(f"Unknown command: {command}", "ERROR"))
            show_usage()
else:
    # No command provided, show usage
    print(f"{config['app_name']} v{config['version']}")
    print()
    show_usage()
