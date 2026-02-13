#!/bin/bash

# Real case: [ -z ] empty input, [ -d ] path must be a directory

read -p "Backup path: " BACKUP_PATH

if [ -z "$BACKUP_PATH" ]; then
  echo "Error: path cannot be empty."
elif [ -d "$BACKUP_PATH" ]; then
  echo "Backing up from $BACKUP_PATH..."
  echo "Backup finished."
else
  echo "Error: $BACKUP_PATH is not a directory."
fi
