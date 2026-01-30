#!/usr/bin/env python3
# sys.argv vs input() - When to use each

import sys

"""
sys.argv vs input()

USE sys.argv WHEN:
- Building CLI tools
- Script called by other scripts
- Automation/batch processing
- Non-interactive use
- One-shot commands

USE input() WHEN:
- Interactive programs
- User needs to see prompts
- Multiple inputs needed
- Dynamic questions based on previous answers
- User-friendly interface

EXAMPLES:

CLI with sys.argv:
  python backup.py --full /data
  → Non-interactive, scriptable

Interactive with input():
  python backup.py
  → "Which directory? "
  → "/data"
  → "Full or incremental? "
  → "full"

BEST OF BOTH WORLDS:
Accept arguments if provided, prompt if not
"""

def backup(directory=None, backup_type=None):
    """Perform backup with flexible input"""
    
    # Use sys.argv if provided
    if directory is None and len(sys.argv) > 1:
        directory = sys.argv[1]
    
    if backup_type is None and len(sys.argv) > 2:
        backup_type = sys.argv[2]
    
    # Fall back to input() if still missing
    if directory is None:
        directory = input("Directory to backup: ")
    
    if backup_type is None:
        backup_type = input("Backup type (full/incremental): ")
    
    print(f"\nBacking up {directory} ({backup_type})")
    return True

# Demonstration
print("Flexible Backup Tool\n")

if len(sys.argv) >= 3:
    print("Using command-line arguments:")
    print(f"  Directory: {sys.argv[1]}")
    print(f"  Type: {sys.argv[2]}")
    backup()
elif len(sys.argv) == 2:
    print(f"Using CLI for directory: {sys.argv[1]}")
    print("Will prompt for backup type")
    backup()
else:
    print("No arguments provided")
    print("Will prompt for all inputs\n")
    backup()

print("\nExamples:")
print(f"  python {sys.argv[0]} /data full")
print(f"  python {sys.argv[0]} /data")
print(f"  python {sys.argv[0]}")
