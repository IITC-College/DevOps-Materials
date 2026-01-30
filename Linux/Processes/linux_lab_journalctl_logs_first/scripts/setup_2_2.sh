#!/bin/bash
# BEFORE Level 2, Clue 2: Start lab-logger-fail for time/priority filtering.
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
USER_UNIT_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"
UNIT_FILE="$USER_UNIT_DIR/lab-logger-fail.service"
TRACKING="$LAB_ROOT/.lab_2_2_service"

[ -f "$TRACKING" ] && { echo "Clue 2-2 already set up (failure in logs)."; exit 0; }

mkdir -p "$USER_UNIT_DIR"
chmod +x "$SCRIPT_DIR/dummy_logger_fail.sh" 2>/dev/null || true

cat > "$UNIT_FILE" << EOF
[Unit]
Description=Lab logger FAIL - for time/priority filtering practice
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
echo "Clue 2-2: lab-logger-fail was started. Use journalctl --user -u lab-logger-fail.service --since '10 minutes ago' and -p err"
echo "Done."
