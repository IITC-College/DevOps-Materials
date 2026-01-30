#!/usr/bin/env python3
# Importing external libraries vs built-in modules

"""
BUILT-IN MODULES (No installation needed)
- Come with Python
- Always available
- Import directly
"""

# Built-in modules
import datetime
import json
import random
import os
import sys
import math

print("Built-in modules (always available):")
print(f"  datetime: {datetime.date.today()}")
print(f"  random: {random.randint(1, 10)}")
print(f"  math: pi = {math.pi}")
print()

"""
EXTERNAL LIBRARIES (Need installation)
- Not included with Python
- Install with pip
- Then import
"""

print("External libraries (need pip install):")
print()

# Try to import requests (external)
try:
    import requests
    print("✓ requests - pip install requests")
    print("  Used for: HTTP requests")
except ImportError:
    print("✗ requests - pip install requests")
    print("  Used for: HTTP requests")

print()

# Try to import flask (external)
try:
    import flask
    print("✓ flask - pip install flask")
    print("  Used for: Web applications")
except ImportError:
    print("✗ flask - pip install flask")
    print("  Used for: Web applications")

print()

# Try to import pandas (external)
try:
    import pandas
    print("✓ pandas - pip install pandas")
    print("  Used for: Data analysis")
except ImportError:
    print("✗ pandas - pip install pandas")
    print("  Used for: Data analysis")

print()

# Try to import colorama (external)
try:
    from colorama import Fore, Style, init
    init()
    print(Fore.GREEN + "✓ colorama - pip install colorama" + Style.RESET_ALL)
    print("  Used for: Colored terminal output")
except ImportError:
    print("✗ colorama - pip install colorama")
    print("  Used for: Colored terminal output")

print()

"""
HOW TO TELL IF MODULE IS BUILT-IN:

1. Try importing without installing
   - If it works → built-in
   - If ImportError → external

2. Check Python docs: https://docs.python.org/3/library/
   - Listed there → built-in

3. Check PyPI: https://pypi.org/
   - Listed there → external

COMMON BUILT-IN MODULES:
  os, sys, datetime, json, math, random, re, 
  collections, itertools, functools, urllib

COMMON EXTERNAL LIBRARIES:
  requests, flask, django, pandas, numpy, 
  pytest, sqlalchemy, celery, beautifulsoup4
"""

print("\nTo install external libraries:")
print("  pip install library_name")
