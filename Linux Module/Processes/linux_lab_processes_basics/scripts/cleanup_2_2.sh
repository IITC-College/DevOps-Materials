#!/bin/bash
# AFTER Level 2, Clue 2: Stop dummy processes from this clue.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PIDFILE="$LAB_ROOT/.lab_pids_2_2"

[ ! -f "$PIDFILE" ] && { echo "No processes to stop for Clue 2-2."; exit 0; }

while read -r pid; do
  [ -z "$pid" ] && continue
  kill "$pid" 2>/dev/null && echo "Stopped PID $pid"
done < "$PIDFILE"
rm -f "$PIDFILE"
echo "✓ Cleanup complete for Clue 2-2."
