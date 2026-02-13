#!/usr/bin/env python3
# Validating sys.argv arguments

import sys

"""
VALIDATE ARGUMENTS:

1. Check count
2. Check types (convert strings)
3. Check values (allowed options)
4. Provide helpful error messages
"""

def validate_args():
    """Validate command-line arguments"""
    
    # Check if command provided
    if len(sys.argv) < 2:
        print("Error: No command provided")
        print(f"Usage: python {sys.argv[0]} <command>")
        return False
    
    command = sys.argv[1]
    
    # Validate command
    valid_commands = ["start", "stop", "status", "restart"]
    if command not in valid_commands:
        print(f"Error: Invalid command '{command}'")
        print(f"Valid commands: {', '.join(valid_commands)}")
        return False
    
    # If command is 'start', check for port number
    if command == "start":
        if len(sys.argv) < 3:
            print("Error: 'start' command requires port number")
            print(f"Usage: python {sys.argv[0]} start <port>")
            return False
        
        # Validate port is a number
        try:
            port = int(sys.argv[2])
            if port < 1 or port > 65535:
                print(f"Error: Port must be between 1 and 65535")
                return False
        except ValueError:
            print(f"Error: Port must be a number, got '{sys.argv[2]}'")
            return False
    
    return True

# Main execution
print("Validating arguments...\n")

if validate_args():
    command = sys.argv[1]
    print(f"✓ Valid command: {command}")
    
    if command == "start" and len(sys.argv) >= 3:
        port = sys.argv[2]
        print(f"✓ Port: {port}")
        print(f"\nWould start server on port {port}")
    else:
        print(f"\nWould execute: {command}")
else:
    print("\n✗ Validation failed")

print("\nExample valid commands:")
print(f"  python {sys.argv[0]} status")
print(f"  python {sys.argv[0]} start 8080")
print(f"  python {sys.argv[0]} stop")
