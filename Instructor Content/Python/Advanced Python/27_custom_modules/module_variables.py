#!/usr/bin/env python3
# Module with variables and functions

# Module-level variables
APP_NAME = "DevOps Tool"
VERSION = "1.0.0"
MAX_RETRIES = 3

def get_app_info():
    """Return app information"""
    return f"{APP_NAME} v{VERSION}"

def get_max_retries():
    """Return max retries setting"""
    return MAX_RETRIES

# Use in another file:
# import module_variables
# print(module_variables.APP_NAME)
# print(module_variables.get_app_info())
