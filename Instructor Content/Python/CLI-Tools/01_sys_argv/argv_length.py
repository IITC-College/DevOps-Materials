#!/usr/bin/env python3
# Checking sys.argv length

import sys

"""
CHECK ARGUMENT COUNT:

len(sys.argv) tells you how many arguments (including script name)

Examples:
  python script.py          → len(sys.argv) = 1
  python script.py arg1     → len(sys.argv) = 2
  python script.py a b c    → len(sys.argv) = 4

Use length to validate input:
  - Require exact number of arguments
  - Require minimum number
  - Check if optional arguments present
"""

arg_count = len(sys.argv)

print(f"Total items in sys.argv: {arg_count}")
print(f"Number of arguments (excluding script): {arg_count - 1}")
print()

# Check for exact number
if arg_count == 1:
    print("No arguments provided")
    print(f"Usage: python {sys.argv[0]} <command> [options]")
elif arg_count == 2:
    print(f"One argument provided: {sys.argv[1]}")
elif arg_count == 3:
    print(f"Two arguments provided: {sys.argv[1]}, {sys.argv[2]}")
else:
    print(f"Multiple arguments provided: {sys.argv[1:]}")

# Require minimum number
print("\nValidation example:")
if len(sys.argv) < 2:
    print("Error: Command required")
    print(f"Usage: python {sys.argv[0]} <command>")
else:
    command = sys.argv[1]
    print(f"Command: {command}")
    
    # Check for optional second argument
    if len(sys.argv) >= 3:
        option = sys.argv[2]
        print(f"Option: {option}")
