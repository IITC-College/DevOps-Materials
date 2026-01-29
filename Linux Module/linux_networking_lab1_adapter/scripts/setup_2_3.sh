#!/bin/bash
# Setup for Level 2, Clue 3
# Run this BEFORE students start clues/level2/clue3.txt

SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
exec sudo "$SCRIPT_DIR/setup_environment.sh" 2 3
