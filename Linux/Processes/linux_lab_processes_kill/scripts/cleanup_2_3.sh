#!/bin/bash
# AFTER Level 2, Clue 3: Stop stuck process (requires kill -9).
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PIDFILE="$LAB_ROOT/.lab_pids_2_3"

[ ! -f "$PIDFILE" ] && { echo "No processes to stop for Clue 2-3."; exit 0; }

while read -r pid; do
  [ -z "$pid" ] && continue
  kill -9 "$pid" 2>/dev/null && echo "Stopped PID $pid (SIGKILL)"
done < "$PIDFILE"
rm -f "$PIDFILE"
echo "✓ Cleanup complete for Clue 2-3."
