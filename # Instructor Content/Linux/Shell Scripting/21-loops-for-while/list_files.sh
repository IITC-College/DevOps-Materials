#!/bin/bash

# Real scenario: process each log file in /var/log/app (or ./logs)

LOG_DIR="${1:-logs}"
echo "[$(date '+%H:%M:%S')] Processing logs in $LOG_DIR..."

for LOG in "$LOG_DIR"/*.log 2>/dev/null; do
  if [ -f "$LOG" ]; then
    echo "  Rotating $LOG..."
    echo "  [simulated] gzip $LOG"
    echo "  Done: $LOG"
  fi
done
echo "[$(date '+%H:%M:%S')] Log rotation complete."
