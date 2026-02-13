#!/usr/bin/env python3
# Step 6: Replacing print with logging module

import sys
import json
import logging
import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('devops_helper.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Note: This requires: pip install colorama
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False
    logger.warning("colorama not installed, colors disabled")

# Import from our custom module
from helper_functions import (
    validate_command,
    show_config,
    print_header
)

# Exit codes
EXIT_SUCCESS = 0
EXIT_ERROR = 1
EXIT_INVALID_ARGS = 2
EXIT_FILE_ERROR = 3
EXIT_PERMISSION_ERROR = 4

# Default configuration
config = {
    "app_name": "DevOps Helper",
    "version": 2.6,
    "status": "active",
    "ready": True,
    "max_retries": 3,
    "log_level": "INFO"
}

# List of valid commands
commands = ["status", "backup", "help", "config", "exit"]

def format_message_colored(message, prefix="INFO"):
    """Return a formatted message with color"""
    if not COLORAMA_AVAILABLE:
        return message
    
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
    
    return f"{color}{message}{Style.RESET_ALL}"

def save_backup_report(backup_info):
    """Save backup report to file"""
    report_file = "backup_report.txt"
    
    try:
        with open(report_file, 'w') as f:
            f.write("=" * 50 + "\n")
            f.write("BACKUP REPORT\n")
            f.write("=" * 50 + "\n")
            f.write(f"Timestamp: {datetime.datetime.now().isoformat()}\n")
            f.write(f"Status: {backup_info['status']}\n")
            f.write(f"Files backed up: {backup_info['files_count']}\n")
            f.write(f"Total size: {backup_info['total_size']} MB\n")
            f.write("=" * 50 + "\n")
        logger.info(f"Backup report saved to {report_file}")
        return True
    except PermissionError:
        logger.error(f"Permission denied: Cannot write {report_file}")
        return False
    except Exception as e:
        logger.error(f"Error saving report: {e}")
        return False

def load_config(filename):
    """Load configuration from JSON file"""
    try:
        with open(filename, 'r') as f:
            loaded_config = json.load(f)
            logger.info(f"Loaded config from {filename}")
            return loaded_config
    except FileNotFoundError:
        logger.error(f"Config file {filename} not found")
        sys.exit(EXIT_FILE_ERROR)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in {filename}")
        sys.exit(EXIT_ERROR)
    except PermissionError:
        logger.error(f"Permission denied reading {filename}")
        sys.exit(EXIT_PERMISSION_ERROR)

def show_usage():
    """Show usage information"""
    print(f"Usage: python {sys.argv[0]} [--config FILE] <command>")
    print(f"\nOptions:")
    print(f"  --config FILE    Load configuration from FILE")
    print(f"\nAvailable commands:")
    for cmd in commands:
        print(f"  - {cmd}")

# Log startup
logger.info(f"{config['app_name']} v{config['version']} started")

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
    logger.info(f"Command executed: {command}")
    
    if command == "backup" and config.get("ready", False):
        print(format_message_colored("Starting backup", "ACTION"))
        logger.info("Backup started")
        
        # Simulate backup
        backup_info = {
            "status": "success",
            "files_count": 127,
            "total_size": 45.2
        }
        
        if save_backup_report(backup_info):
            logger.info("Backup completed successfully")
            print("\n✓ Backup completed successfully")
            sys.exit(EXIT_SUCCESS)
        else:
            logger.error("Backup failed")
            print("\n✗ Backup failed")
            sys.exit(EXIT_FILE_ERROR)
        
    elif command == "backup" and not config.get("ready", False):
        print(format_message_colored("System not ready for backup", "WARNING"))
        logger.warning("Backup failed: system not ready")
        sys.exit(EXIT_ERROR)
        
    elif command == "status":
        print(format_message_colored(f"{config['app_name']} is running", "STATUS"))
        print(f"  Version: {config['version']}")
        print(f"  Status: {config['status']}")
        logger.info("Status check performed")
        sys.exit(EXIT_SUCCESS)
        
    elif command == "config":
        show_config(config)
        logger.info("Config displayed")
        sys.exit(EXIT_SUCCESS)
        
    elif command == "help"):
        show_usage()
        sys.exit(EXIT_SUCCESS)
        
    elif command == "exit":
        print("Goodbye!")
        logger.info("Application exited normally")
        sys.exit(EXIT_SUCCESS)
        
    else:
        if not validate_command(command, commands):
            logger.error(f"Unknown command attempted: {command}")
            print(f"Error: Unknown command '{command}'")
            show_usage()
            sys.exit(EXIT_INVALID_ARGS)
else:
    print()
    show_usage()
    sys.exit(EXIT_INVALID_ARGS)
