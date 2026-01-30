#!/bin/bash
# BEFORE Level 1: Create operational environment (logs, configs) for ops helper lab.
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
OPS_ENV="$LAB_ROOT/data/ops_env"
TRACKING="$LAB_ROOT/.lab_1_1_ops_env"

[ -f "$TRACKING" ] && { echo "Clue 1-1 already set up (ops_env exists)."; exit 0; }

mkdir -p "$OPS_ENV/logs" "$OPS_ENV/configs"

cat > "$OPS_ENV/configs/app.conf" << 'EOF'
# App config
APP_NAME=webapp
PORT=8080
ENV=production
EOF

cat > "$OPS_ENV/logs/app.log" << 'EOF'
[2026-01-29 10:15:23] INFO: Application started
[2026-01-29 10:15:24] INFO: Listening on port 8080
[2026-01-29 10:18:45] WARNING: High memory usage (75%)
[2026-01-29 10:20:00] INFO: Health check OK
EOF

echo "ops_env" > "$TRACKING"
echo "Clue 1-1: Operational environment created in data/ops_env/ (logs, configs). Use ops_helper.sh with deploy/check/backup."
echo "Done."
