#!/usr/bin/env python3
# Indexing sys.argv

import sys

"""
ACCESSING ARGUMENTS BY INDEX:

sys.argv[0]  → Script name (always present)
sys.argv[1]  → First argument
sys.argv[2]  → Second argument
sys.argv[-1] → Last argument

CAREFUL: Check length before accessing!
"""

print("Demonstrating sys.argv indexing:\n")

# Always safe (script name)
print(f"sys.argv[0] = {sys.argv[0]}")

# Check before accessing
if len(sys.argv) > 1:
    print(f"sys.argv[1] = {sys.argv[1]}")
else:
    print("sys.argv[1] = (not provided)")

if len(sys.argv) > 2:
    print(f"sys.argv[2] = {sys.argv[2]}")
else:
    print("sys.argv[2] = (not provided)")

# Last argument (if any)
if len(sys.argv) > 1:
    print(f"sys.argv[-1] = {sys.argv[-1]}")

# Safe access with .get() alternative using try/except
print("\nSafe access example:")
try:
    third_arg = sys.argv[3]
    print(f"Third argument: {third_arg}")
except IndexError:
    print("Third argument not provided")

# Better approach: check length
print("\nBetter approach:")
if len(sys.argv) >= 4:
    print(f"Third argument: {sys.argv[3]}")
else:
    print("Need at least 3 arguments")
