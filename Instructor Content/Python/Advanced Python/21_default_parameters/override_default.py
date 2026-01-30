#!/usr/bin/env python3
# Overriding default parameters

def log_message(message, level="INFO", timestamp=True):
    if timestamp:
        print(f"[{level}] {message} (timestamp enabled)")
    else:
        print(f"[{level}] {message}")

# Use all defaults
log_message("Application started")

# Override level
log_message("Error occurred", level="ERROR")

# Override timestamp
log_message("Debug info", timestamp=False)

# Override both
log_message("Critical issue", level="CRITICAL", timestamp=True)
