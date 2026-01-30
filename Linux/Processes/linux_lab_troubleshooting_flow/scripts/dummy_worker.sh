#!/bin/bash
# Lab dummy "lab-helper" process - simple worker that stays running.
# Used when we want the process to be running; for "not running" scenarios we do not start it.
LAB_ROOT="${LAB_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
LOG_DIR="$LAB_ROOT/data/logs"
mkdir -p "$LOG_DIR"
while true; do
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] lab-helper running" >> "$LOG_DIR/lab_helper.log" 2>/dev/null || true
  sleep 5
done
