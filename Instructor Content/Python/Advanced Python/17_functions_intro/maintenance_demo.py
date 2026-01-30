#!/usr/bin/env python3
# Functions make maintenance easier

def format_log(message, level="INFO"):
    # If we need to change the format, we only change it here
    print(f"[{level}] {message}")

# Using the function throughout the code
format_log("Application started")
format_log("User logged in")
format_log("Processing data")
format_log("Error occurred", "ERROR")
format_log("Warning: Low memory", "WARNING")

# To change the format everywhere, just modify the function once!
