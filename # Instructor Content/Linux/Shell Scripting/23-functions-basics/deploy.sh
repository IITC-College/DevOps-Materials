#!/bin/bash

# Topic 23: Functions - real scenario: reusable deploy steps

deploy_tier() {
  echo "  [$(date '+%H:%M:%S')] Stopping $1..."
  echo "  [$(date '+%H:%M:%S')] Deploying $1 from /opt/releases/$1..."
  echo "  [$(date '+%H:%M:%S')] Starting $1..."
  echo "  $1: deployed"
}

echo "[$(date '+%H:%M:%S')] Deploy started."
deploy_tier frontend
deploy_tier api
deploy_tier worker
echo "[$(date '+%H:%M:%S')] Deploy complete."
