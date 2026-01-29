#!/bin/bash
# BEFORE Level 2, Clue 1: Create dummy application logs for backup practice.
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
LOGS_DIR="$LAB_ROOT/data/logs"
TRACKING="$LAB_ROOT/.lab_2_1_logs"

[ -f "$TRACKING" ] && { echo "Clue 2-1 already set up (logs exist)."; exit 0; }

mkdir -p "$LOGS_DIR"

cat > "$LOGS_DIR/app.log" << 'EOF'
[2026-01-29 10:15:23] INFO: Application started successfully
[2026-01-29 10:15:24] INFO: Connected to database
[2026-01-29 10:15:25] INFO: Loaded config from /etc/app/config.yaml
[2026-01-29 10:18:45] WARNING: High memory usage detected (78%)
[2026-01-29 10:20:00] INFO: Health check passed
[2026-01-29 10:22:10] ERROR: Connection timeout to external API
[2026-01-29 10:22:11] INFO: Retry scheduled in 60s
EOF

cat > "$LOGS_DIR/error.log" << 'EOF'
[2026-01-29 10:22:10] ERROR: Connection timeout to external API (host: api.example.com)
[2026-01-29 10:22:10] ERROR: Stack trace: connect() timed out after 5000ms
EOF

echo "app.log" > "$TRACKING"
echo "error.log" >> "$TRACKING"
echo "Clue 2-1: Dummy logs created in data/logs/ (app.log, error.log). Use them for backup practice."
echo "Done."
