#!/bin/bash

# Real scenario: timestamp in deploy log for audit

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Deploy started."
echo "  User: $(whoami)"
echo "  Host: $(hostname)"
echo "  Disk before: $(df -h . 2>/dev/null | tail -1 | awk '{print $5}')"
echo "  Deploying..."
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Deploy complete."
