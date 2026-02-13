#!/usr/bin/env python3
# Exit code conventions

"""
STANDARD EXIT CODES:

0   = Success (everything OK)
1   = General error
2   = Misuse/invalid arguments  
3-125 = Custom error codes
126 = Command cannot execute
127 = Command not found
128 = Invalid exit argument
130 = Terminated by Ctrl+C

CONVENTION:
- 0 = Success, non-zero = Failure
- Use specific codes for different errors
- Document your exit codes
"""

import sys

print("Standard Exit Codes")
print("=" * 50)

exit_codes = {
    0: "Success",
    1: "General error",
    2: "Misuse of command (invalid arguments)",
    64: "Command line usage error",
    65: "Data format error",
    66: "Cannot open input",
    67: "Addressee unknown",
    68: "Host name unknown",
    69: "Service unavailable",
    70: "Internal software error",
    71: "System error",
    72: "Critical OS file missing",
    73: "Can't create output file",
    74: "Input/output error",
    75: "Temp failure",
    76: "Remote error in protocol",
    77: "Permission denied",
    78: "Configuration error",
    126: "Command invoked cannot execute",
    127: "Command not found",
    128: "Invalid argument to exit",
    130: "Script terminated by Ctrl+C"
}

for code, description in exit_codes.items():
    print(f"  {code:3d}: {description}")

print("\nCustom Exit Codes Example:")
print("-" * 50)

# Define custom codes
EXIT_SUCCESS = 0
EXIT_ERROR = 1
EXIT_INVALID_ARGS = 2
EXIT_FILE_NOT_FOUND = 3
EXIT_PERMISSION_DENIED = 4
EXIT_NETWORK_ERROR = 5
EXIT_DATABASE_ERROR = 6

custom_codes = {
    EXIT_SUCCESS: "Operation successful",
    EXIT_ERROR: "General error",
    EXIT_INVALID_ARGS: "Invalid command-line arguments",
    EXIT_FILE_NOT_FOUND: "Required file not found",
    EXIT_PERMISSION_DENIED: "Permission denied",
    EXIT_NETWORK_ERROR: "Network connection failed",
    EXIT_DATABASE_ERROR: "Database operation failed"
}

for code, desc in custom_codes.items():
    print(f"  {code}: {desc}")

print("\nUsage Example:")
print("-" * 50)
print("""
#!/usr/bin/env python3
import sys

EXIT_SUCCESS = 0
EXIT_FILE_ERROR = 3

def main():
    try:
        with open('config.json', 'r') as f:
            config = f.read()
        # Process config...
        sys.exit(EXIT_SUCCESS)
    except FileNotFoundError:
        print("Error: config.json not found")
        sys.exit(EXIT_FILE_ERROR)

if __name__ == '__main__':
    main()

# In bash:
# python script.py
# if [ $? -eq 0 ]; then
#     echo "Success"
# else
#     echo "Failed with code $?"
# fi
""")

print("\nBest Practices:")
print("  ✓ Use 0 for success")
print("  ✓ Use 1 for general errors")
print("  ✓ Use specific codes (2-125) for different errors")
print("  ✓ Document your exit codes")
print("  ✓ Be consistent across your tools")
