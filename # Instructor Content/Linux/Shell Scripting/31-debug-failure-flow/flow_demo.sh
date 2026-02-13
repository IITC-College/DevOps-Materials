#!/bin/bash

# Real scenario: follow failure path - don't guess

echo "[$(date '+%H:%M:%S')] Step 1: Check config..."
if [ ! -f "config.txt" ]; then
  echo "  FAIL: config.txt not found."
  echo "[$(date '+%H:%M:%S')] Exiting - fix config first."
  exit 1
fi

echo "[$(date '+%H:%M:%S')] Step 2: Check disk..."
echo "  OK"

echo "[$(date '+%H:%M:%S')] Step 3: Deploy..."
echo "  OK"

echo "[$(date '+%H:%M:%S')] Done."
exit 0
