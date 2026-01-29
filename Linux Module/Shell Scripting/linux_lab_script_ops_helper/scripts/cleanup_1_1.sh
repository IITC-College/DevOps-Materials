#!/bin/bash
# AFTER Level 1: Remove operational environment created by setup_1_1.sh.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
OPS_ENV="$LAB_ROOT/data/ops_env"
TRACKING="$LAB_ROOT/.lab_1_1_ops_env"

[ ! -f "$TRACKING" ] && { echo "No Clue 1-1 ops_env to clean up."; exit 0; }

rm -rf "$OPS_ENV"
rm -f "$TRACKING"
echo "Clue 1-1 cleanup complete (ops_env removed)."
echo "Done."
