#!/bin/bash
# BEFORE Level 2, Clue 3: Start lab-logger-warn and lab-logger-fail for full scenario.
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
USER_UNIT_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"
TRACKING="$LAB_ROOT/.lab_2_3_service"

[ -f "$TRACKING" ] && { echo "Clue 2-3 services already set up."; exit 0; }

mkdir -p "$USER_UNIT_DIR"
chmod +x "$SCRIPT_DIR/dummy_logger_warn.sh" "$SCRIPT_DIR/dummy_logger_fail.sh" 2>/dev/null || true

# Install and start lab-logger-warn (runs in background)
cat > "$USER_UNIT_DIR/lab-logger-warn.service" << EOF
[Unit]
Description=Lab logger WARN - warnings for journalctl practice
After=default.target

[Service]
Type=simple
ExecStart=$LAB_ROOT/scripts/dummy_logger_warn.sh
Restart=no

[Install]
WantedBy=default.target
EOF

# Install and start lab-logger-fail (fails)
cat > "$USER_UNIT_DIR/lab-logger-fail.service" << EOF
[Unit]
Description=Lab logger FAIL - for full problem description practice
After=default.target

[Service]
Type=oneshot
ExecStart=$LAB_ROOT/scripts/dummy_logger_fail.sh
RemainAfterExit=no

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload 2>/dev/null || { echo "Warning: systemctl --user failed. Ensure you have a user D-Bus session."; exit 1; }
systemctl --user start lab-logger-warn.service 2>/dev/null || true
systemctl --user start lab-logger-fail.service 2>/dev/null || true   # fails on purpose
echo "lab-logger-warn lab-logger-fail" > "$TRACKING"
echo "Clue 2-3: lab-logger-warn and lab-logger-fail were started (fail will have failed). Use journalctl --user to trace and describe."
echo "Done."
