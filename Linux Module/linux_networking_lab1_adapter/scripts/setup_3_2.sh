#!/bin/bash
# Setup for Level 3, Clue 2
# WARNING: May drop SSH connections - use VM console!
# Run this BEFORE students start clues/level3/clue2.txt

SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
exec sudo "$SCRIPT_DIR/setup_environment.sh" 3 2
