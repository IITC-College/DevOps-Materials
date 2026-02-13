#!/bin/bash

# Topic 24: Functions + Loops - real scenario: deploy each tier with same steps

deploy_tier() {
  echo "  [$(date '+%H:%M:%S')] $1: stopping old, copying build, starting new"
  echo "  $1: deployed"
}

TIERS="frontend api worker cache"
echo "[$(date '+%H:%M:%S')] Deploying tiers..."
for TIER in $TIERS; do
  deploy_tier "$TIER"
done
echo "[$(date '+%H:%M:%S')] All tiers up. Running smoke tests..."
