#!/bin/bash
# BEFORE Level 2, Clue 3: Start "stuck" process (ignores SIGTERM) for real-world scenario.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PIDFILE="$LAB_ROOT/.lab_pids_2_3"

[ -f "$PIDFILE" ] && { echo "Clue 2-3 process already running."; exit 0; }

chmod +x "$SCRIPT_DIR/dummy_stubborn_process.sh" 2>/dev/null || true
: > "$PIDFILE"
"$SCRIPT_DIR/dummy_stubborn_process.sh" & echo $! >> "$PIDFILE"
echo "✓ Stuck process started for Clue 2-3 (try kill, then kill -9)."
