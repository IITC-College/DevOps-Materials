#!/bin/bash
# Setup for Level 2, Clue 1
# Run this BEFORE students start clues/level2/clue1.txt

SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
exec sudo "$SCRIPT_DIR/setup_environment.sh" 2 1
