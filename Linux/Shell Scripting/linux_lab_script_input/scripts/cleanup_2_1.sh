#!/bin/bash
# AFTER Level 2, Clue 1: Stop dummy database service.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PIDFILE="$LAB_ROOT/.lab_pids_2_1"

[ ! -f "$PIDFILE" ] && { echo "No Clue 2-1 processes to stop."; exit 0; }

while read -r pid; do
  [ -z "$pid" ] && continue
  kill "$pid" 2>/dev/null && echo "Stopped PID $pid"
done < "$PIDFILE"
rm -f "$PIDFILE"
echo "Clue 2-1 cleanup complete."
echo "Done."
