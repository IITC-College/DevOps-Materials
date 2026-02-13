#!/bin/bash

# Topic 27: Exit codes - health check returns 0=OK, 1=fail
# Used by monitoring, CI, or other scripts that depend on $?

LOG_DIR="${1:-logs}"
LOG_PREFIX="[$(date '+%Y-%m-%d %H:%M:%S')] [check]"

echo "$LOG_PREFIX Health check (log dir: $LOG_DIR)..."

# Check 1: Log dir exists (app started and writing logs)
if [ ! -d "$LOG_DIR" ]; then
  echo "$LOG_PREFIX ERROR: Log directory missing: $LOG_DIR"
  echo "$LOG_PREFIX App may not have started. Check startup logs."
  exit 1
fi
echo "$LOG_PREFIX Log dir: OK"

# Check 2: Required services (simulated)
echo "$LOG_PREFIX Checking nginx..."
echo "$LOG_PREFIX   nginx: listening 80/443 - OK"
echo "$LOG_PREFIX Checking postgres..."
echo "$LOG_PREFIX   postgres: 12 connections - OK"
echo "$LOG_PREFIX Checking app..."
echo "$LOG_PREFIX   app: HTTP 200 /health - OK"

echo "$LOG_PREFIX All checks passed."
exit 0
