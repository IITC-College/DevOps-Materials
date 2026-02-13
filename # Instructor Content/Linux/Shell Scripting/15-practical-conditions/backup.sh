#!/bin/bash

# Real case: backup dir - create if missing, else use existing

BACKUP_DIR="backup"

if [ ! -d "$BACKUP_DIR" ]; then
  mkdir "$BACKUP_DIR"
  echo "Created $BACKUP_DIR"
else
  echo "Using existing $BACKUP_DIR"
fi

echo "Backing up..."
echo "Backup finished."
