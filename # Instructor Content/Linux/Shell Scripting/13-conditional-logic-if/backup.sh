#!/bin/bash

# Real case: confirm before backup (destructive action)

read -p "Backup will overwrite existing. Continue? (yes/no): " CONFIRM

if [ "$CONFIRM" = "yes" ]; then
  echo "Backing up..."
  echo "Backup finished."
else
  echo "Backup cancelled."
fi
