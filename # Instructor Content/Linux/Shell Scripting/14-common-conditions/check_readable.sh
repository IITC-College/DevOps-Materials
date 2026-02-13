#!/bin/bash

# Real case: [ -r ] - file exists AND we can read it

CONFIG="config.txt"

if [ -f "$CONFIG" ] && [ -r "$CONFIG" ]; then
  echo "Config exists and is readable. Loading..."
  echo "Config loaded."
elif [ -f "$CONFIG" ]; then
  echo "Error: $CONFIG exists but is not readable (permissions?)."
else
  echo "Error: $CONFIG not found."
fi
