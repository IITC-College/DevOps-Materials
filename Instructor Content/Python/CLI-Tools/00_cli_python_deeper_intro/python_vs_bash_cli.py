#!/usr/bin/env python3
# Python vs Bash for CLI tools

"""
WHEN TO USE BASH:

✓ Simple file operations
  - cp, mv, rm files
  - chmod, chown
  - grep, sed, awk

✓ Gluing existing commands
  - Piping commands together
  - For loops over files
  - Quick one-liners

✓ System administration
  - Already know bash
  - Native to Linux/Mac
  - No dependencies

Example Bash script:
  for file in *.txt; do
    grep "ERROR" "$file" >> errors.log
  done

WHEN TO USE PYTHON:

✓ Complex logic
  - Data structures (lists, dicts)
  - Object-oriented design
  - Error handling

✓ String processing
  - Parsing logs
  - Formatting output
  - Regular expressions

✓ Cross-platform
  - Works on Windows, Linux, Mac
  - Same code everywhere

✓ API integration
  - HTTP requests (requests library)
  - JSON parsing
  - External services

✓ Data processing
  - CSV, Excel files
  - Database connections
  - Mathematical operations

Example Python CLI:
  import sys
  import requests
  
  def fetch_data(api_key):
      response = requests.get(f"https://api.example.com/data")
      return response.json()
  
  if __name__ == "__main__":
      data = fetch_data(sys.argv[1])
      print(f"Found {len(data)} items")

COMPARISON:

Task: Count lines in files

Bash (simpler):
  wc -l *.txt

Python (more control):
  for file in glob.glob("*.txt"):
      with open(file) as f:
          lines = len(f.readlines())
          print(f"{file}: {lines} lines")

BEST PRACTICE:

- Start with bash for simple tasks
- Use Python when bash gets messy
- Use Python for production tools
- Combine both: bash calls Python when needed
"""

print("Bash: Great for simple file operations and gluing commands")
print("Python: Better for complex logic, cross-platform, and production tools")
print("\nRule of thumb:")
print("  < 50 lines of logic? → Bash is fine")
print("  > 50 lines or complex? → Use Python")
