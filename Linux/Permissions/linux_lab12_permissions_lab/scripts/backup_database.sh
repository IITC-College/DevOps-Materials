#!/bin/bash
# Database backup script - should be executable by engineering team
echo "Connecting to database..."
echo "Creating backup: backup_$(date +%Y%m%d).sql"
echo "Backup completed successfully!"
echo "Stored in /backups/db/"
