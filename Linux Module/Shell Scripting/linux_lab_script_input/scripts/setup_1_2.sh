#!/bin/bash
# BEFORE Level 1, Clue 2: Start dummy web service for input lab.
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PIDFILE="$LAB_ROOT/.lab_pids_1_2"

[ -f "$PIDFILE" ] && { echo "Clue 1-2 already set up (dummy web service running)."; exit 0; }

chmod +x "$SCRIPT_DIR/dummy_web_service.sh" 2>/dev/null || true
: > "$PIDFILE"
"$SCRIPT_DIR/dummy_web_service.sh" & echo $! >> "$PIDFILE"
echo "Clue 1-2: Dummy web service started. Use check_service.sh and enter 'web' when prompted."
echo "Done."
