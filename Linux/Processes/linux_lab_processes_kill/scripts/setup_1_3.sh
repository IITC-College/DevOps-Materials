#!/bin/bash
# BEFORE Level 1, Clue 3: Start 2-3 dummy processes for finding and stopping.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PIDFILE="$LAB_ROOT/.lab_pids_1_3"

[ -f "$PIDFILE" ] && { echo "Clue 1-3 processes already running."; exit 0; }

chmod +x "$SCRIPT_DIR/dummy_normal_process.sh" 2>/dev/null || true
: > "$PIDFILE"
"$SCRIPT_DIR/dummy_normal_process.sh" & echo $! >> "$PIDFILE"
"$SCRIPT_DIR/dummy_normal_process.sh" & echo $! >> "$PIDFILE"
"$SCRIPT_DIR/dummy_normal_process.sh" & echo $! >> "$PIDFILE"
echo "✓ Three dummy processes started for Clue 1-3."
