#!/bin/bash

# Simple chain: check -> deploy (each step must pass)
# For full CI/CD (validate->build->test->deploy) use pipeline.sh

LOG_PREFIX="[$(date '+%Y-%m-%d %H:%M:%S')] [chain]"

echo "$LOG_PREFIX Pipeline: check -> deploy"
echo ""

echo "$LOG_PREFIX Step 1: Health check..."
./check.sh
if [ $? -ne 0 ]; then
  echo "$LOG_PREFIX Step 1 FAILED. Aborting."
  exit 1
fi
echo ""

echo "$LOG_PREFIX Step 2: Deploy..."
./deploy.sh
if [ $? -ne 0 ]; then
  echo "$LOG_PREFIX Step 2 FAILED. Aborting."
  exit 1
fi
echo ""

echo "$LOG_PREFIX Chain complete. All steps passed."
exit 0
