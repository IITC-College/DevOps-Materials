#!/bin/bash
# BEFORE Level 2, Clue 1: Start lab-logger-fail for journalctl -xe practice.
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
USER_UNIT_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"
UNIT_FILE="$USER_UNIT_DIR/lab-logger-fail.service"
TRACKING="$LAB_ROOT/.lab_2_1_service"

[ -f "$TRACKING" ] && { echo "Clue 2-1 already set up (failure in logs)."; exit 0; }

mkdir -p "$USER_UNIT_DIR"
chmod +x "$SCRIPT_DIR/dummy_logger_fail.sh" 2>/dev/null || true

cat > "$UNIT_FILE" << EOF
[Unit]
Description=Lab logger FAIL - for journalctl -xe practice
After=default.target

[Service]
Type=oneshot
ExecStart=$LAB_ROOT/scripts/dummy_logger_fail.sh
RemainAfterExit=no

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload 2>/dev/null || { echo "Warning: systemctl --user failed. Ensure you have a user D-Bus session."; exit 1; }
systemctl --user start lab-logger-fail.service 2>/dev/null || true
echo "lab-logger-fail" > "$TRACKING"
echo "Clue 2-1: lab-logger-fail was started (it fails). Use journalctl --user -xe to find the error."
echo "Done."
