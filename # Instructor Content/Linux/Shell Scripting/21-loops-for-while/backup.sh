#!/bin/bash

# Real scenario: retry backup until success or max attempts

MAX_ATTEMPTS=3
ATTEMPT=1
BACKUP_TARGET="/backup/$(date +%Y-%m-%d)"

echo "[$(date '+%H:%M:%S')] Backup to $BACKUP_TARGET"
while [ $ATTEMPT -le $MAX_ATTEMPTS ]; do
  echo "  Attempt $ATTEMPT/$MAX_ATTEMPTS..."
  echo "  [simulated] rsync -av /var/data/ $BACKUP_TARGET/"
  echo "  Backup completed."
  break
  ATTEMPT=$((ATTEMPT + 1))
done
echo "[$(date '+%H:%M:%S')] Backup finished."
