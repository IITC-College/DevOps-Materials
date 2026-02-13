#!/usr/bin/env python3
# Step 9: Complete CLI tool with all features integrated

"""
DevOps Helper CLI Tool v3.5
Complete implementation with all features:
- Command-line arguments (argparse)
- Configuration files (JSON)
- Logging (file + console)
- Error handling (try/except)
- Exit codes
- Help system
- Multiple commands
"""

import sys
import json
import logging
import argparse
from pathlib import Path
import datetime

# Exit codes
EXIT_SUCCESS = 0
EXIT_ERROR = 1
EXIT_INVALID_ARGS = 2
EXIT_FILE_ERROR = 3
EXIT_PERMISSION_ERROR = 4

# Default configuration
DEFAULT_CONFIG = {
    "app_name": "DevOps Helper",
    "version": 3.5,
    "status": "active",
    "ready": True,
    "max_retries": 3,
    "backup_dir": "./backups",
    "log_level": "INFO"
}

def setup_logging(level=logging.INFO, log_file='devops_helper.log'):
    """Configure logging with file and console handlers"""
    logging.basicConfig(
        level=level,
        format='[%(asctime)s] [%(levelname)-8s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def load_config(config_file=None):
    """Load configuration from JSON file"""
    if not config_file:
        logger.info("Using default configuration")
        return DEFAULT_CONFIG.copy()
    
    try:
        config_path = Path(config_file)
        if not config_path.exists():
            logger.error(f"Config file not found: {config_file}")
            sys.exit(EXIT_FILE_ERROR)
        
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        # Merge with defaults
        merged_config = {**DEFAULT_CONFIG, **config}
        logger.info(f"Configuration loaded from {config_file}")
        return merged_config
        
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in config file: {e}")
        sys.exit(EXIT_ERROR)
    except PermissionError:
        logger.error(f"Permission denied reading config file: {config_file}")
        sys.exit(EXIT_PERMISSION_ERROR)
    except Exception as e:
        logger.error(f"Unexpected error loading config: {e}")
        sys.exit(EXIT_ERROR)

def parse_arguments():
    """Parse command-line arguments using argparse"""
    parser = argparse.ArgumentParser(
        prog='devops-helper',
        description='DevOps Helper - Production-ready CLI tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s status
  %(prog)s backup --full
  %(prog)s deploy staging
  %(prog)s --config custom.json status
  %(prog)s --verbose backup
        """
    )
    
    # Global options
    parser.add_argument('--version', action='version',
                       version=f'%(prog)s {DEFAULT_CONFIG["version"]}')
    parser.add_argument('--config', '-c', metavar='FILE',
                       help='Configuration file path')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose output (DEBUG level)')
    parser.add_argument('--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                       default='INFO', help='Set logging level')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would happen without executing')
    
    # Subcommands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Status command
    status_parser = subparsers.add_parser('status', help='Show system status')
    status_parser.add_argument('--detailed', action='store_true',
                              help='Show detailed status')
    
    # Backup command
    backup_parser = subparsers.add_parser('backup', help='Perform backup operation')
    backup_parser.add_argument('--full', action='store_true',
                              help='Perform full backup (default: incremental)')
    backup_parser.add_argument('--path', metavar='DIR',
                              help='Backup destination directory')
    
    # Deploy command
    deploy_parser = subparsers.add_parser('deploy', help='Deploy application')
    deploy_parser.add_argument('environment',
                              choices=['dev', 'staging', 'production'],
                              help='Target environment')
    deploy_parser.add_argument('--force', action='store_true',
                              help='Force deployment without confirmation')
    
    # Config command
    config_parser = subparsers.add_parser('config', help='Show configuration')
    config_parser.add_argument('--export', metavar='FILE',
                              help='Export config to file')
    
    return parser.parse_args()

def save_backup_report(backup_info, report_file='backup_report.txt'):
    """Save backup report to file"""
    try:
        with open(report_file, 'w') as f:
            f.write("=" * 60 + "\n")
            f.write("BACKUP REPORT\n")
            f.write("=" * 60 + "\n")
            f.write(f"Timestamp: {datetime.datetime.now().isoformat()}\n")
            for key, value in backup_info.items():
                f.write(f"{key}: {value}\n")
            f.write("=" * 60 + "\n")
        logger.info(f"Backup report saved: {report_file}")
        return True
    except Exception as e:
        logger.error(f"Failed to save backup report: {e}")
        return False

def cmd_status(config, args):
    """Handle status command"""
    logger.info("Executing status command")
    
    print(f"\n{config['app_name']} v{config['version']}")
    print("=" * 50)
    print(f"Status: {config['status']}")
    print(f"Ready: {config['ready']}")
    
    if args.detailed:
        print(f"\nDetailed Information:")
        print(f"  Max Retries: {config['max_retries']}")
        print(f"  Backup Dir: {config['backup_dir']}")
        print(f"  Log Level: {config['log_level']}")
    
    logger.info("Status command completed")
    return EXIT_SUCCESS

def cmd_backup(config, args):
    """Handle backup command"""
    backup_type = "full" if args.full else "incremental"
    backup_path = args.path or config['backup_dir']
    
    logger.info(f"Starting {backup_type} backup to {backup_path}")
    
    if args.dry_run:
        print(f"\n[DRY RUN] Would perform {backup_type} backup")
        print(f"[DRY RUN] Destination: {backup_path}")
        return EXIT_SUCCESS
    
    print(f"\nPerforming {backup_type} backup...")
    print(f"Destination: {backup_path}")
    
    # Simulate backup operation
    backup_info = {
        "type": backup_type,
        "destination": backup_path,
        "status": "success",
        "files_count": 127,
        "total_size": "45.2 MB",
        "duration": "2.5 seconds"
    }
    
    if save_backup_report(backup_info):
        print("✓ Backup completed successfully")
        print(f"  Files: {backup_info['files_count']}")
        print(f"  Size: {backup_info['total_size']}")
        logger.info("Backup completed successfully")
        return EXIT_SUCCESS
    else:
        print("✗ Backup completed but report save failed")
        logger.warning("Backup completed but report save failed")
        return EXIT_ERROR

def cmd_deploy(config, args):
    """Handle deploy command"""
    environment = args.environment
    
    logger.info(f"Deploying to {environment}")
    
    if environment == 'production' and not args.force:
        response = input(f"Deploy to PRODUCTION? This is irreversible. (yes/no): ")
        if response.lower() != 'yes':
            print("Deployment cancelled")
            logger.info("Production deployment cancelled by user")
            return EXIT_SUCCESS
    
    if args.dry_run:
        print(f"\n[DRY RUN] Would deploy to {environment}")
        return EXIT_SUCCESS
    
    print(f"\nDeploying to {environment}...")
    # Simulate deployment
    print(f"✓ Successfully deployed to {environment}")
    
    logger.info(f"Deployment to {environment} completed")
    return EXIT_SUCCESS

def cmd_config(config, args):
    """Handle config command"""
    logger.info("Displaying configuration")
    
    print("\nCurrent Configuration:")
    print("=" * 50)
    for key, value in config.items():
        print(f"  {key}: {value}")
    
    if args.export:
        try:
            with open(args.export, 'w') as f:
                json.dump(config, f, indent=2)
            print(f"\n✓ Configuration exported to {args.export}")
            logger.info(f"Config exported to {args.export}")
        except Exception as e:
            print(f"\n✗ Failed to export config: {e}")
            logger.error(f"Config export failed: {e}")
            return EXIT_ERROR
    
    return EXIT_SUCCESS

def main():
    """Main entry point"""
    # Parse arguments first
    args = parse_arguments()
    
    # Determine log level
    if args.verbose:
        log_level = logging.DEBUG
    else:
        log_level = getattr(logging, args.log_level)
    
    # Setup logging
    global logger
    logger = setup_logging(log_level)
    
    logger.info(f"{DEFAULT_CONFIG['app_name']} v{DEFAULT_CONFIG['version']} started")
    logger.debug(f"Arguments: {args}")
    
    # Load configuration
    config = load_config(args.config)
    
    # Check if dry-run
    if hasattr(args, 'dry_run') and args.dry_run:
        logger.info("DRY RUN MODE enabled")
    
    # Handle no command
    if not args.command:
        print("Error: No command specified")
        print("Use --help for usage information")
        logger.warning("No command specified")
        return EXIT_INVALID_ARGS
    
    # Route to command handlers
    try:
        if args.command == 'status':
            return cmd_status(config, args)
        elif args.command == 'backup':
            return cmd_backup(config, args)
        elif args.command == 'deploy':
            return cmd_deploy(config, args)
        elif args.command == 'config':
            return cmd_config(config, args)
        else:
            logger.error(f"Unknown command: {args.command}")
            return EXIT_ERROR
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user")
        logger.warning("Operation cancelled by user (Ctrl+C)")
        return EXIT_ERROR
    except Exception as e:
        logger.critical(f"Unexpected error: {e}", exc_info=True)
        print(f"\n✗ Critical error: {e}")
        return EXIT_ERROR

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
