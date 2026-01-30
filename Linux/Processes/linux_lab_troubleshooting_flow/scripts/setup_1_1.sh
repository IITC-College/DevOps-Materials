#!/bin/bash
# BEFORE Level 1, Clue 1: Prepare "lab-helper not running" scenario. Do NOT start the process.
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
LOG_DIR="$LAB_ROOT/data/logs"
LOG_FILE="$LOG_DIR/lab_helper.log"

mkdir -p "$LOG_DIR"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] lab-helper expected but not running – no process found." > "$LOG_FILE"
echo "✓ Clue 1-1 scenario ready: lab-helper is not running. Check with the flow (process? status? logs? next action)."
echo "  Log written to data/logs/lab_helper.log"
