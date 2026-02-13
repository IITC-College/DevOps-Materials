#!/usr/bin/env python3
# Using os module

import os

# Get current working directory
cwd = os.getcwd()
print(f"Current directory: {cwd}")

# Get environment variable
home = os.getenv("HOME", "not_found")
print(f"HOME: {home}")

user = os.getenv("USER", "unknown")
print(f"USER: {user}")

# Check if path exists
exists = os.path.exists(".")
print(f"Current dir exists: {exists}")

# Join paths
path = os.path.join("folder", "subfolder", "file.txt")
print(f"Joined path: {path}")

# Get file basename and dirname
full_path = "/home/user/documents/file.txt"
basename = os.path.basename(full_path)
dirname = os.path.dirname(full_path)
print(f"Basename: {basename}")
print(f"Dirname: {dirname}")
