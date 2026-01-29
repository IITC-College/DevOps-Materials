#!/bin/bash
# BEFORE Level 2, Clue 1: Start dummy database service for input lab.
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PIDFILE="$LAB_ROOT/.lab_pids_2_1"

[ -f "$PIDFILE" ] && { echo "Clue 2-1 already set up (dummy database service running)."; exit 0; }

chmod +x "$SCRIPT_DIR/dummy_db_service.sh" 2>/dev/null || true
: > "$PIDFILE"
"$SCRIPT_DIR/dummy_db_service.sh" & echo $! >> "$PIDFILE"
echo "Clue 2-1: Dummy database service started. Use check_service.sh with empty input to observe the problem."
echo "Done."
