#!/usr/bin/env python3
# sys.argv examples

import sys

"""
READING ARGUMENTS:

python script.py deploy production
  sys.argv[0] = 'script.py'
  sys.argv[1] = 'deploy'
  sys.argv[2] = 'production'

python script.py backup --full /data
  sys.argv[0] = 'script.py'
  sys.argv[1] = 'backup'
  sys.argv[2] = '--full'
  sys.argv[3] = '/data'
"""

print("Command-line arguments:")
print(f"  Total arguments: {len(sys.argv)}")
print(f"  Script name: {sys.argv[0]}")

if len(sys.argv) > 1:
    print(f"\nArguments passed:")
    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"    arg{i}: {arg}")
else:
    print("\nNo arguments provided")
    print(f"\nTry: python {sys.argv[0]} command arg1 arg2")

# Example: Simple command handling
if len(sys.argv) == 2:
    command = sys.argv[1]
    print(f"\nCommand received: {command}")
    
    if command == "status":
        print("Checking status...")
    elif command == "help":
        print("Showing help...")
    else:
        print(f"Unknown command: {command}")
