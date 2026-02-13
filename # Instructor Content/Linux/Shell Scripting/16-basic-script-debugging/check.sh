#!/bin/bash

# Real case: check fails - add echo to see SERVICE and LOG_DIR

SERVICE="web"
LOG_DIR="logs"

# echo "DEBUG: SERVICE=$SERVICE LOG_DIR=$LOG_DIR"

if [ -d "$LOG_DIR" ]; then
  echo "Checking $SERVICE..."
  echo "Status: OK"
else
  echo "Error: $LOG_DIR not found."
  echo "Current dir: $(pwd)"
  ls -l
fi
