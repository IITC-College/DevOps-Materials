#!/bin/bash

# Topic 27: Pipeline runs script, checks $? to pass/fail
# Real scenario: CI job runs this; exit 0 = green, exit 1 = red

LOG_PREFIX="[$(date '+%Y-%m-%d %H:%M:%S')]"
echo "$LOG_PREFIX Running health check..."

./check.sh
CODE=$?

echo ""
echo "$LOG_PREFIX Exit code: $CODE"

if [ $CODE -eq 0 ]; then
  echo "$LOG_PREFIX Result: PASS - continue pipeline (e.g. deploy next)."
  exit 0
else
  echo "$LOG_PREFIX Result: FAIL - abort pipeline (e.g. notify, no deploy)."
  exit 1
fi
