#!/bin/bash

# Real case: ensure multiple dirs exist before running app

LOG_DIR="logs"
BACKUP_DIR="backup"
TMP_DIR="tmp"

for DIR in "$LOG_DIR" "$BACKUP_DIR" "$TMP_DIR"; do
  if [ ! -d "$DIR" ]; then
    mkdir "$DIR"
    echo "Created $DIR"
  fi
done

echo "All dirs ready. Starting app..."
