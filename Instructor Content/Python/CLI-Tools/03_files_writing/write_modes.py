#!/usr/bin/env python3
# File writing modes

"""
FILE MODES:

'w'  - Write mode (overwrites, creates if not exists)
'a'  - Append mode (adds to end, creates if not exists)
'x'  - Exclusive create (fails if file exists)
'w+' - Write and read
'a+' - Append and read

TEXT vs BINARY:
't'  - Text mode (default)
'b'  - Binary mode
"""

# Mode 'w': Write (overwrites)
print("Mode 'w': Write (overwrites)")
print("-" * 40)

with open('mode_w.txt', 'w') as f:
    f.write("First write\n")

with open('mode_w.txt', 'w') as f:
    f.write("Second write (overwrites first)\n")

with open('mode_w.txt', 'r') as f:
    print(f"Content: {f.read().strip()}")

# Mode 'a': Append (adds to end)
print("\nMode 'a': Append (adds to end)")
print("-" * 40)

with open('mode_a.txt', 'w') as f:
    f.write("Line 1\n")

with open('mode_a.txt', 'a') as f:
    f.write("Line 2\n")

with open('mode_a.txt', 'a') as f:
    f.write("Line 3\n")

with open('mode_a.txt', 'r') as f:
    print("Content:")
    print(f.read())

# Mode 'x': Exclusive create
print("Mode 'x': Exclusive create (fails if exists)")
print("-" * 40)

try:
    with open('mode_x.txt', 'x') as f:
        f.write("Created with 'x' mode\n")
    print("✓ File created")
except FileExistsError:
    print("✗ File already exists")

# Try again - should fail
try:
    with open('mode_x.txt', 'x') as f:
        f.write("This won't work\n")
except FileExistsError:
    print("✗ Cannot create - file exists")

# Mode comparison
print("\nMode comparison:")
print("-" * 40)

modes_comparison = """
'w' → Creates or overwrites
      Use: When you want fresh content

'a' → Creates or appends
      Use: For logs, incremental data

'x' → Creates only (safe mode)
      Use: When file shouldn't exist

'w+' → Write and read
       Use: When you need both

'a+' → Append and read
       Use: Append + verify
"""

print(modes_comparison)

# Practical example: Log file
print("Practical: Appending to log file")
print("-" * 40)

import datetime

def log_message(message):
    """Append log message to file"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('app.log', 'a') as f:
        f.write(f"[{timestamp}] {message}\n")

log_message("Application started")
log_message("User logged in")
log_message("Data processed")

with open('app.log', 'r') as f:
    print("Log contents:")
    print(f.read())

print("\nBest practices:")
print("  'w' → Complete rewrite")
print("  'a' → Add to existing (logs)")
print("  'x' → Prevent overwrites")
