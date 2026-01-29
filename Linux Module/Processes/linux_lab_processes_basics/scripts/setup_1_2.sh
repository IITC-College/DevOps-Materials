#!/bin/bash
# BEFORE Level 1, Clue 2: Start dummy processes for this clue.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PIDFILE="$LAB_ROOT/.lab_pids_1_2"

[ -f "$PIDFILE" ] && { echo "Clue 1-2 processes already running."; exit 0; }

chmod +x "$SCRIPT_DIR/dummy_cpu_eater.sh" 2>/dev/null || true
: > "$PIDFILE"
"$SCRIPT_DIR/dummy_cpu_eater.sh" & echo $! >> "$PIDFILE"
echo "✓ Dummy processes started for Clue 1-2."
