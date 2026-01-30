#!/usr/bin/env python3
# Demonstrating virtual environment activation

"""
When you activate a virtual environment:

1. Your command prompt changes to show (venv)
2. Python and pip commands use the venv versions
3. Packages installed go into venv, not globally

Example session:

$ python -m venv myproject_venv
$ source myproject_venv/bin/activate  # Linux/Mac
$ # or myproject_venv\Scripts\activate  # Windows

(myproject_venv) $ which python
/path/to/myproject_venv/bin/python

(myproject_venv) $ pip install requests
# Installs only in this venv

(myproject_venv) $ deactivate
$  # Back to global environment
"""

print("Virtual environment activation is a shell operation")
print("Not a Python script you run directly")
print("See venv_commands.txt for commands")
