#!/bin/bash
# Setup for Level 1, Clue 2
# Run this BEFORE students start clues/level1/clue2.txt

SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
exec sudo "$SCRIPT_DIR/setup_environment.sh" 1 2
