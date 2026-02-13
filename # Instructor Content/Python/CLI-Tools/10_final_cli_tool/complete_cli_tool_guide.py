#!/usr/bin/env python3
# Complete CLI Tool Development Guide

"""
COMPLETE GUIDE TO BUILDING PRODUCTION-READY CLI TOOLS IN PYTHON

This comprehensive guide covers everything needed to build professional CLI tools
"""

print("="*70)
print("COMPLETE CLI TOOL DEVELOPMENT GUIDE")
print("="*70)

# TABLE OF CONTENTS
print("\nTABLE OF CONTENTS:")
print("-"*70)

toc = """
1. Introduction
2. Core Components
3. Argument Parsing
4. Configuration Management
5. Logging
6. Error Handling
7. Exit Codes
8. User Interface
9. Testing
10. Distribution
11. Best Practices
12. Common Patterns
"""
print(toc)

# 1. INTRODUCTION
print("\n" + "="*70)
print("1. INTRODUCTION")
print("="*70)

intro = """
A production-ready CLI tool should:
  • Be easy to use
  • Handle errors gracefully
  • Provide helpful feedback
  • Be maintainable
  • Follow conventions
  • Be testable

Key Libraries:
  • argparse - Argument parsing
  • logging - Professional logging
  • pathlib - Path handling
  • json/yaml - Configuration
  • sys - Exit codes
"""
print(intro)

# 2. CORE COMPONENTS
print("\n" + "="*70)
print("2. CORE COMPONENTS")
print("="*70)

components = """
Every CLI tool needs:

1. ARGUMENT PARSER
   Parse and validate command-line arguments

2. CONFIGURATION LOADER
   Load settings from files and merge with defaults

3. LOGGING SETUP
   Configure logging to file and console

4. COMMAND HANDLERS
   Functions that implement each command

5. MAIN FUNCTION
   Coordinate all components and handle errors

6. ERROR HANDLING
   try/except blocks for all risky operations

7. EXIT CODES
   Return appropriate codes to shell
"""
print(components)

# 3. ARGUMENT PARSING
print("\n" + "="*70)
print("3. ARGUMENT PARSING")
print("="*70)

argparse_example = """
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description='My CLI Tool',
        epilog='Example: %(prog)s command --option'
    )
    
    # Global options
    parser.add_argument('--version', action='version', version='1.0')
    parser.add_argument('--config', help='Config file')
    parser.add_argument('--verbose', '-v', action='store_true')
    
    # Subcommands
    subparsers = parser.add_subparsers(dest='command')
    
    # status subcommand
    status = subparsers.add_parser('status', help='Show status')
    status.add_argument('--json', action='store_true')
    
    # deploy subcommand
    deploy = subparsers.add_parser('deploy', help='Deploy app')
    deploy.add_argument('env', choices=['dev', 'prod'])
    deploy.add_argument('--force', action='store_true')
    
    return parser.parse_args()

# Usage
args = parse_args()
print(f"Command: {args.command}")
"""
print(argparse_example)

# 4. CONFIGURATION
print("\n" + "="*70)
print("4. CONFIGURATION MANAGEMENT")
print("="*70)

config_example = """
import json
from pathlib import Path

DEFAULT_CONFIG = {
    "app": "MyApp",
    "version": "1.0",
    "debug": False
}

def load_config(config_file=None):
    '''Load config with defaults'''
    if not config_file:
        return DEFAULT_CONFIG.copy()
    
    try:
        with open(config_file, 'r') as f:
            user_config = json.load(f)
        
        # Merge with defaults
        return {**DEFAULT_CONFIG, **user_config}
    
    except FileNotFoundError:
        print(f"Config file not found: {config_file}")
        return DEFAULT_CONFIG.copy()
    except json.JSONDecodeError:
        print(f"Invalid JSON in: {config_file}")
        return DEFAULT_CONFIG.copy()

# Usage
config = load_config('myconfig.json')
"""
print(config_example)

# 5. LOGGING
print("\n" + "="*70)
print("5. LOGGING")
print("="*70)

logging_example = """
import logging

def setup_logging(level=logging.INFO):
    '''Configure logging'''
    logging.basicConfig(
        level=level,
        format='[%(asctime)s] [%(levelname)s] %(message)s',
        handlers=[
            logging.FileHandler('app.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()

# Usage
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
"""
print(logging_example)

# 6. ERROR HANDLING
print("\n" + "="*70)
print("6. ERROR HANDLING")
print("="*70)

error_example = """
import logging

logger = logging.getLogger(__name__)

def safe_operation():
    '''Operation with error handling'''
    try:
        # Risky operation
        with open('file.txt', 'r') as f:
            data = f.read()
        
        # Process data
        result = process(data)
        
        logger.info("Operation successful")
        return result
        
    except FileNotFoundError:
        logger.error("File not found")
        return None
    except PermissionError:
        logger.error("Permission denied")
        return None
    except Exception as e:
        logger.critical(f"Unexpected error: {e}")
        return None
"""
print(error_example)

# 7. EXIT CODES
print("\n" + "="*70)
print("7. EXIT CODES")
print("="*70)

exit_codes_example = """
import sys

# Define exit codes
EXIT_SUCCESS = 0
EXIT_ERROR = 1
EXIT_INVALID_ARGS = 2
EXIT_FILE_ERROR = 3

def main():
    '''Main function'''
    try:
        # Do work
        if everything_ok:
            return EXIT_SUCCESS
        else:
            return EXIT_ERROR
    
    except FileNotFoundError:
        return EXIT_FILE_ERROR
    except Exception:
        return EXIT_ERROR

if __name__ == '__main__':
    sys.exit(main())
"""
print(exit_codes_example)

# 8. COMPLETE TEMPLATE
print("\n" + "="*70)
print("8. COMPLETE TEMPLATE")
print("="*70)

complete_template = """
#!/usr/bin/env python3
'''Production-ready CLI tool template'''

import sys
import json
import logging
import argparse
from pathlib import Path

# Constants
EXIT_SUCCESS = 0
EXIT_ERROR = 1
DEFAULT_CONFIG = {"app": "MyApp", "version": "1.0"}

# Setup logging
def setup_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format='[%(asctime)s] [%(levelname)s] %(message)s',
        handlers=[
            logging.FileHandler('app.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()

# Configuration
def load_config(config_file=None):
    if not config_file:
        return DEFAULT_CONFIG
    try:
        with open(config_file) as f:
            return {**DEFAULT_CONFIG, **json.load(f)}
    except Exception as e:
        logger.error(f"Config load failed: {e}")
        return DEFAULT_CONFIG

# Argument parsing
def parse_args():
    parser = argparse.ArgumentParser(description='My Tool')
    parser.add_argument('--config', help='Config file')
    parser.add_argument('--verbose', action='store_true')
    subparsers = parser.add_subparsers(dest='command')
    subparsers.add_parser('status', help='Show status')
    return parser.parse_args()

# Command handlers
def cmd_status(config):
    logger.info("Status command")
    print(f"App: {config['app']}")
    print(f"Version: {config['version']}")
    return EXIT_SUCCESS

# Main
def main():
    args = parse_args()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    config = load_config(args.config)
    
    if not args.command:
        print("No command specified")
        return EXIT_ERROR
    
    try:
        if args.command == 'status':
            return cmd_status(config)
    except Exception as e:
        logger.error(f"Error: {e}")
        return EXIT_ERROR
    
    return EXIT_SUCCESS

if __name__ == '__main__':
    sys.exit(main())
"""
print(complete_template)

# BEST PRACTICES
print("\n" + "="*70)
print("BEST PRACTICES")
print("="*70)

best_practices = """
1. Use argparse for argument parsing
2. Use logging module (not print)
3. Load configuration from files
4. Handle all errors gracefully
5. Return proper exit codes
6. Provide --help and --version
7. Use subcommands for different operations
8. Validate all inputs
9. Log all important operations
10. Make it testable
11. Follow PEP 8
12. Document everything
13. Use constants, not magic numbers
14. Provide examples
15. Make it installable with pip

Remember:
  ✓ User experience matters
  ✓ Good error messages save time
  ✓ Logging helps debugging
  ✓ Exit codes enable automation
  ✓ Configuration makes it flexible
"""
print(best_practices)
