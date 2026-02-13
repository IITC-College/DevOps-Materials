#!/usr/bin/env python3
# How to read library documentation

"""
WHERE TO FIND LIBRARY DOCUMENTATION:

1. PYPI PAGE
   https://pypi.org/project/package-name/
   - Basic information
   - Installation instructions
   - Links to full documentation

2. OFFICIAL DOCUMENTATION
   Usually linked from PyPI page
   Examples:
   - requests: https://requests.readthedocs.io/
   - flask: https://flask.palletsprojects.com/
   - pandas: https://pandas.pydata.org/docs/

3. GITHUB REPOSITORY
   - README.md file
   - Examples folder
   - Issues and discussions

4. IN PYTHON HELP
   import requests
   help(requests)
   help(requests.get)

WHAT TO LOOK FOR IN DOCS:

1. INSTALLATION
   pip install package_name

2. QUICK START / TUTORIAL
   Basic usage example

3. API REFERENCE
   All functions and classes

4. EXAMPLES
   Real-world usage

5. FAQ / TROUBLESHOOTING
   Common problems and solutions

EXAMPLE: requests library

# 1. Find on PyPI
https://pypi.org/project/requests/

# 2. Read Quick Start
https://requests.readthedocs.io/en/latest/user/quickstart/

# 3. Basic usage from docs:
import requests
response = requests.get('https://api.github.com')
print(response.status_code)

# 4. Check help in Python
help(requests.get)

# 5. Try examples from docs

READING DOCUMENTATION TIPS:

✓ Start with Quick Start or Tutorial
✓ Run examples in your own environment
✓ Modify examples to understand them
✓ Keep documentation open while coding
✓ Search docs for specific functions
✓ Check examples in GitHub repo
✓ Look at real projects using the library

DON'T:
✗ Read entire docs top to bottom
✗ Try to memorize everything
✗ Use library without reading any docs
"""

print("To read library documentation:")
print("1. Visit PyPI: https://pypi.org/project/library-name/")
print("2. Find link to official docs")
print("3. Start with Quick Start or Tutorial")
print("4. Run examples yourself")
print("5. Reference API docs when needed")
