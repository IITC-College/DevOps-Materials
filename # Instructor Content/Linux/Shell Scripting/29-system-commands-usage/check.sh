#!/bin/bash

# Real scenario: ops runbook - uptime + disk before investigating

echo "[$(date '+%H:%M:%S')] Pre-check (before restart/deploy):"
echo "  Uptime: $(uptime -p 2>/dev/null || uptime)"
echo "  Disk: $(df -h . 2>/dev/null | tail -1)"
echo "  Memory: $(free -h 2>/dev/null | grep Mem | awk '{print $3 "/" $2}')"
echo "  Status: OK"
