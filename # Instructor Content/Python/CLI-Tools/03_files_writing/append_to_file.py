#!/usr/bin/env python3
# Appending to files

"""
APPEND MODE ('a'):

- Adds content to end of file
- Creates file if doesn't exist
- Never overwrites existing content
- Perfect for logs

COMMON USES:
- Log files
- Audit trails
- Incremental data
- History tracking
"""

import datetime

# Example 1: Basic append
print("Example 1: Basic append")
print("-" * 40)

# Create initial file
with open('notes.txt', 'w') as f:
    f.write("Note 1: Initial content\n")

# Append to it
with open('notes.txt', 'a') as f:
    f.write("Note 2: Added later\n")
    f.write("Note 3: Added even later\n")

with open('notes.txt', 'r') as f:
    print("Content:")
    print(f.read())

# Example 2: Logging function
print("\nExample 2: Logging function")
print("-" * 40)

def log(message, level="INFO"):
    """Append log message to file"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] [{level}] {message}\n"
    
    with open('application.log', 'a') as f:
        f.write(log_line)
    
    print(f"Logged: {message}")

log("Application started")
log("User logged in", "INFO")
log("High memory usage", "WARNING")
log("Database error", "ERROR")

print("\nLog file contents:")
with open('application.log', 'r') as f:
    print(f.read())

# Example 3: Append creates file if missing
print("\nExample 3: Append creates file")
print("-" * 40)

import os

filename = 'newfile.txt'
if os.path.exists(filename):
    os.remove(filename)
    print(f"Removed {filename}")

# Append creates it
with open(filename, 'a') as f:
    f.write("Created with append mode\n")

print(f"✓ {filename} created")

# Example 4: Activity log
print("\nExample 4: Activity tracking")
print("-" * 40)

def track_activity(user, action):
    """Track user activities"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('activity.log', 'a') as f:
        f.write(f"{timestamp} | {user} | {action}\n")

track_activity("alice", "login")
track_activity("alice", "view_dashboard")
track_activity("bob", "login")
track_activity("alice", "deploy_app")
track_activity("bob", "run_backup")

print("Activity log:")
with open('activity.log', 'r') as f:
    for line in f:
        print(f"  {line.strip()}")

# Example 5: Daily report appending
print("\nExample 5: Daily reports")
print("-" * 40)

def add_daily_report(date, metrics):
    """Append daily metrics to report"""
    with open('daily_report.txt', 'a') as f:
        f.write(f"\n{'='*40}\n")
        f.write(f"Report for {date}\n")
        f.write(f"{'='*40}\n")
        for key, value in metrics.items():
            f.write(f"{key}: {value}\n")

add_daily_report("2024-01-15", {
    "requests": 1234,
    "errors": 5,
    "uptime": "99.9%"
})

add_daily_report("2024-01-16", {
    "requests": 1456,
    "errors": 2,
    "uptime": "100%"
})

print("Daily reports:")
with open('daily_report.txt', 'r') as f:
    print(f.read())

# Example 6: Write vs Append comparison
print("\nExample 6: Write vs Append")
print("-" * 40)

# Write mode
with open('compare_w.txt', 'w') as f:
    f.write("First\n")
with open('compare_w.txt', 'w') as f:
    f.write("Second\n")

# Append mode
with open('compare_a.txt', 'w') as f:
    f.write("First\n")
with open('compare_a.txt', 'a') as f:
    f.write("Second\n")

with open('compare_w.txt', 'r') as f:
    print(f"Write mode result: {f.read().strip()}")

with open('compare_a.txt', 'r') as f:
    print(f"Append mode result:\n{f.read()}")

print("Key points:")
print("  ✓ 'a' mode never overwrites")
print("  ✓ Perfect for logs")
print("  ✓ Creates file if missing")
print("  ✓ Always adds to end")
