#!/bin/bash
# AFTER Level 1, Clue 2: Stop dummy web service.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PIDFILE="$LAB_ROOT/.lab_pids_1_2"

[ ! -f "$PIDFILE" ] && { echo "No Clue 1-2 processes to stop."; exit 0; }

while read -r pid; do
  [ -z "$pid" ] && continue
  kill "$pid" 2>/dev/null && echo "Stopped PID $pid"
done < "$PIDFILE"
rm -f "$PIDFILE"
echo "Clue 1-2 cleanup complete."
echo "Done."
