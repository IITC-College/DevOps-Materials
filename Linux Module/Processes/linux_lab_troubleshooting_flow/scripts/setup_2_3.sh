#!/bin/bash
# BEFORE Level 2, Clue 3: Install lab-troubleshoot service with daemon that RUNS but writes ERROR to logs.
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
USER_UNIT_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"
UNIT_FILE="$USER_UNIT_DIR/lab-troubleshoot.service"
TRACKING="$LAB_ROOT/.lab_2_3_service"

[ -f "$TRACKING" ] && { echo "Clue 2-3 service already configured."; exit 0; }

mkdir -p "$USER_UNIT_DIR"
chmod +x "$SCRIPT_DIR/dummy_daemon_error_log.sh" 2>/dev/null || true

cat > "$UNIT_FILE" << EOF
[Unit]
Description=Lab troubleshooting demo service (running but error in logs)
After=network.target

[Service]
Type=simple
ExecStart=$LAB_ROOT/scripts/dummy_daemon_error_log.sh
Restart=no

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload 2>/dev/null || { echo "Warning: systemctl --user daemon-reload failed. Ensure you have a user D-Bus session."; exit 1; }
systemctl --user start lab-troubleshoot 2>/dev/null || true
touch "$TRACKING"
echo "✓ Clue 2-3 scenario ready: lab-troubleshoot service is RUNNING but logs show errors (app not responding). Apply the flow: service? status? logs? next action?"
echo "  Run: systemctl --user status lab-troubleshoot ; journalctl --user -u lab-troubleshoot -n 20"
