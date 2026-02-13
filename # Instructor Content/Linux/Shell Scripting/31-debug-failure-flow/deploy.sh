#!/bin/bash

# Topic 31: Debug & failure flow - real scenario: why deploy failed

CONFIG="${1:-config.txt}"

echo "DEBUG: CONFIG=$CONFIG"
echo "DEBUG: pwd=$(pwd)"
echo "DEBUG: ls=$(ls -la "$CONFIG" 2>&1)"

if [ ! -f "$CONFIG" ]; then
  echo "Error: $CONFIG not found."
  echo "DEBUG: files in $(pwd):"
  ls -la
  exit 1
fi

echo "[$(date '+%H:%M:%S')] Deploying..."
echo "Deploy complete."
exit 0
