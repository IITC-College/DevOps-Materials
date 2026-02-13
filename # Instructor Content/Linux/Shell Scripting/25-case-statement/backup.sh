#!/bin/bash

# Real scenario: backup type - full / incremental / config-only

read -p "Backup type (full/incremental/config): " TYPE

case "$TYPE" in
  full)
    echo "[$(date '+%H:%M:%S')] Full backup..."
    echo "  Dumping database..."
    echo "  Archiving /var/log/app, /etc/app, /opt/app..."
    echo "  Target: /backup/full-$(date +%Y%m%d).tar.gz"
    echo "[$(date '+%H:%M:%S')] Full backup done."
    ;;
  incremental)
    echo "[$(date '+%H:%M:%S')] Incremental backup..."
    echo "  Syncing changed files since last run..."
    echo "  Target: /backup/incr-$(date +%Y%m%d-%H%M).tar.gz"
    echo "[$(date '+%H:%M:%S')] Incremental backup done."
    ;;
  config)
    echo "[$(date '+%H:%M:%S')] Config backup only..."
    echo "  Copying /etc/app/*.conf -> /backup/config-$(date +%Y%m%d).tar.gz"
    echo "[$(date '+%H:%M:%S')] Config backup done."
    ;;
  *)
    echo "Error: use full, incremental, or config."
    ;;
esac
