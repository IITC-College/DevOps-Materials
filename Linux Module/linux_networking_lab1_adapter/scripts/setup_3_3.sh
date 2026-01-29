#!/bin/bash
# Setup for Level 3, Clue 3
# Run this BEFORE students start clues/level3/clue3.txt

SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
exec sudo "$SCRIPT_DIR/setup_environment.sh" 3 3
