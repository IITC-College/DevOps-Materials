#!/usr/bin/env python3
# Logging basics

import logging

"""
LOGGING MODULE:

Advantages over print():
- Levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Timestamps automatic
- Can log to file and console
- Can disable/enable easily
- Production-ready
- Formatting control

BASIC USAGE:
  import logging
  logging.basicConfig(level=logging.INFO)
  logging.info("Message")
  logging.warning("Warning")
  logging.error("Error")
"""

# Example 1: Basic logging
print("Example 1: Basic logging")
print("-" * 40)

logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
logging.warning("This is a warning")
logging.error("This is an error")

# Example 2: Logging levels
print("\nExample 2: Different log levels")
print("-" * 40)

logging.debug("Debug message (won't show with INFO level)")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

# Example 3: Custom format
print("\nExample 3: Custom format")
print("-" * 40)

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True  # Override previous config
)

logging.info("Application started")
logging.info("Processing data")
logging.warning("Low memory")

# Example 4: Log to file
print("\nExample 4: Logging to file")
print("-" * 40)

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    force=True
)

logging.info("Logged to file")
logging.error("Error logged to file")
print("✓ Check app.log file")

# Example 5: Log to both file and console
print("\nExample 5: Log to file AND console")
print("-" * 40)

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ],
    force=True
)

logging.info("This goes to both file and console")
logging.warning("Warning in both places")

print("\nKey concepts:")
print("  • logging.info() instead of print()")
print("  • Automatic timestamps")
print("  • Multiple levels")
print("  • File and console output")
print("  • Professional logging")
