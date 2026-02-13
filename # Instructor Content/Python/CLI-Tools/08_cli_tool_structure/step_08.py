#!/usr/bin/env python3
# Step 8: Professional CLI tool structure

"""
DevOps Helper CLI Tool v3.0
A production-ready command-line tool demonstrating best practices
"""

import sys
import json
import logging
import argparse
from pathlib import Path

# Exit codes
EXIT_SUCCESS = 0
EXIT_ERROR = 1
EXIT_INVALID_ARGS = 2
EXIT_FILE_ERROR = 3

# Configure logging
def setup_logging(log_level=logging.INFO):
    """Configure logging with file and console handlers"""
    logging.basicConfig(
        level=log_level,
        format='[%(asctime)s] [%(levelname)-8s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler('devops_helper.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

# Configuration
DEFAULT_CONFIG = {
    "app_name": "DevOps Helper",
    "version": 3.0,
    "status": "active",
    "ready": True
}

def load_config(config_file=None):
    """Load configuration from file or use defaults"""
    if not config_file:
        logger.info("Using default configuration")
        return DEFAULT_CONFIG.copy()
    
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
            logger.info(f"Loaded config from {config_file}")
            return {**DEFAULT_CONFIG, **config}
    except FileNotFoundError:
        logger.error(f"Config file not found: {config_file}")
        sys.exit(EXIT_FILE_ERROR)
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in {config_file}")
        sys.exit(EXIT_ERROR)

def parse_arguments():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(
        description='DevOps Helper - A production-ready CLI tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s status
  %(prog)s backup --verbose
  %(prog)s --config custom.json deploy
  %(prog)s --version
        """
    )
    
    parser.add_argument('--version', action='version', 
                       version=f'%(prog)s {DEFAULT_CONFIG["version"]}')
    parser.add_argument('--config', help='Configuration file path')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose output')
    parser.add_argument('--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                       default='INFO', help='Set logging level')
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # status command
    subparsers.add_parser('status', help='Show system status')
    
    # backup command
    backup_parser = subparsers.add_parser('backup', help='Perform backup')
    backup_parser.add_argument('--full', action='store_true', help='Full backup')
    
    # deploy command
    deploy_parser = subparsers.add_parser('deploy', help='Deploy application')
    deploy_parser.add_argument('environment', choices=['dev', 'staging', 'prod'],
                              help='Target environment')
    
    return parser.parse_args()

def run_status(config):
    """Execute status command"""
    logger.info("Status command executed")
    print(f"\n{config['app_name']} v{config['version']}")
    print(f"Status: {config['status']}")
    print(f"Ready: {config['ready']}")
    return EXIT_SUCCESS

def run_backup(config, full=False):
    """Execute backup command"""
    backup_type = "full" if full else "incremental"
    logger.info(f"Starting {backup_type} backup")
    
    print(f"\nPerforming {backup_type} backup...")
    # Backup logic here
    print("✓ Backup completed successfully")
    
    logger.info("Backup completed")
    return EXIT_SUCCESS

def run_deploy(config, environment):
    """Execute deploy command"""
    logger.info(f"Deploying to {environment}")
    
    print(f"\nDeploying to {environment}...")
    # Deploy logic here
    print(f"✓ Deployed to {environment}")
    
    logger.info(f"Deploy to {environment} completed")
    return EXIT_SUCCESS

def main():
    """Main entry point"""
    # Parse arguments
    args = parse_arguments()
    
    # Setup logging
    log_level = getattr(logging, args.log_level)
    global logger
    logger = setup_logging(log_level)
    
    logger.info(f"{DEFAULT_CONFIG['app_name']} v{DEFAULT_CONFIG['version']} started")
    
    # Load configuration
    config = load_config(args.config)
    
    # Handle no command
    if not args.command:
        print("Error: No command specified")
        print("Use --help for usage information")
        return EXIT_INVALID_ARGS
    
    # Route to command handlers
    try:
        if args.command == 'status':
            return run_status(config)
        elif args.command == 'backup':
            return run_backup(config, args.full)
        elif args.command == 'deploy':
            return run_deploy(config, args.environment)
        else:
            logger.error(f"Unknown command: {args.command}")
            return EXIT_ERROR
    except Exception as e:
        logger.critical(f"Unexpected error: {e}", exc_info=True)
        return EXIT_ERROR

if __name__ == '__main__':
    sys.exit(main())
