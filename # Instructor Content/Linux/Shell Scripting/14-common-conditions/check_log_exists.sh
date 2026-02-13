#!/bin/bash

# Real case: [ -f ] - only tail log if file exists

LOG_FILE="logs/app.log"

if [ -f "$LOG_FILE" ]; then
  echo "Log file exists. Showing last 5 lines..."
  echo "[simulated] tail -5 $LOG_FILE"
  echo "Done."
else
  echo "Error: $LOG_FILE not found. App may not have started."
fi
