#!/bin/bash
# AFTER Level 1, Clue 1: Stop and remove lab-logger-ok service.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
USER_UNIT_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"
UNIT_FILE="$USER_UNIT_DIR/lab-logger-ok.service"
TRACKING="$LAB_ROOT/.lab_1_1_service"

[ ! -f "$TRACKING" ] && { echo "No Clue 1-1 service to clean up."; exit 0; }

systemctl --user stop lab-logger-ok.service 2>/dev/null || true
rm -f "$UNIT_FILE"
systemctl --user daemon-reload 2>/dev/null || true
rm -f "$TRACKING"
echo "Clue 1-1 cleanup complete."
echo "Done."
