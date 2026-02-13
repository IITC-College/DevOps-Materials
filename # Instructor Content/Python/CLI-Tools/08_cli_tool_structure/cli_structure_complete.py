#!/usr/bin/env python3
# Complete CLI tool structure guide

"""
PROFESSIONAL CLI TOOL STRUCTURE

This file demonstrates the complete structure of a professional CLI tool,
covering all aspects: argument parsing, logging, config, error handling,
exit codes, help system, and command routing.
"""

import sys
import json
import logging
import argparse
from pathlib import Path

print("PROFESSIONAL CLI TOOL STRUCTURE")
print("="*70)

# SECTION 1: CONSTANTS AND CONFIGURATION
print("\n[1] CONSTANTS & EXIT CODES")
print("-"*70)

EXIT_SUCCESS = 0
EXIT_ERROR = 1
EXIT_INVALID_ARGS = 2
EXIT_FILE_ERROR = 3

DEFAULT_CONFIG = {
    "app_name": "MyApp",
    "version": "1.0",
    "debug": False
}

print(f"Exit codes defined: SUCCESS={EXIT_SUCCESS}, ERROR={EXIT_ERROR}")
print(f"Default config: {DEFAULT_CONFIG}")

# SECTION 2: LOGGING SETUP
print("\n[2] LOGGING SETUP")
print("-"*70)

def setup_logging(level=logging.INFO):
    """Setup logging configuration"""
    logging.basicConfig(
        level=level,
        format='[%(asctime)s] [%(levelname)-8s] %(message)s',
        handlers=[
            logging.FileHandler('app.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()
logger.info("Logging configured")

# SECTION 3: ARGUMENT PARSING
print("\n[3] ARGUMENT PARSING")
print("-"*70)

def create_parser():
    """Create argument parser"""
    parser = argparse.ArgumentParser(
        description='My CLI Tool',
        epilog='Examples:\n  %(prog)s status\n  %(prog)s deploy prod'
    )
    
    # Global options
    parser.add_argument('--version', action='version', version='1.0')
    parser.add_argument('--config', help='Config file')
    parser.add_argument('--verbose', '-v', action='store_true')
    
    # Subcommands
    subparsers = parser.add_subparsers(dest='command')
    
    subparsers.add_parser('status', help='Show status')
    
    deploy = subparsers.add_parser('deploy', help='Deploy app')
    deploy.add_argument('env', choices=['dev', 'prod'])
    
    return parser

parser = create_parser()
print("✓ Argument parser created with subcommands")

# SECTION 4: CONFIGURATION LOADING
print("\n[4] CONFIGURATION LOADING")
print("-"*70)

def load_config(config_file=None):
    """Load configuration"""
    if not config_file:
        return DEFAULT_CONFIG.copy()
    
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
        logger.info(f"Loaded config from {config_file}")
        return {**DEFAULT_CONFIG, **config}
    except FileNotFoundError:
        logger.error(f"Config not found: {config_file}")
        sys.exit(EXIT_FILE_ERROR)
    except json.JSONDecodeError:
        logger.error("Invalid JSON")
        sys.exit(EXIT_ERROR)

print("✓ Config loading function defined")

# SECTION 5: COMMAND HANDLERS
print("\n[5] COMMAND HANDLERS")
print("-"*70)

def cmd_status(config):
    """Handle status command"""
    logger.info("Status command")
    print(f"App: {config['app_name']}")
    print(f"Version: {config['version']}")
    return EXIT_SUCCESS

def cmd_deploy(config, environment):
    """Handle deploy command"""
    logger.info(f"Deploying to {environment}")
    print(f"Deploying to {environment}...")
    return EXIT_SUCCESS

print("✓ Command handlers defined")

# SECTION 6: MAIN FUNCTION
print("\n[6] MAIN FUNCTION PATTERN")
print("-"*70)

def main():
    """Main entry point"""
    # Parse arguments
    args = parser.parse_args()
    
    # Setup logging
    if hasattr(args, 'verbose') and args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # Load config
    config = load_config(getattr(args, 'config', None))
    
    # Route commands
    if not args.command:
        parser.print_help()
        return EXIT_INVALID_ARGS
    
    try:
        if args.command == 'status':
            return cmd_status(config)
        elif args.command == 'deploy':
            return cmd_deploy(config, args.env)
    except Exception as e:
        logger.error(f"Error: {e}")
        return EXIT_ERROR
    
    return EXIT_SUCCESS

print("✓ Main function defined")

# SECTION 7: ENTRY POINT
print("\n[7] ENTRY POINT")
print("-"*70)

entry_point_code = """
if __name__ == '__main__':
    sys.exit(main())
"""
print(entry_point_code)

# COMPLETE STRUCTURE TEMPLATE
print("\n"+"="*70)
print("COMPLETE STRUCTURE TEMPLATE")
print("="*70)

complete_template = """
#!/usr/bin/env python3
'''My CLI Tool'''

import sys
import json
import logging
import argparse

# Constants
EXIT_SUCCESS = 0
EXIT_ERROR = 1
DEFAULT_CONFIG = {"app": "MyApp"}

# Setup logging
def setup_logging(level=logging.INFO):
    logging.basicConfig(level=level, format='[%(levelname)s] %(message)s')
    return logging.getLogger(__name__)

logger = setup_logging()

# Configuration
def load_config(config_file=None):
    if not config_file:
        return DEFAULT_CONFIG
    with open(config_file, 'r') as f:
        return json.load(f)

# Argument parsing
def parse_args():
    parser = argparse.ArgumentParser(description='My Tool')
    parser.add_argument('--config', help='Config file')
    parser.add_argument('--verbose', '-v', action='store_true')
    
    subparsers = parser.add_subparsers(dest='command')
    subparsers.add_parser('status', help='Show status')
    
    return parser.parse_args()

# Command handlers
def cmd_status(config):
    logger.info("Status command")
    print(f"Status: OK")
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
    
    if args.command == 'status':
        return cmd_status(config)
    
    return EXIT_SUCCESS

# Entry point
if __name__ == '__main__':
    sys.exit(main())
"""

print(complete_template)

print("\n"+"="*70)
print("KEY COMPONENTS")
print("="*70)
print("""
1. Constants & exit codes
2. Logging setup function
3. Configuration loading
4. Argument parsing with argparse
5. Command handler functions
6. Main coordination function
7. if __name__ == '__main__' entry point

BENEFITS:
  ✓ Professional structure
  ✓ Easy to test
  ✓ Easy to extend
  ✓ Clear separation of concerns
  ✓ Proper error handling
  ✓ Production-ready
""")
