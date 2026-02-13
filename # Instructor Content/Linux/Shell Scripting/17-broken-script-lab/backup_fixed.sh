#!/bin/bash

# FIXED: $BACKUP_DIR not BACKUP_DIR, add fi, fix else block

BACKUP_DIR="backup"

if [ ! -d "$BACKUP_DIR" ]; then
  mkdir "$BACKUP_DIR"
  echo "Created backup dir"
else
  echo "Using existing dir"
fi
echo "Backup finished."
