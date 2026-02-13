#!/usr/bin/env python3
# Common exit codes reference

"""
COMMONLY USED EXIT CODES:

Application-Specific (use these for your tools):
0   - Success
1   - General failure
2   - Invalid usage / arguments
3   - File/resource error
4   - Permission error
5   - Network error
6   - Database error
7   - Timeout
8   - Configuration error

System Codes (less commonly used):
64  - Command line usage error
65  - Data format error
66  - Cannot open input
73  - Can't create output file
74  - I/O error
75  - Temporary failure
77  - Permission denied

Shell Codes (informational):
126 - Command found but not executable
127 - Command not found
128 - Invalid exit code argument
130 - Terminated by Ctrl+C (SIGINT)
"""

import sys

print("EXIT CODE REFERENCE GUIDE")
print("=" * 60)

# Application exit codes
print("\nApplication Exit Codes (0-10):")
print("-" * 60)

app_codes = [
    (0, "SUCCESS", "Operation completed successfully"),
    (1, "GENERAL_ERROR", "Unspecified error occurred"),
    (2, "INVALID_ARGS", "Invalid command-line arguments"),
    (3, "FILE_ERROR", "File not found or cannot be accessed"),
    (4, "PERMISSION_ERROR", "Insufficient permissions"),
    (5, "NETWORK_ERROR", "Network connection failed"),
    (6, "DATABASE_ERROR", "Database operation failed"),
    (7, "TIMEOUT_ERROR", "Operation timed out"),
    (8, "CONFIG_ERROR", "Configuration error"),
    (9, "VALIDATION_ERROR", "Data validation failed"),
    (10, "DEPENDENCY_ERROR", "Missing dependency"),
]

for code, name, description in app_codes:
    print(f"  {code:2d} {name:20s} - {description}")

# Usage examples
print("\n" + "=" * 60)
print("USAGE EXAMPLES")
print("=" * 60)

example_code = """
#!/usr/bin/env python3
import sys

# Define exit codes as constants
EXIT_SUCCESS = 0
EXIT_ERROR = 1
EXIT_INVALID_ARGS = 2
EXIT_FILE_ERROR = 3
EXIT_PERMISSION_ERROR = 4

def main():
    # Check arguments
    if len(sys.argv) < 2:
        print("Error: Missing required argument")
        sys.exit(EXIT_INVALID_ARGS)
    
    filename = sys.argv[1]
    
    # Try to process file
    try:
        with open(filename, 'r') as f:
            data = f.read()
        
        # Process data...
        print(f"Processed {len(data)} bytes")
        sys.exit(EXIT_SUCCESS)
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(EXIT_FILE_ERROR)
        
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'")
        sys.exit(EXIT_PERMISSION_ERROR)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(EXIT_ERROR)

if __name__ == '__main__':
    main()
"""

print(example_code)

# Bash usage
print("=" * 60)
print("CHECKING EXIT CODES IN BASH")
print("=" * 60)

bash_examples = """
# Run script and check exit code
python script.py
if [ $? -eq 0 ]; then
    echo "Success"
else
    echo "Failed with code $?"
fi

# Capture exit code
python script.py
EXIT_CODE=$?
echo "Script exited with code: $EXIT_CODE"

# Use in conditional
if python script.py; then
    echo "Success - do next step"
else
    echo "Failed - skip next step"
fi

# Chain commands (only continue if success)
python step1.py && python step2.py && python step3.py

# Run regardless of previous exit code
python step1.py
python step2.py  # Runs even if step1 failed

# Run only if previous failed
python step1.py || python fallback.py
"""

print(bash_examples)

print("=" * 60)
print("BEST PRACTICES")
print("=" * 60)
print("""
1. Use 0 for success, always
2. Use 1 for general/unknown errors
3. Use 2 for invalid arguments/usage
4. Use 3-10 for specific application errors
5. Document your exit codes
6. Be consistent across related tools
7. Return appropriate codes for automation
8. Use constants, not magic numbers
""")
