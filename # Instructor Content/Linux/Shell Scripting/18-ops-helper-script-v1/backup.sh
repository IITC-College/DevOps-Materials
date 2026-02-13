#!/bin/bash

# Ops Helper style: confirm, then act

read -p "Backup? (yes/no): " CONFIRM

if [ "$CONFIRM" = "yes" ]; then
  echo "Backing up..."
  echo "Backup finished."
else
  echo "Backup cancelled."
fi
