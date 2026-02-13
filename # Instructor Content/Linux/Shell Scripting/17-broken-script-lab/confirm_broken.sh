#!/bin/bash

# BROKEN - real case: restart prod - wrong condition

read -p "Restart production? (yes/no): " CONFIRM

if [ $CONFIRM = "yes" ]; then
  echo "Restarting..."
  echo "Done."
else
  echo "Cancelled."
fi
