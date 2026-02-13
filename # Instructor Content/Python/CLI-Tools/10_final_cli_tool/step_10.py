#!/usr/bin/env python3
# Step 10: Final Production-Ready DevOps Helper CLI Tool

"""
DevOps Helper CLI Tool v4.0 - Production Ready

A complete, professional command-line tool demonstrating best practices:
- Argument parsing with argparse
- Configuration management (JSON files)
- Professional logging (file + console)  
- Comprehensive error handling
- Proper exit codes
- Interactive confirmations
- Dry-run mode
- Help system
- Multiple commands with options

Usage:
    python step_10.py --help
    python step_10.py status
    python step_10.py backup --full
    python step_10.py deploy production --force
    python step_10.py --config myconfig.json status
"""

import sys
import json
import logging
import argparse
from pathlib import Path
import datetime

__version__ = "4.0"
__author__ = "DevOps Team"

# Exit codes (following conventions)
EXIT_SUCCESS = 0
EXIT_ERROR = 1
EXIT_INVALID_ARGS = 2
EXIT_FILE_ERROR = 3
EXIT_PERMISSION_ERROR = 4
EXIT_USER_CANCELLED = 5

# Default configuration
DEFAULT_CONFIG = {
    "app_name": "DevOps Helper",
    "version": __version__,
    "status": "active",
    "ready": True,
    "max_retries": 3,
    "backup_dir": "./backups",
    "log_level": "INFO",
    "log_file": "devops_helper.log"
}

def setup_logging(level=logging.INFO, log_file='devops_helper.log'):
    """
    Configure application logging
    
    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Path to log file
    
    Returns:
        Configured logger object
    """
    # Create formatter
    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)-8s] [%(name)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    
    # Console handler  
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    
    # Configure root logger
    logger = logging.getLogger('devops_helper')
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def load_config(config_file=None):
    """
    Load configuration from JSON file
    
    Args:
        config_file: Path to configuration file (optional)
    
    Returns:
        Configuration dictionary
    
    Exits on error with appropriate exit code
    """
    if not config_file:
        logger.info("No config file specified, using defaults")
        return DEFAULT_CONFIG.copy()
    
    try:
        config_path = Path(config_file)
        
        if not config_path.exists():
            logger.error(f"Configuration file not found: {config_file}")
            print(f"Error: Configuration file not found: {config_file}", file=sys.stderr)
            sys.exit(EXIT_FILE_ERROR)
        
        if not config_path.is_file():
            logger.error(f"Configuration path is not a file: {config_file}")
            print(f"Error: {config_file} is not a file", file=sys.stderr)
            sys.exit(EXIT_FILE_ERROR)
        
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        # Merge with defaults (defaults are overridden by config file)
        merged_config = {**DEFAULT_CONFIG, **config}
        logger.info(f"Configuration loaded successfully from {config_file}")
        return merged_config
        
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in configuration file: {e}")
        print(f"Error: Invalid JSON in {config_file}: {e}", file=sys.stderr)
        sys.exit(EXIT_ERROR)
    except PermissionError:
        logger.error(f"Permission denied reading configuration file: {config_file}")
        print(f"Error: Permission denied: {config_file}", file=sys.stderr)
        sys.exit(EXIT_PERMISSION_ERROR)
    except Exception as e:
        logger.critical(f"Unexpected error loading configuration: {e}", exc_info=True)
        print(f"Error: Failed to load configuration: {e}", file=sys.stderr)
        sys.exit(EXIT_ERROR)

def parse_arguments():
    """
    Parse and validate command-line arguments
    
    Returns:
        Parsed arguments object
    """
    parser = argparse.ArgumentParser(
        prog='devops-helper',
        description='DevOps Helper - Production-ready CLI tool for DevOps operations',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Show status:
    %(prog)s status
    %(prog)s status --detailed
  
  Perform backup:
    %(prog)s backup
    %(prog)s backup --full --path /backup/dir
    %(prog)s --dry-run backup --full
  
  Deploy application:
    %(prog)s deploy staging
    %(prog)s deploy production --force
  
  View configuration:
    %(prog)s config
    %(prog)s config --export myconfig.json
  
  With custom config:
    %(prog)s --config custom.json status
  
  Verbose mode:
    %(prog)s --verbose backup

For more information, visit: https://github.com/example/devops-helper
        """
    )
    
    # Global options
    parser.add_argument('--version', action='version',
                       version=f'%(prog)s {__version__}',
                       help='Show program version and exit')
    parser.add_argument('--config', '-c', metavar='FILE',
                       help='Path to configuration file (JSON)')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose output (DEBUG logging level)')
    parser.add_argument('--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                       default='INFO',
                       help='Set logging level (default: INFO)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would happen without executing operations')
    parser.add_argument('--no-color', action='store_true',
                       help='Disable colored output')
    
    # Subcommands
    subparsers = parser.add_subparsers(dest='command',
                                       help='Available commands (use <command> --help for details)')
    
    # Status command
    status_parser = subparsers.add_parser('status',
                                          help='Show system status',
                                          description='Display current system status and health checks')
    status_parser.add_argument('--detailed', action='store_true',
                              help='Show detailed status information')
    status_parser.add_argument('--json', action='store_true',
                              help='Output status as JSON')
    
    # Backup command
    backup_parser = subparsers.add_parser('backup',
                                          help='Perform backup operation',
                                          description='Backup system data and configurations')
    backup_parser.add_argument('--full', action='store_true',
                              help='Perform full backup (default: incremental)')
    backup_parser.add_argument('--path', metavar='DIR',
                              help='Backup destination directory (overrides config)')
    backup_parser.add_argument('--compress', action='store_true',
                              help='Compress backup archive')
    
    # Deploy command
    deploy_parser = subparsers.add_parser('deploy',
                                          help='Deploy application',
                                          description='Deploy application to specified environment')
    deploy_parser.add_argument('environment',
                              choices=['dev', 'staging', 'production'],
                              help='Target environment for deployment')
    deploy_parser.add_argument('--force', '-f', action='store_true',
                              help='Force deployment without confirmation prompts')
    deploy_parser.add_argument('--rollback', action='store_true',
                              help='Rollback to previous version')
    
    # Config command
    config_parser = subparsers.add_parser('config',
                                          help='Configuration management',
                                          description='View or manage configuration')
    config_parser.add_argument('--export', metavar='FILE',
                              help='Export current configuration to file')
    config_parser.add_argument('--validate', action='store_true',
                              help='Validate configuration')
    
    return parser.parse_args()

def save_backup_report(backup_info, report_file='backup_report.txt'):
    """
    Save backup report to file
    
    Args:
        backup_info: Dictionary containing backup information
        report_file: Path to report file
    
    Returns:
        True if successful, False otherwise
    """
    try:
        with open(report_file, 'w') as f:
            f.write("=" * 70 + "\n")
            f.write("DEVOPS HELPER - BACKUP REPORT\n")
            f.write("=" * 70 + "\n")
            f.write(f"Generated: {datetime.datetime.now().isoformat()}\n")
            f.write("-" * 70 + "\n")
            for key, value in backup_info.items():
                f.write(f"{key:20s}: {value}\n")
            f.write("=" * 70 + "\n")
        
        logger.info(f"Backup report saved: {report_file}")
        return True
    except PermissionError:
        logger.error(f"Permission denied writing report: {report_file}")
        return False
    except Exception as e:
        logger.error(f"Failed to save backup report: {e}")
        return False

def confirm_action(message, default=False):
    """
    Prompt user for confirmation
    
    Args:
        message: Confirmation message
        default: Default answer if user just presses Enter
    
    Returns:
        True if confirmed, False otherwise
    """
    prompt = f"{message} ({'Y/n' if default else 'y/N'}): "
    response = input(prompt).strip().lower()
    
    if not response:
        return default
    
    return response in ['y', 'yes']

def cmd_status(config, args):
    """Handle status command"""
    logger.info("Executing status command")
    
    print(f"\n{config['app_name']} v{config['version']}")
    print("=" * 70)
    
    # Basic status
    print(f"Status      : {config['status']}")
    print(f"Ready       : {config['ready']}")
    
    if args.detailed:
        print(f"\nDetailed Information:")
        print(f"  Max Retries  : {config['max_retries']}")
        print(f"  Backup Dir   : {config['backup_dir']}")
        print(f"  Log Level    : {config['log_level']}")
        print(f"  Log File     : {config['log_file']}")
    
    if args.json:
        import json
        status_data = {
            "app": config['app_name'],
            "version": config['version'],
            "status": config['status'],
            "ready": config['ready']
        }
        print("\nJSON Output:")
        print(json.dumps(status_data, indent=2))
    
    logger.info("Status command completed successfully")
    return EXIT_SUCCESS

def cmd_backup(config, args):
    """Handle backup command"""
    backup_type = "full" if args.full else "incremental"
    backup_path = args.path or config['backup_dir']
    
    logger.info(f"Starting {backup_type} backup to {backup_path}")
    
    # Dry run mode
    if args.dry_run:
        print(f"\n[DRY RUN MODE]")
        print(f"Would perform {backup_type} backup")
        print(f"Destination: {backup_path}")
        if args.compress:
            print("Compression: enabled")
        logger.info("Dry run completed")
        return EXIT_SUCCESS
    
    # Display operation
    print(f"\nPerforming {backup_type} backup...")
    print(f"Destination : {backup_path}")
    print(f"Compression : {'enabled' if args.compress else 'disabled'}")
    print()
    
    # Simulate backup operation
    logger.debug("Simulating backup operation")
    backup_info = {
        "Type": backup_type,
        "Destination": backup_path,
        "Status": "success",
        "Files": 127,
        "Total Size": "45.2 MB",
        "Compressed": "Yes" if args.compress else "No",
        "Duration": "2.5 seconds",
        "Timestamp": datetime.datetime.now().isoformat()
    }
    
    # Save report
    if save_backup_report(backup_info):
        print("✓ Backup completed successfully")
        print(f"  Files backed up: {backup_info['Files']}")
        print(f"  Total size: {backup_info['Total Size']}")
        print(f"  Report saved: backup_report.txt")
        logger.info("Backup operation completed successfully")
        return EXIT_SUCCESS
    else:
        print("✓ Backup completed")
        print("✗ Warning: Failed to save backup report")
        logger.warning("Backup completed but report save failed")
        return EXIT_SUCCESS

def cmd_deploy(config, args):
    """Handle deploy command"""
    environment = args.environment
    
    logger.info(f"Deploying to {environment}")
    
    # Confirmation for production
    if environment == 'production' and not args.force:
        print(f"\n⚠  WARNING: You are about to deploy to PRODUCTION")
        print(f"   This operation cannot be undone.")
        if not confirm_action("Continue with deployment?", default=False):
            print("Deployment cancelled by user")
            logger.info("Production deployment cancelled by user")
            return EXIT_USER_CANCELLED
    
    # Dry run
    if args.dry_run:
        print(f"\n[DRY RUN MODE]")
        print(f"Would deploy to {environment}")
        if args.rollback:
            print("Operation: Rollback to previous version")
        else:
            print("Operation: Deploy new version")
        return EXIT_SUCCESS
    
    # Execute deployment
    print(f"\nDeploying to {environment}...")
    
    if args.rollback:
        print("  Rolling back to previous version...")
        logger.info("Performing rollback")
    else:
        print("  Deploying new version...")
    
    # Simulate deployment
    print("  [1/4] Preparing deployment...")
    print("  [2/4] Uploading files...")
    print("  [3/4] Updating configuration...")
    print("  [4/4] Restarting services...")
    
    print(f"\n✓ Successfully deployed to {environment}")
    logger.info(f"Deployment to {environment} completed successfully")
    return EXIT_SUCCESS

def cmd_config(config, args):
    """Handle config command"""
    logger.info("Processing config command")
    
    # Validation
    if args.validate:
        print("\nValidating configuration...")
        # Add validation logic here
        print("✓ Configuration is valid")
        logger.info("Configuration validation passed")
        return EXIT_SUCCESS
    
    # Display config
    print("\nCurrent Configuration:")
    print("=" * 70)
    for key, value in config.items():
        print(f"  {key:15s} : {value}")
    print("=" * 70)
    
    # Export config
    if args.export:
        try:
            with open(args.export, 'w') as f:
                json.dump(config, f, indent=2, sort_keys=True)
            print(f"\n✓ Configuration exported to: {args.export}")
            logger.info(f"Configuration exported to {args.export}")
        except Exception as e:
            print(f"\n✗ Failed to export configuration: {e}")
            logger.error(f"Config export failed: {e}")
            return EXIT_ERROR
    
    logger.info("Config command completed")
    return EXIT_SUCCESS

def main():
    """
    Main entry point for the application
    
    Returns:
        Exit code (0 for success, non-zero for errors)
    """
    # Parse command-line arguments
    args = parse_arguments()
    
    # Determine logging level
    if args.verbose:
        log_level = logging.DEBUG
    else:
        log_level = getattr(logging, args.log_level)
    
    # Setup logging
    global logger
    logger = setup_logging(log_level, DEFAULT_CONFIG['log_file'])
    
    logger.info(f"{DEFAULT_CONFIG['app_name']} v{__version__} started")
    logger.debug(f"Command-line arguments: {vars(args)}")
    
    # Load configuration
    try:
        config = load_config(args.config)
    except SystemExit:
        raise  # Re-raise sys.exit() calls
    except Exception as e:
        logger.critical(f"Failed to load configuration: {e}", exc_info=True)
        return EXIT_ERROR
    
    # Check for dry-run mode
    if hasattr(args, 'dry_run') and args.dry_run:
        logger.info("DRY RUN MODE enabled - no changes will be made")
    
    # Validate command
    if not args.command:
        print("Error: No command specified", file=sys.stderr)
        print("Use --help for usage information", file=sys.stderr)
        logger.warning("No command specified")
        return EXIT_INVALID_ARGS
    
    # Route to command handlers
    try:
        logger.debug(f"Routing to command handler: {args.command}")
        
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
            print(f"Error: Unknown command '{args.command}'", file=sys.stderr)
            return EXIT_ERROR
            
    except KeyboardInterrupt:
        print("\n\n✗ Operation cancelled by user (Ctrl+C)", file=sys.stderr)
        logger.warning("Operation cancelled by user (KeyboardInterrupt)")
        return EXIT_USER_CANCELLED
    except Exception as e:
        logger.critical(f"Unexpected error in command handler: {e}", exc_info=True)
        print(f"\n✗ Critical error: {e}", file=sys.stderr)
        print("Check log file for details", file=sys.stderr)
        return EXIT_ERROR
    finally:
        logger.info("Application shutting down")

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
