#!/usr/bin/env python3
# Complete guide to logging levels

import logging

"""
LOGGING LEVELS COMPLETE GUIDE

Covers: all levels, when to use each, hierarchy, setting levels, examples
"""

print("LOGGING LEVELS - COMPLETE GUIDE")
print("="*70)

# Setup logging
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)-8s] %(message)s'
)

# ALL LEVELS
print("\n[1] ALL LOGGING LEVELS")
print("-"*70)

levels_info = """
DEBUG (10)    - Detailed diagnostic information
INFO (20)     - General informational messages
WARNING (30)  - Warning messages (something unexpected)
ERROR (40)    - Error messages (functionality affected)
CRITICAL (50) - Critical errors (program may not continue)

Hierarchy: DEBUG < INFO < WARNING < ERROR < CRITICAL
"""
print(levels_info)

# DEMONSTRATIONS
print("\n[2] LEVEL DEMONSTRATIONS")
print("-"*70)

logging.debug("DEBUG: Variable x = 42, entering function foo()")
logging.info("INFO: User 'alice' logged in")
logging.warning("WARNING: Disk space is 85% full")
logging.error("ERROR: Failed to connect to database")
logging.critical("CRITICAL: Out of memory, shutting down")

# WHEN TO USE EACH
print("\n[3] WHEN TO USE EACH LEVEL")
print("-"*70)

usage_guide = """
DEBUG:
  - Development/troubleshooting
  - Variable values, function calls
  - Detailed execution flow
  Example: logging.debug(f"Processing item {i} of {total}")

INFO:
  - Normal program operation
  - Major milestones
  - User actions
  Example: logging.info("Application started successfully")

WARNING:
  - Unexpected but handled situations
  - Deprecated features
  - Non-critical issues
  Example: logging.warning("Using deprecated API, please upgrade")

ERROR:
  - Errors that affect functionality
  - Failed operations
  - Exceptions caught
  Example: logging.error("Failed to save file: permission denied")

CRITICAL:
  - Severe errors
  - Program cannot continue
  - System-level failures
  Example: logging.critical("Database unavailable, shutting down")
"""
print(usage_guide)

# SETTING LEVELS
print("\n[4] SETTING LOG LEVELS")
print("-"*70)

# basicConfig
logging.basicConfig(level=logging.INFO, force=True)
print("Set level to INFO:")
logging.debug("  This won't show (DEBUG < INFO)")
logging.info("  This shows (INFO >= INFO)")
logging.warning("  This shows (WARNING > INFO)")

# Logger object
custom_logger = logging.getLogger('custom')
custom_logger.setLevel(logging.WARNING)
handler = logging.StreamHandler()
custom_logger.addHandler(handler)

print("\nCustom logger at WARNING level:")
custom_logger.info("  Won't show")
custom_logger.warning("  Shows")
custom_logger.error("  Shows")

# HIERARCHY
print("\n[5] LEVEL HIERARCHY & FILTERING")
print("-"*70)

hierarchy_explanation = """
If log level set to WARNING:
  DEBUG   → ✗ Filtered out
  INFO    → ✗ Filtered out
  WARNING → ✓ Shows
  ERROR   → ✓ Shows
  CRITICAL → ✓ Shows

Rule: Messages at or above the set level are shown.

Production: Usually INFO or WARNING
Development: Usually DEBUG
"""
print(hierarchy_explanation)

# NUMERIC VALUES
print("\n[6] NUMERIC LEVEL VALUES")
print("-"*70)

print(f"DEBUG    = {logging.DEBUG}")
print(f"INFO     = {logging.INFO}")
print(f"WARNING  = {logging.WARNING}")
print(f"ERROR    = {logging.ERROR}")
print(f"CRITICAL = {logging.CRITICAL}")

# PRACTICAL EXAMPLES
print("\n[7] PRACTICAL EXAMPLES")
print("-"*70)

# Simulation
def process_user_request(user_id):
    """Example function with different log levels"""
    logger = logging.getLogger('app')
    logger.setLevel(logging.DEBUG)
    h = logging.StreamHandler()
    logger.addHandler(h)
    
    logger.debug(f"Starting request processing for user {user_id}")
    logger.info(f"User {user_id} authenticated")
    
    if user_id == "admin":
        logger.warning("Admin user detected, elevated permissions granted")
    
    try:
        # Simulate operation
        if user_id == "error_user":
            raise Exception("Database error")
        logger.info(f"Request processed successfully for {user_id}")
    except Exception as e:
        logger.error(f"Failed to process request: {e}")

process_user_request("alice")
print()
process_user_request("admin")
print()
process_user_request("error_user")

# SUMMARY
print("\n"+"="*70)
print("QUICK REFERENCE")
print("="*70)

summary = """
# Set level globally:
logging.basicConfig(level=logging.INFO)

# Set level for specific logger:
logger = logging.getLogger('myapp')
logger.setLevel(logging.DEBUG)

# Use in code:
logging.debug("Detailed info")
logging.info("General info")
logging.warning("Warning")
logging.error("Error occurred")
logging.critical("Critical failure")

BEST PRACTICES:
  ✓ Use DEBUG for development
  ✓ Use INFO for production
  ✓ Use WARNING for deprecations/issues
  ✓ Use ERROR for failures
  ✓ Use CRITICAL for severe errors

PRODUCTION SETTING:
  logging.basicConfig(level=logging.INFO)
  
DEVELOPMENT SETTING:
  logging.basicConfig(level=logging.DEBUG)
"""
print(summary)
