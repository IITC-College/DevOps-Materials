#!/bin/bash
# BEFORE Level 1, Clue 2: Start lab-logger-ok service for filtering by unit.
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
USER_UNIT_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"
UNIT_FILE="$USER_UNIT_DIR/lab-logger-ok.service"
TRACKING="$LAB_ROOT/.lab_1_2_service"

[ -f "$TRACKING" ] && { echo "Clue 1-2 service already running."; exit 0; }

mkdir -p "$USER_UNIT_DIR"
chmod +x "$SCRIPT_DIR/dummy_logger_ok.sh" 2>/dev/null || true

cat > "$UNIT_FILE" << EOF
[Unit]
Description=Lab logger OK - success messages for journalctl practice
After=default.target

[Service]
Type=simple
ExecStart=$LAB_ROOT/scripts/dummy_logger_ok.sh
Restart=no

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload 2>/dev/null || { echo "Warning: systemctl --user failed. Ensure you have a user D-Bus session."; exit 1; }
systemctl --user start lab-logger-ok.service 2>/dev/null || true
echo "lab-logger-ok" > "$TRACKING"
echo "Clue 1-2: lab-logger-ok service started. Run journalctl --user -u lab-logger-ok.service"
echo "Done."
