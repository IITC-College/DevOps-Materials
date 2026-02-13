#!/bin/bash

# Text + variables in one echo

BACKUP_DIR="/backup"
DATE=$(date +%Y-%m-%d)
TIME=$(date +%H:%M)

echo "Backup to $BACKUP_DIR started at $TIME"
echo "Date: $DATE"
echo "Backup finished."
