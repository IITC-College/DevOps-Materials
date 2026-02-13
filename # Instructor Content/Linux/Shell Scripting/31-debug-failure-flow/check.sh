#!/bin/bash

# Real scenario: trace why health check failed

SERVICE="${1:-app}"
echo "DEBUG: SERVICE=$SERVICE"

if [ -z "$SERVICE" ]; then
  echo "Error: service required (e.g. nginx, app)."
  exit 1
fi

echo "[$(date '+%H:%M:%S')] Checking $SERVICE..."
echo "  $SERVICE: OK"
exit 0
