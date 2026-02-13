#!/usr/bin/env python3
# Step 4: Adding error handling with try/except

import sys
import json
import datetime

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
    "version": 2.4,
    "status": "active",
    "ready": True,
    "max_retries": 3,
    "log_level": "INFO",
    "log_file": "devops_helper.log"
}

# List of valid commands
commands = ["status", "backup", "help", "config", "exit"]

def format_message_colored(message, prefix="INFO"):
    """Return a formatted message with color"""
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
    else:
        color = Fore.WHITE
    
    return f"[{timestamp}] {color}[{prefix}]{Style.RESET_ALL} {message}"

def log_to_file(message, prefix="INFO"):
    """Write log message to file with error handling"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] [{prefix}] {message}\n"
    
    try:
        with open(config['log_file'], 'a') as f:
            f.write(log_message)
    except PermissionError:
        print(format_message_colored(f"Permission denied: Cannot write to {config['log_file']}", "ERROR"))
    except IOError as e:
        print(format_message_colored(f"IO Error writing log: {e}", "ERROR"))
    except Exception as e:
        print(format_message_colored(f"Unexpected error writing log: {e}", "ERROR"))

def save_backup_report(backup_info):
    """Save backup report to file with error handling"""
    report_file = "backup_report.txt"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        with open(report_file, 'w') as f:
            f.write("=" * 50 + "\n")
            f.write("BACKUP REPORT\n")
            f.write("=" * 50 + "\n")
            f.write(f"Timestamp: {timestamp}\n")
            f.write(f"Status: {backup_info['status']}\n")
            f.write(f"Files backed up: {backup_info['files_count']}\n")
            f.write(f"Total size: {backup_info['total_size']} MB\n")
            f.write("=" * 50 + "\n")
        print(format_message_colored(f"Backup report saved to {report_file}", "INFO"))
        log_to_file(f"Backup report saved to {report_file}")
    except PermissionError:
        print(format_message_colored(f"Permission denied: Cannot write {report_file}", "ERROR"))
        log_to_file(f"Permission error saving report", "ERROR")
    except Exception as e:
        print(format_message_colored(f"Error saving report: {e}", "ERROR"))
        log_to_file(f"Error saving report: {e}", "ERROR")

def load_config(filename):
    """Load configuration from JSON file with error handling"""
    try:
        with open(filename, 'r') as f:
            loaded_config = json.load(f)
            print(format_message_colored(f"Loaded config from {filename}", "INFO"))
            log_to_file(f"Loaded config from {filename}")
            return loaded_config
    except FileNotFoundError:
        print(format_message_colored(f"Config file {filename} not found, using defaults", "WARNING"))
        log_to_file(f"Config file not found: {filename}", "WARNING")
        return None
    except json.JSONDecodeError as e:
        print(format_message_colored(f"Invalid JSON in {filename}: {e}", "ERROR"))
        log_to_file(f"Invalid JSON in config file: {filename}", "ERROR")
        return None
    except PermissionError:
        print(format_message_colored(f"Permission denied reading {filename}", "ERROR"))
        log_to_file(f"Permission denied: {filename}", "ERROR")
        return None
    except Exception as e:
        print(format_message_colored(f"Unexpected error loading config: {e}", "ERROR"))
        log_to_file(f"Unexpected error loading config: {e}", "ERROR")
        return None

def show_usage():
    """Show usage information"""
    print(f"Usage: python {sys.argv[0]} [--config FILE] <command>")
    print(f"\nOptions:")
    print(f"  --config FILE    Load configuration from FILE")
    print(f"\nAvailable commands:")
    for cmd in commands:
        print(f"  - {cmd}")

# Log startup
try:
    log_to_file(f"{config['app_name']} v{config['version']} started")
except Exception as e:
    print(f"Warning: Could not write to log: {e}")

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
    log_to_file(f"Command executed: {command}")
    
    try:
        if command == "backup" and config.get("ready", False):
            print(format_message_colored("Starting backup", "ACTION"))
            log_to_file("Backup started", "ACTION")
            
            # Simulate backup
            backup_info = {
                "status": "success",
                "files_count": 127,
                "total_size": 45.2
            }
            save_backup_report(backup_info)
            log_to_file("Backup completed successfully", "ACTION")
            
        elif command == "backup" and not config.get("ready", False):
            print(format_message_colored("System not ready for backup", "WARNING"))
            log_to_file("Backup failed: system not ready", "WARNING")
        elif command == "status":
            print(format_message_colored(f"{config['app_name']} is running", "STATUS"))
            print(f"  Version: {config['version']}")
            print(f"  Status: {config['status']}")
            log_to_file("Status check performed")
        elif command == "config":
            show_config(config)
            log_to_file("Config displayed")
        elif command == "help":
            show_usage()
        else:
            if not validate_command(command, commands):
                print(format_message_colored(f"Unknown command: {command}", "ERROR"))
                log_to_file(f"Unknown command attempted: {command}", "ERROR")
                show_usage()
    except Exception as e:
        print(format_message_colored(f"Error executing command: {e}", "ERROR"))
        log_to_file(f"Command execution error: {e}", "ERROR")
else:
    print()
    show_usage()

print(f"\n✓ Activity logged to: {config['log_file']}")
