#!/bin/bash
# AFTER Level 2, Clue 2: Stop and remove lab-troubleshoot user service.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
USER_UNIT_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"
UNIT_FILE="$USER_UNIT_DIR/lab-troubleshoot.service"
TRACKING="$LAB_ROOT/.lab_2_2_service"

systemctl --user stop lab-troubleshoot 2>/dev/null || true
rm -f "$UNIT_FILE"
systemctl --user daemon-reload 2>/dev/null || true
rm -f "$TRACKING"
echo "✓ Cleanup complete for Clue 2-2."
