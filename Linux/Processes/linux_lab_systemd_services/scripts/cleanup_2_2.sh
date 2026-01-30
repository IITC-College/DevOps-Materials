#!/bin/bash
# Cleanup for Level 2 Clue 2: stop and remove lab-demo user service.
USER_UNIT_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"
UNIT_FILE="$USER_UNIT_DIR/lab-demo.service"

systemctl --user stop lab-demo 2>/dev/null || true
rm -f "$UNIT_FILE"
systemctl --user daemon-reload 2>/dev/null || true
echo "Lab demo service removed (cleanup 2-2)."
