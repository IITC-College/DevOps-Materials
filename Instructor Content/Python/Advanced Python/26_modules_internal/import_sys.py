#!/usr/bin/env python3
# Using sys module

import sys

# Python version
print(f"Python version: {sys.version}")

# Platform
print(f"Platform: {sys.platform}")

# Command line arguments
print(f"Script name: {sys.argv[0]}")
print(f"All arguments: {sys.argv}")

# Python path
print("Python path (first 3):")
for path in sys.path[:3]:
    print(f"  {path}")

# Exit with code (commented out to not exit)
# sys.exit(0)  # Exit with success
# sys.exit(1)  # Exit with error

print("Script continues...")
