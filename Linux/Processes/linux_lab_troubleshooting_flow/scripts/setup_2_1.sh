#!/bin/bash
# BEFORE Level 2, Clue 1: Install lab-troubleshoot user service and STOP it (scenario: service stopped).
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
USER_UNIT_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"
UNIT_FILE="$USER_UNIT_DIR/lab-troubleshoot.service"
TRACKING="$LAB_ROOT/.lab_2_1_service"

[ -f "$TRACKING" ] && { echo "Clue 2-1 service already configured."; exit 0; }

mkdir -p "$USER_UNIT_DIR"
chmod +x "$SCRIPT_DIR/dummy_daemon.sh" 2>/dev/null || true

cat > "$UNIT_FILE" << EOF
[Unit]
Description=Lab troubleshooting demo service
After=network.target

[Service]
Type=simple
ExecStart=$LAB_ROOT/scripts/dummy_daemon.sh
Restart=no

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload 2>/dev/null || { echo "Warning: systemctl --user daemon-reload failed. Ensure you have a user D-Bus session (e.g. logged in graphically or via SSH)."; exit 1; }
systemctl --user stop lab-troubleshoot 2>/dev/null || true
touch "$TRACKING"
echo "✓ Clue 2-1 scenario ready: lab-troubleshoot service is installed but STOPPED. Apply the flow: service? status? logs? next action?"
echo "  Run: systemctl --user status lab-troubleshoot"
