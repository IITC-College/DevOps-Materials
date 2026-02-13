#!/bin/bash

# Repetitive task: backing up logs
# Without script: do this manually every day

echo "Backing up application logs..."
echo "Source: /var/log/app"
echo "Target: /backup/logs/$(date +%Y-%m-%d)"
echo ""
echo "Files backed up:"
echo "  - app.log"
echo "  - error.log"
echo "  - access.log"
echo ""
echo "Backup completed at $(date +%H:%M:%S)"
echo ""
echo "Without script: You'd type all this daily"
echo "With script: Just run ./backup_logs.sh"
