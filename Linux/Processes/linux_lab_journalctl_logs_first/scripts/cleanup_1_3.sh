#!/bin/bash
# AFTER Level 1, Clue 3: Remove lab-logger-fail service (it already exited).
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
USER_UNIT_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"
UNIT_FILE="$USER_UNIT_DIR/lab-logger-fail.service"
TRACKING="$LAB_ROOT/.lab_1_3_service"

[ ! -f "$TRACKING" ] && { echo "No Clue 1-3 service to clean up."; exit 0; }

systemctl --user stop lab-logger-fail.service 2>/dev/null || true
rm -f "$UNIT_FILE"
systemctl --user daemon-reload 2>/dev/null || true
rm -f "$TRACKING"
echo "Clue 1-3 cleanup complete."
echo "Done."
