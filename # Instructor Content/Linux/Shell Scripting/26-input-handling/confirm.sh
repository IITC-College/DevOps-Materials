#!/bin/bash

# Real scenario: production restart - require explicit yes

read -p "Restart PRODUCTION app? Type 'yes' to confirm: " CONFIRM

if [ "$CONFIRM" != "yes" ]; then
  echo "Cancelled. Type exactly 'yes' to confirm."
  exit 1
fi

echo "[$(date '+%H:%M:%S')] Restarting production app..."
echo "  Stopping app..."
echo "  Starting app..."
echo "[$(date '+%H:%M:%S')] App restarted."
