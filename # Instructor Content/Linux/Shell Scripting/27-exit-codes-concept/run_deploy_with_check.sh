#!/bin/bash

# Topic 27: One script depends on another via exit codes
# Simulates: run check first; if OK, run deploy. Stop on first failure.

LOG_PREFIX="[$(date '+%Y-%m-%d %H:%M:%S')] [runner]"
CONFIG="${1:-config.txt}"

echo "$LOG_PREFIX === Deploy runner (check then deploy) ==="
echo ""

# Step 1: Health check must pass before we deploy
echo "$LOG_PREFIX Step 1: Running health check..."
./check.sh
CHECK_EXIT=$?
if [ $CHECK_EXIT -ne 0 ]; then
  echo "$LOG_PREFIX Step 1 FAILED (exit $CHECK_EXIT). Aborting deploy."
  exit 1
fi
echo "$LOG_PREFIX Step 1 passed."
echo ""

# Step 2: Deploy
echo "$LOG_PREFIX Step 2: Running deploy..."
./deploy.sh "$CONFIG"
DEPLOY_EXIT=$?
if [ $DEPLOY_EXIT -ne 0 ]; then
  echo "$LOG_PREFIX Step 2 FAILED (exit $DEPLOY_EXIT)."
  exit 1
fi
echo "$LOG_PREFIX Step 2 passed."
echo ""

echo "$LOG_PREFIX === Runner complete. All steps passed. ==="
exit 0
