#!/bin/bash
# AFTER Level 2, Clue 1: Remove dummy application logs.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
LOGS_DIR="$LAB_ROOT/data/logs"
TRACKING="$LAB_ROOT/.lab_2_1_logs"

[ ! -f "$TRACKING" ] && { echo "No Clue 2-1 logs to clean up."; exit 0; }

rm -f "$LOGS_DIR/app.log" "$LOGS_DIR/error.log" 2>/dev/null || true
rm -f "$TRACKING"
echo "Clue 2-1 cleanup complete (dummy logs removed)."
echo "Done."
