#!/usr/bin/env python3
# All logging topics in one comprehensive file

import logging
import sys

"""
COMPLETE LOGGING REFERENCE
Covers: basics, vs print, config, file/console, formats, logger objects, handlers
"""

print("LOGGING COMPLETE REFERENCE")
print("="*70)

# TOPIC 1: Why logging vs print
print("\n[1] LOGGING VS PRINT")
print("-"*70)
print("""
print():
  - Simple but limited
  - No levels or timestamps  
  - Hard to disable
  - Not production-ready

logging:
  - Professional
  - Multiple levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
  - Automatic timestamps
  - Easy to configure
  - Production-ready
""")

# TOPIC 2: Basic usage
print("\n[2] BASIC USAGE")
print("-"*70)

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s'
)

logging.debug("Debug - won't show")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

# TOPIC 3: basicConfig
print("\n[3] BASIC CONFIG")
print("-"*70)

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='basic.log',
    force=True
)
print("✓ Configured logging with custom format and file output")

# TOPIC 4: Logger objects
print("\n[4] LOGGER OBJECTS")
print("-"*70)

logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('[%(name)s] %(message)s'))
logger.addHandler(handler)

logger.info("Message from named logger")

# TOPIC 5: Multiple loggers
print("\n[5] MULTIPLE LOGGERS")
print("-"*70)

db_logger = logging.getLogger('database')
api_logger = logging.getLogger('api')

for log in [db_logger, api_logger]:
    log.setLevel(logging.INFO)
    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter('[%(name)s] %(message)s'))
    log.addHandler(h)

db_logger.info("Database connection established")
api_logger.info("API server started")

# TOPIC 6: Log to file
print("\n[6] FILE LOGGING")
print("-"*70)

file_logger = logging.getLogger('file_app')
file_logger.setLevel(logging.INFO)
fh = logging.FileHandler('app_log.log')
fh.setFormatter(logging.Formatter('[%(asctime)s] %(message)s'))
file_logger.addHandler(fh)

file_logger.info("This goes to file")
print("✓ Check app_log.log")

# TOPIC 7: Log format options
print("\n[7] FORMAT OPTIONS")
print("-"*70)

format_examples = """
%(asctime)s     - Timestamp
%(levelname)s   - Level name (INFO, ERROR, etc.)
%(message)s     - Log message
%(name)s        - Logger name
%(filename)s    - Source file
%(lineno)d      - Line number
%(funcName)s    - Function name

Example formats:
  '[%(asctime)s] %(levelname)s: %(message)s'
  '%(levelname)-8s %(message)s'
  '[%(name)s] [%(levelname)s] %(message)s'
"""
print(format_examples)

# TOPIC 8: Log timestamp
print("\n[8] TIMESTAMP FORMATS")
print("-"*70)

logger_ts = logging.getLogger('timestamp')
logger_ts.setLevel(logging.INFO)
h = logging.StreamHandler()
h.setFormatter(logging.Formatter(
    '[%(asctime)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
))
logger_ts.addHandler(h)

logger_ts.info("Custom timestamp format")

# SUMMARY
print("\n"+"="*70)
print("QUICK REFERENCE")
print("="*70)

quick_ref = """
# Basic setup:
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Message")

# File logging:
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s'
)

# File + Console:
logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

# Logger object:
logger = logging.getLogger('myapp')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)
logger.info("Message")

LEVELS (lowest to highest):
  DEBUG    - Detailed information
  INFO     - General information
  WARNING  - Warning messages
  ERROR    - Error messages
  CRITICAL - Critical errors
"""
print(quick_ref)
