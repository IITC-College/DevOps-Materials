#!/bin/bash

# Real scenario: backup one path, call for logs + config + db dump

backup_path() {
  echo "  [$(date '+%H:%M:%S')] Backing up $1 -> /backup/$(date +%Y-%m-%d)/"
  echo "  $1: done"
}

echo "[$(date '+%H:%M:%S')] Backup started."
backup_path /var/log/app
backup_path /etc/app
backup_path "db_dump.sql"
echo "[$(date '+%H:%M:%S')] Backup finished."
