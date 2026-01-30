#!/bin/bash
# BEFORE Level 2, Clue 1: Start dummy processes for this clue.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LAB_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PIDFILE="$LAB_ROOT/.lab_pids_2_1"

[ -f "$PIDFILE" ] && { echo "Clue 2-1 processes already running."; exit 0; }

for f in "$SCRIPT_DIR/dummy_cpu_eater.sh" "$SCRIPT_DIR/dummy_cpu_eater2.sh" "$SCRIPT_DIR/dummy_ram_eater.sh"; do
  chmod +x "$f" 2>/dev/null || true
done

: > "$PIDFILE"
"$SCRIPT_DIR/dummy_cpu_eater.sh" & echo $! >> "$PIDFILE"
"$SCRIPT_DIR/dummy_cpu_eater2.sh" & echo $! >> "$PIDFILE"
"$SCRIPT_DIR/dummy_ram_eater.sh" & echo $! >> "$PIDFILE"
echo "✓ Dummy processes started for Clue 2-1 (2 CPU + 1 RAM)."
