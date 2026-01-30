#!/bin/bash
# BEFORE Level 2, Clue 2: Start one normal process for "try graceful first" discussion.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PIDFILE="$LAB_ROOT/.lab_pids_2_2"

[ -f "$PIDFILE" ] && { echo "Clue 2-2 process already running."; exit 0; }

chmod +x "$SCRIPT_DIR/dummy_normal_process.sh" 2>/dev/null || true
: > "$PIDFILE"
"$SCRIPT_DIR/dummy_normal_process.sh" & echo $! >> "$PIDFILE"
echo "✓ Dummy process started for Clue 2-2 (practice graceful stop first)."
