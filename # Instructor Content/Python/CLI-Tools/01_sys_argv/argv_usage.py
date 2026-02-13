#!/usr/bin/env python3
# Showing usage information

import sys

"""
USAGE MESSAGES:

Good usage message includes:
1. How to run the program
2. Required arguments
3. Optional arguments
4. Examples
"""

def show_usage():
    """Display usage information"""
    script_name = sys.argv[0]
    
    print(f"Usage: python {script_name} <command> [options] [arguments]")
    print()
    print("Commands:")
    print("  deploy <env>     Deploy to environment (dev/staging/prod)")
    print("  backup           Backup data")
    print("  status           Show system status")
    print("  help             Show this help message")
    print()
    print("Options:")
    print("  -v, --verbose    Show detailed output")
    print("  -f, --force      Force operation without confirmation")
    print("  -q, --quiet      Suppress non-error output")
    print()
    print("Examples:")
    print(f"  python {script_name} status")
    print(f"  python {script_name} deploy staging")
    print(f"  python {script_name} -v deploy production")
    print(f"  python {script_name} --force backup")
    print()

# Check if help requested or no args
if len(sys.argv) == 1:
    print("Error: No command provided\n")
    show_usage()
    sys.exit(1)

if sys.argv[1] in ['-h', '--help', 'help']:
    show_usage()
    sys.exit(0)

# Parse command
command = sys.argv[1]
print(f"Command: {command}")

if command not in ['deploy', 'backup', 'status']:
    print(f"\nError: Unknown command '{command}'\n")
    show_usage()
    sys.exit(1)

print(f"Would execute: {command}")
