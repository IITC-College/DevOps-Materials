#!/bin/bash
# Setup for Level 2 Clue 3: install and start lab-demo user service.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
USER_UNIT_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"
UNIT_FILE="$USER_UNIT_DIR/lab-demo.service"

mkdir -p "$USER_UNIT_DIR"
chmod +x "$SCRIPT_DIR/dummy_daemon.sh" 2>/dev/null || true

cat > "$UNIT_FILE" << EOF
[Unit]
Description=Lab demo service for systemd practice
After=network.target

[Service]
Type=simple
ExecStart=$LAB_ROOT/scripts/dummy_daemon.sh
Restart=no

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload 2>/dev/null || { echo "Warning: systemctl --user daemon-reload failed. Ensure you have a user D-Bus session (e.g. logged in graphically or via SSH)."; exit 1; }
systemctl --user start lab-demo 2>/dev/null || true
echo "Lab demo service installed (clue 2-3). Run: systemctl --user status lab-demo"
