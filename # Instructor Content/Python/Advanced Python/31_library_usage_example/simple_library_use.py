#!/usr/bin/env python3
# Simple example of using external libraries

"""
TYPICAL WORKFLOW:

1. Find library you need
2. Install it: pip install library_name
3. Import it in your code
4. Use it!
"""

# Example 1: Using requests for HTTP
print("Example 1: requests library")
print("-" * 40)

try:
    import requests
    
    response = requests.get('https://api.github.com')
    print(f"Status: {response.status_code}")
    print("✓ requests is working!")
    
except ImportError:
    print("✗ requests not installed")
    print("  Install: pip install requests")

print()

# Example 2: Using colorama for colors
print("Example 2: colorama library")
print("-" * 40)

try:
    from colorama import Fore, Style, init
    init()
    
    print(Fore.GREEN + "✓ colorama is working!" + Style.RESET_ALL)
    
except ImportError:
    print("✗ colorama not installed")
    print("  Install: pip install colorama")

print()

# Example 3: Using python-dateutil for dates
print("Example 3: python-dateutil library")
print("-" * 40)

try:
    from dateutil import parser
    
    date_str = "2026-01-30 14:30:00"
    parsed = parser.parse(date_str)
    print(f"Parsed date: {parsed}")
    print("✓ python-dateutil is working!")
    
except ImportError:
    print("✗ python-dateutil not installed")
    print("  Install: pip install python-dateutil")

print()

# Built-in modules (no installation needed)
print("Built-in modules (always available):")
print("-" * 40)

import datetime
import json
import random

print("✓ datetime")
print("✓ json")
print("✓ random")
print("\nThese come with Python!")
