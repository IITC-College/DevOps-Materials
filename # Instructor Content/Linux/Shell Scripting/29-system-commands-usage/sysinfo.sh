#!/bin/bash

# Topic 29: System commands - real ops info
# date, uptime, df, free - used in monitoring/runbooks

echo "[$(date '+%Y-%m-%d %H:%M:%S')] === System Info ==="
echo ""
echo "Date: $(date)"
echo "Uptime: $(uptime -p 2>/dev/null || uptime)"
echo ""
echo "Disk usage (current dir):"
df -h . 2>/dev/null || echo "  (df not available)"
echo ""
echo "Memory:"
free -h 2>/dev/null || echo "  (free not available)"
echo ""
echo "Load average: $(uptime | sed 's/.*load average: //' 2>/dev/null || uptime)"
echo "[$(date '+%H:%M:%S')] Done."
