#!/usr/bin/env python3
# sys.argv basics

"""
sys.argv = System Arguments Vector

A list containing command-line arguments passed to the Python script

STRUCTURE:
  sys.argv[0] = script name
  sys.argv[1] = first argument
  sys.argv[2] = second argument
  ...

EXAMPLE:
  python script.py arg1 arg2 arg3
  
  sys.argv = ['script.py', 'arg1', 'arg2', 'arg3']
  sys.argv[0] = 'script.py'
  sys.argv[1] = 'arg1'
  sys.argv[2] = 'arg2'
  sys.argv[3] = 'arg3'
  len(sys.argv) = 4

WHY sys.argv?

- Accept commands from command line
- Build CLI tools
- Automate without user interaction
- Script can be called from other scripts

NO ARGUMENTS:
  python script.py
  sys.argv = ['script.py']
  len(sys.argv) = 1
"""

import sys

print("sys.argv contents:")
print(f"  Full list: {sys.argv}")
print(f"  Length: {len(sys.argv)}")
print()

if len(sys.argv) > 0:
    print(f"Script name: {sys.argv[0]}")

if len(sys.argv) > 1:
    print(f"First argument: {sys.argv[1]}")

if len(sys.argv) > 2:
    print(f"Second argument: {sys.argv[2]}")

print()
print("Try running:")
print(f"  python {sys.argv[0]} hello world")
