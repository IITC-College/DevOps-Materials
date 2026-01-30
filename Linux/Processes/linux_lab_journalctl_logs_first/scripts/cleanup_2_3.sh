#!/bin/bash
# AFTER Level 2, Clue 3: Remove lab-logger-warn and lab-logger-fail services.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
USER_UNIT_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"
TRACKING="$LAB_ROOT/.lab_2_3_service"

[ ! -f "$TRACKING" ] && { echo "No Clue 2-3 services to clean up."; exit 0; }

systemctl --user stop lab-logger-warn.service 2>/dev/null || true
systemctl --user stop lab-logger-fail.service 2>/dev/null || true
rm -f "$USER_UNIT_DIR/lab-logger-warn.service" "$USER_UNIT_DIR/lab-logger-fail.service"
systemctl --user daemon-reload 2>/dev/null || true
rm -f "$TRACKING"
echo "Clue 2-3 cleanup complete."
echo "Done."
