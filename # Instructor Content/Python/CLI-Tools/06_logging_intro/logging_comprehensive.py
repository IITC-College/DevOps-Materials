#!/usr/bin/env python3
# Comprehensive logging guide

import logging
import sys

"""
COMPLETE LOGGING GUIDE

Topics covered:
- Basic logging
- Logging to file
- Logging to console
- Custom formats
- Logger objects
- Multiple handlers
"""

print("="*60)
print("COMPREHENSIVE LOGGING EXAMPLES")
print("="*60)

# 1. BASIC CONFIGURATION
print("\n1. Basic Configuration")
print("-"*60)

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info("Application started")
logging.warning("This is a warning")
logging.error("This is an error")

# 2. LOGGING LEVELS
print("\n2. Logging Levels")
print("-"*60)

levels = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}

for name, level in levels.items():
    print(f"  {name}: {level}")

# 3. FILE LOGGING
print("\n3. File Logging")
print("-"*60)

file_logger = logging.getLogger('file_logger')
file_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('application.log')
file_handler.setFormatter(
    logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
)
file_logger.addHandler(file_handler)

file_logger.info("Logged to file")
file_logger.error("Error logged to file")
print("✓ Check application.log")

# 4. CONSOLE AND FILE
print("\n4. Console and File Logging")
print("-"*60)

dual_logger = logging.getLogger('dual_logger')
dual_logger.setLevel(logging.INFO)

# File handler
fh = logging.FileHandler('dual.log')
fh.setLevel(logging.INFO)
fh.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s'))

# Console handler  
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
ch.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))

dual_logger.addHandler(fh)
dual_logger.addHandler(ch)

dual_logger.info("This appears in both console and file")
dual_logger.warning("Warning in both places")

# 5. PRACTICAL PATTERNS
print("\n5. Practical Logging Patterns")
print("-"*60)

# Setup function
def setup_logging(log_file='app.log', level=logging.INFO):
    """Setup logging with file and console handlers"""
    logger = logging.getLogger('app')
    logger.setLevel(level)
    
    # Clear existing handlers
    logger.handlers = []
    
    # File handler
    fh = logging.FileHandler(log_file)
    fh.setFormatter(logging.Formatter(
        '[%(asctime)s] [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    ))
    logger.addHandler(fh)
    
    # Console handler
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
    logger.addHandler(ch)
    
    return logger

# Use it
app_logger = setup_logging('myapp.log')
app_logger.info("Application initialized")
app_logger.info("Processing data...")
app_logger.warning("Low disk space")
app_logger.error("Failed to connect to database")

# 6. WHY LOGGING > PRINT
print("\n6. Why Logging is Better Than Print")
print("-"*60)

comparison = """
Feature          | print()         | logging
-----------------+-----------------+------------------
Timestamps       | Manual          | Automatic
Levels           | No              | Yes (5 levels)
File output      | Manual redirect | Built-in
Disable easily   | Remove code     | Change level
Production ready | No              | Yes
Formatting       | Manual          | Configurable
Multiple outputs | Hard            | Easy (handlers)
Thread-safe      | Not guaranteed  | Yes
"""
print(comparison)

print("\n"+"="*60)
print("Key Takeaways:")
print("="*60)
print("""
1. Use logging instead of print() in production code
2. Set appropriate levels (DEBUG for development, INFO for production)
3. Log to both file (for history) and console (for monitoring)
4. Use structured format with timestamps
5. Create logger objects for better control
6. Configure once at application startup
""")
