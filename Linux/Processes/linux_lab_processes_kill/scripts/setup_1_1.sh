#!/bin/bash
# BEFORE Level 1, Clue 1: Start a simple sleep process for this clue.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PIDFILE="$LAB_ROOT/.lab_pids_1_1"

[ -f "$PIDFILE" ] && { echo "Clue 1-1 process already running."; exit 0; }

: > "$PIDFILE"
sleep 9999 & echo $! >> "$PIDFILE"
echo "✓ Dummy process (sleep) started for Clue 1-1."
