#!/bin/bash

# Topic 20: Opening & Ops Mindset
# Real scenario: script runs in production - not a toy

echo "[$(date '+%Y-%m-%d %H:%M:%S')] === Ops Session Started ==="
echo ""
echo "Environment: production-like"
echo "Scripts here: deploy, health-check, backup, rollback"
echo "Standard: clear logs, exit codes, no silent failures"
echo ""
echo "[$(date '+%H:%M:%S')] Ready for ops commands."
