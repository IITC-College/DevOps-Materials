#!/bin/bash
# AFTER Level 3, Clue 1: Remove any PID file; no service to stop.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PIDFILE="$LAB_ROOT/.lab_pids_3_1"

[ ! -f "$PIDFILE" ] && { echo "No processes to stop for Clue 3-1."; exit 0; }
while read -r pid; do
  [ -z "$pid" ] && continue
  kill "$pid" 2>/dev/null && echo "Stopped PID $pid"
done < "$PIDFILE"
rm -f "$PIDFILE"
echo "✓ Cleanup complete for Clue 3-1."
