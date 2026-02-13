#!/usr/bin/env python3
# Step 7: Using different log levels

import sys
import json
import logging

# Configure logging with different levels
logging.basicConfig(
    level=logging.DEBUG,  # Show all levels
    format='[%(asctime)s] [%(levelname)-8s] %(message)s',
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

# Default configuration
config = {
    "app_name": "DevOps Helper",
    "version": 2.7,
    "status": "active",
    "ready": True,
    "max_retries": 3,
    "log_level": "INFO"
}

commands = ["status", "backup", "help", "config", "exit"]

def save_backup_report(backup_info):
    """Save backup report"""
    report_file = "backup_report.txt"
    logger.debug(f"Attempting to save backup report to {report_file}")
    
    try:
        with open(report_file, 'w') as f:
            f.write("=" * 50 + "\n")
            f.write("BACKUP REPORT\n")
            f.write("=" * 50 + "\n")
            for key, value in backup_info.items():
                f.write(f"{key}: {value}\n")
            f.write("=" * 50 + "\n")
        logger.info(f"Backup report saved successfully to {report_file}")
        return True
    except PermissionError:
        logger.error(f"Permission denied writing to {report_file}")
        return False
    except Exception as e:
        logger.critical(f"Critical error saving report: {e}")
        return False

def load_config(filename):
    """Load configuration"""
    logger.debug(f"Attempting to load config from {filename}")
    try:
        with open(filename, 'r') as f:
            loaded_config = json.load(f)
            logger.info(f"Successfully loaded config from {filename}")
            return loaded_config
    except FileNotFoundError:
        logger.error(f"Config file {filename} not found")
        sys.exit(EXIT_FILE_ERROR)
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in {filename}")
        sys.exit(EXIT_ERROR)

def show_usage():
    """Show usage"""
    print(f"Usage: python {sys.argv[0]} [--config FILE] [--log-level LEVEL] <command>")
    print(f"\nOptions:")
    print(f"  --config FILE       Load configuration from FILE")
    print(f"  --log-level LEVEL   Set log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)")
    print(f"\nCommands:")
    for cmd in commands:
        print(f"  - {cmd}")

# Log startup
logger.info(f"{config['app_name']} v{config['version']} starting")
logger.debug("Debug mode enabled")

# Parse arguments
config_file = None
command = None
log_level = None

i = 1
while i < len(sys.argv):
    if sys.argv[i] == '--config' and i + 1 < len(sys.argv):
        config_file = sys.argv[i + 1]
        i += 2
    elif sys.argv[i] == '--log-level' and i + 1 < len(sys.argv):
        log_level = sys.argv[i + 1].upper()
        i += 2
    else:
        command = sys.argv[i]
        i += 1

# Set log level if specified
if log_level:
    numeric_level = getattr(logging, log_level, None)
    if isinstance(numeric_level, int):
        logger.setLevel(numeric_level)
        logger.info(f"Log level set to {log_level}")
    else:
        logger.warning(f"Invalid log level: {log_level}")

# Load config if specified
if config_file:
    loaded = load_config(config_file)
    if loaded:
        config.update(loaded)
        logger.debug(f"Config updated: {config}")

# Show header
print("=" * 50)
print(f"{config['app_name']} v{config['version']}")
print("=" * 50)

# Execute command
if command:
    logger.info(f"Executing command: {command}")
    
    if command == "backup":
        logger.debug("Backup command initiated")
        if config.get("ready", False):
            logger.info("System ready for backup")
            print("Starting backup...")
            
            backup_info = {
                "status": "success",
                "files_count": 127,
                "total_size": "45.2 MB"
            }
            
            if save_backup_report(backup_info):
                logger.info("Backup completed successfully")
                print("✓ Backup completed")
                sys.exit(EXIT_SUCCESS)
            else:
                logger.error("Backup failed")
                sys.exit(EXIT_ERROR)
        else:
            logger.warning("System not ready for backup")
            print("System not ready")
            sys.exit(EXIT_ERROR)
            
    elif command == "status":
        logger.debug("Status command executed")
        print(f"Status: {config['status']}")
        logger.info("Status check completed")
        sys.exit(EXIT_SUCCESS)
        
    elif command == "config":
        logger.debug("Displaying configuration")
        show_config(config)
        sys.exit(EXIT_SUCCESS)
        
    elif command == "help":
        show_usage()
        sys.exit(EXIT_SUCCESS)
        
    elif command == "exit":
        logger.info("Application shutting down normally")
        print("Goodbye!")
        sys.exit(EXIT_SUCCESS)
        
    else:
        logger.error(f"Unknown command: {command}")
        print(f"Error: Unknown command '{command}'")
        show_usage()
        sys.exit(EXIT_INVALID_ARGS)
else:
    logger.warning("No command provided")
    show_usage()
    sys.exit(EXIT_INVALID_ARGS)
