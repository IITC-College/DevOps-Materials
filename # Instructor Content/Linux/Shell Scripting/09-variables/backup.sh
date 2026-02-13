#!/bin/bash

# Common mistake: VAR = value (wrong - spaces)
# Right: VAR=value

BACKUP_DIR="/backup/logs"
DATE=$(date +%Y-%m-%d)

echo "Backing up to $BACKUP_DIR"
echo "Date: $DATE"
echo "Backup done."
