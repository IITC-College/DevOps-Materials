#!/bin/bash

# Topic 21: Loops - real scenario: deploy multiple app tiers

APP_TIERS="frontend api worker"
BUILD_DIR="/opt/build"
LOG_FILE="deploy.log"

echo "[$(date '+%H:%M:%S')] Deploying tiers from $BUILD_DIR..."
for TIER in $APP_TIERS; do
  echo "  [$(date '+%H:%M:%S')] Stopping $TIER..."
  echo "  [$(date '+%H:%M:%S')] Copying artifacts for $TIER..."
  echo "  [$(date '+%H:%M:%S')] Starting $TIER..."
  echo "  $TIER: deployed"
done
echo "[$(date '+%H:%M:%S')] All tiers deployed. Restarting load balancer..."
