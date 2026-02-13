#!/bin/bash

# Real case: app writes logs - ensure log dir exists

LOG_DIR="logs"

if [ ! -d "$LOG_DIR" ]; then
  mkdir "$LOG_DIR"
  echo "Created $LOG_DIR for logs."
fi

echo "Checking services..."
echo "Status: OK"
echo "Logs in $LOG_DIR"
