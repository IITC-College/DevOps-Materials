#!/bin/bash

# Real scenario: retry API deploy until healthy or max 3

MAX=3
ATTEMPT=1
echo "[$(date '+%H:%M:%S')] Deploying API, waiting for health..."

while [ $ATTEMPT -le $MAX ]; do
  echo "  Attempt $ATTEMPT: calling /health..."
  if [ $ATTEMPT -eq 2 ]; then
    echo "  HTTP 200 OK - API healthy."
    break
  fi
  echo "  HTTP 503 - retrying in 5s..."
  ATTEMPT=$((ATTEMPT + 1))
done
echo "[$(date '+%H:%M:%S')] Deploy complete."
