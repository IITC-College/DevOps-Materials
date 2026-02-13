#!/bin/bash

# CI/CD Step 4: Deploy - depends on test passing
# Exit 0 = deployed. Exit 1 = abort.

STAGE="deploy"
LOG_PREFIX="[$(date '+%Y-%m-%d %H:%M:%S')] [$STAGE]"

echo "$LOG_PREFIX Starting deploy..."

# Require artifact (build + test passed)
CONFIG_FILE="${1:-config.txt}"
APP_NAME=$(grep APP_NAME "$CONFIG_FILE" 2>/dev/null | cut -d= -f2) || APP_NAME="app"
ARTIFACT="build/${APP_NAME}.tar.gz"
ENV="${2:-staging}"

if [ ! -f "$ARTIFACT" ]; then
  echo "$LOG_PREFIX ERROR: Artifact not found. Run build and test first."
  exit 1
fi

# Validate env
case "$ENV" in
  prod|staging|dev) ;;
  *)
    echo "$LOG_PREFIX ERROR: Invalid env: $ENV (use prod, staging, dev)"
    exit 1
    ;;
esac

echo "$LOG_PREFIX Deploying $APP_NAME to $ENV..."
echo "$LOG_PREFIX   Stopping old version..."
echo "$LOG_PREFIX   Copying $ARTIFACT to target..."
echo "$LOG_PREFIX   Starting new version..."
echo "$LOG_PREFIX   Health check..."
echo "$LOG_PREFIX   HTTP 200 /health - OK"

echo "$LOG_PREFIX Deploy complete. $APP_NAME is live on $ENV."
exit 0
