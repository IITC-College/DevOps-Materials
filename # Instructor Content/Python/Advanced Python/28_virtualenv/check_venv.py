#!/usr/bin/env python3
# Check if running in a virtual environment

import sys

def is_venv():
    """Check if running in virtual environment"""
    return hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )

if is_venv():
    print("Running in a virtual environment")
    print(f"Virtual env path: {sys.prefix}")
else:
    print("Running in global Python environment")
    print(f"Python path: {sys.prefix}")

# Show Python executable location
print(f"Python executable: {sys.executable}")

# Show Python version
print(f"Python version: {sys.version}")
