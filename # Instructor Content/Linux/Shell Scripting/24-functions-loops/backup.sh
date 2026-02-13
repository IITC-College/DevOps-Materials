#!/bin/bash

# Real scenario: backup each dir in list with same logic

backup_dir() {
  echo "  [$(date '+%H:%M:%S')] $1 -> /backup/$(date +%Y-%m-%d)/$(basename "$1")"
  echo "  Done: $1"
}

DIRS="/var/log/app /etc/app /opt/app/data"
echo "[$(date '+%H:%M:%S')] Backup started."
for DIR in $DIRS; do
  backup_dir "$DIR"
done
echo "[$(date '+%H:%M:%S')] Backup finished."
