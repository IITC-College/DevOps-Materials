#!/bin/bash
# BEFORE Level 2, Clue 1: Start process that ignores SIGTERM (needs kill -9).
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PIDFILE="$LAB_ROOT/.lab_pids_2_1"

[ -f "$PIDFILE" ] && { echo "Clue 2-1 process already running."; exit 0; }

chmod +x "$SCRIPT_DIR/dummy_stubborn_process.sh" 2>/dev/null || true
: > "$PIDFILE"
"$SCRIPT_DIR/dummy_stubborn_process.sh" & echo $! >> "$PIDFILE"
echo "✓ Dummy process (stubborn, ignores SIGTERM) started for Clue 2-1."
