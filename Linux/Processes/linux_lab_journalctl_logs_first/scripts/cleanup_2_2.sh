#!/bin/bash
# AFTER Level 2, Clue 2: Remove lab-logger-fail service.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
USER_UNIT_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"
UNIT_FILE="$USER_UNIT_DIR/lab-logger-fail.service"
TRACKING="$LAB_ROOT/.lab_2_2_service"

[ ! -f "$TRACKING" ] && { echo "No Clue 2-2 service to clean up."; exit 0; }

systemctl --user stop lab-logger-fail.service 2>/dev/null || true
rm -f "$UNIT_FILE"
systemctl --user daemon-reload 2>/dev/null || true
rm -f "$TRACKING"
echo "Clue 2-2 cleanup complete."
echo "Done."
