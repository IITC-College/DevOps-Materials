#!/bin/bash
# AFTER Level 1, Clue 1: Stop any lab-helper process from this clue (if student started it) and remove PID file.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PIDFILE="$LAB_ROOT/.lab_pids_1_1"

[ ! -f "$PIDFILE" ] && { echo "No processes to stop for Clue 1-1."; exit 0; }

while read -r pid; do
  [ -z "$pid" ] && continue
  kill "$pid" 2>/dev/null && echo "Stopped PID $pid"
done < "$PIDFILE"
rm -f "$PIDFILE"
echo "✓ Cleanup complete for Clue 1-1."
