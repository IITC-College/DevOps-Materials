#!/bin/bash

# Real case: backup fails - echo BACKUP_DIR, check permissions with ls -l

BACKUP_DIR="backup"

# echo "DEBUG: BACKUP_DIR=$BACKUP_DIR"

if [ ! -d "$BACKUP_DIR" ]; then
  mkdir "$BACKUP_DIR"
  echo "Created $BACKUP_DIR"
fi

echo "Backing up..."
echo "Backup finished."
# If something fails: add echo right before the failing line
