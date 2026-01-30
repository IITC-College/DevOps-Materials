#!/bin/bash
# BEFORE Level 3, Clue 1: Combined – "only a process" scenario. lab-helper (process) not running.
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
LOG_DIR="$LAB_ROOT/data/logs"
LOG_FILE="$LOG_DIR/lab_helper.log"

mkdir -p "$LOG_DIR"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] lab-helper (process) expected but not running." > "$LOG_FILE"
echo "✓ Clue 3-1 scenario ready: this is a PROCESS-only scenario (no service). lab-helper is not running. Apply the flow."
