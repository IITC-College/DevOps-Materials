#!/usr/bin/env python3
# Handling flags in sys.argv

import sys

"""
HANDLING FLAGS:

Flags are optional arguments that change behavior:
  -v, --verbose
  -q, --quiet
  -f, --force
  -h, --help

Examples:
  python script.py deploy
  python script.py deploy -v
  python script.py deploy --verbose
  python script.py -v deploy
"""

# Check for flags
verbose = False
force = False
command = None

print("Parsing arguments...\n")

# Parse all arguments
for arg in sys.argv[1:]:
    if arg in ['-v', '--verbose']:
        verbose = True
    elif arg in ['-f', '--force']:
        force = True
    elif arg in ['-h', '--help']:
        print(f"Usage: python {sys.argv[0]} [options] <command>")
        print("\nOptions:")
        print("  -v, --verbose    Verbose output")
        print("  -f, --force      Force operation")
        print("  -h, --help       Show this help")
        sys.exit(0)
    elif not arg.startswith('-'):
        command = arg

# Show what was parsed
print("Parsed flags:")
print(f"  Verbose: {verbose}")
print(f"  Force: {force}")
print(f"  Command: {command}")

# Use flags
if command:
    if verbose:
        print(f"\n[VERBOSE] Executing command: {command}")
    
    if force:
        print(f"[FORCE] Skipping confirmations")
    
    print(f"\nExecuting: {command}")
else:
    print("\nError: No command specified")

print("\nExamples:")
print(f"  python {sys.argv[0]} deploy")
print(f"  python {sys.argv[0]} -v deploy")
print(f"  python {sys.argv[0]} --verbose --force backup")
