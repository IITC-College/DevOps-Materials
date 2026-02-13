#!/bin/bash

# Real case: script fails on "config not found"
# Step 1: add echo to see CONFIG value and pwd
# Step 2: ls -l to see what files exist in current dir

CONFIG="${1:-config.txt}"

echo "DEBUG: CONFIG=$CONFIG"
echo "DEBUG: pwd=$(pwd)"

if [ -f "$CONFIG" ]; then
  echo "Config found. Loading..."
  echo "Done."
else
  echo "Error: $CONFIG not found."
  echo "Files in current dir:"
  ls -l
fi
