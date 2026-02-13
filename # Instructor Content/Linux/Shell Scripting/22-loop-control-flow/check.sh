#!/bin/bash

# Real scenario: stop on first failing service (fail-fast)

SERVICES="nginx postgres redis app"
echo "[$(date '+%H:%M:%S')] Health check (fail-fast)..."
for SVC in $SERVICES; do
  echo "  Checking $SVC..."
  if [ "$SVC" = "postgres" ]; then
    echo "  FAIL: $SVC not responding on 5432"
    echo "[$(date '+%H:%M:%S')] Aborting - fix $SVC first."
    break
  fi
  echo "  $SVC: OK"
done
echo "Done."
