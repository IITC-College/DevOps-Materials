#!/usr/bin/env python3
# Step 2: Reading configuration from files

import sys
import json

# Note: This requires: pip install colorama
try:
    from colorama import Fore, Style, init
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

# Default configuration
config = {
    "app_name": "DevOps Helper",
    "version": 2.2,
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

def load_config(filename):
    """Load configuration from JSON file"""
    try:
        with open(filename, 'r') as f:
            loaded_config = json.load(f)
            print(format_message_colored(f"Loaded config from {filename}", "INFO"))
            return loaded_config
    except FileNotFoundError:
        print(format_message_colored(f"Config file {filename} not found, using defaults", "WARNING"))
        return None
    except json.JSONDecodeError:
        print(format_message_colored(f"Invalid JSON in {filename}, using defaults", "ERROR"))
        return None

def show_usage():
    """Show usage information"""
    print(f"Usage: python {sys.argv[0]} [--config FILE] <command>")
    print(f"\nOptions:")
    print(f"  --config FILE    Load configuration from FILE")
    print(f"\nAvailable commands:")
    for cmd in commands:
        print(f"  - {cmd}")
    print(f"\nExamples:")
    print(f"  python {sys.argv[0]} status")
    print(f"  python {sys.argv[0]} --config myconfig.json backup")

# Parse arguments
config_file = None
command = None

i = 1
while i < len(sys.argv):
    if sys.argv[i] == '--config' and i + 1 < len(sys.argv):
        config_file = sys.argv[i + 1]
        i += 2
    else:
        command = sys.argv[i]
        i += 1

# Load config if specified
if config_file:
    loaded = load_config(config_file)
    if loaded:
        config.update(loaded)

# Show header
if COLORAMA_AVAILABLE:
    print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)
    print(Fore.GREEN + f"{config['app_name']} v{config['version']}" + Style.RESET_ALL)
else:
    print("=" * 50)
    print(f"{config['app_name']} v{config['version']}")

# Execute command if provided
if command:
    print(format_message_colored(f"Command: {command}"))
    
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
    else:
        if not validate_command(command, commands):
            print(format_message_colored(f"Unknown command: {command}", "ERROR"))
            show_usage()
else:
    print()
    show_usage()
