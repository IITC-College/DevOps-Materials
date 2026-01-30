#!/bin/bash
# BEFORE Level 3, Clue 3: "Logs tell you which" – write to log that lab-troubleshoot SERVICE should be running; do NOT start it.
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
USER_UNIT_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"
UNIT_FILE="$USER_UNIT_DIR/lab-troubleshoot.service"
LOG_DIR="$LAB_ROOT/data/logs"
LOG_FILE="$LOG_DIR/troubleshoot_hint.log"
TRACKING="$LAB_ROOT/.lab_3_3_service"

[ -f "$TRACKING" ] && { echo "Clue 3-3 already configured."; exit 0; }

mkdir -p "$LOG_DIR"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Incident: lab-troubleshoot SERVICE should be running. Check systemctl --user status lab-troubleshoot and start if stopped." > "$LOG_FILE"

mkdir -p "$USER_UNIT_DIR"
chmod +x "$SCRIPT_DIR/dummy_daemon.sh" 2>/dev/null || true
cat > "$UNIT_FILE" << EOF
[Unit]
Description=Lab troubleshooting demo service (Level 3 – logs tell you)
After=network.target

[Service]
Type=simple
ExecStart=$LAB_ROOT/scripts/dummy_daemon.sh
Restart=no

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload 2>/dev/null || { echo "Warning: systemctl --user daemon-reload failed."; exit 1; }
systemctl --user stop lab-troubleshoot 2>/dev/null || true
touch "$TRACKING"
echo "✓ Clue 3-3 scenario ready: the LOG tells you what to check (process or service?). Read data/logs/troubleshoot_hint.log and apply the flow."
