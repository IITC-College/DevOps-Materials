#!/bin/bash

# FIXED: quote $CONFIRM (empty input breaks [ = ] without quotes)

read -p "Restart production? (yes/no): " CONFIRM

if [ "$CONFIRM" = "yes" ]; then
  echo "Restarting..."
  echo "Done."
else
  echo "Cancelled."
fi
