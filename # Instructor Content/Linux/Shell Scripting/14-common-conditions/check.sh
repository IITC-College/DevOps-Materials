#!/bin/bash

# Real case: [ -d ] - log dir must exist before we check logs

LOG_DIR="logs"

if [ -d "$LOG_DIR" ]; then
  echo "Log directory exists. Checking..."
  echo "Status: OK"
else
  echo "Error: $LOG_DIR not found. Create logs dir first."
fi
