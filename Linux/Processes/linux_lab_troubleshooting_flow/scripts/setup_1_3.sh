#!/bin/bash
# BEFORE Level 1, Clue 3: Prepare "process disappeared" scenario – write to log, do NOT start process.
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
LOG_DIR="$LAB_ROOT/data/logs"
LOG_FILE="$LOG_DIR/lab_helper.log"

mkdir -p "$LOG_DIR"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] lab-helper was running, then exited (exit code 1)." >> "$LOG_FILE"
echo "✓ Clue 1-3 scenario ready: process disappeared. Apply the flow: process? status (not in ps)? logs? next action?"
