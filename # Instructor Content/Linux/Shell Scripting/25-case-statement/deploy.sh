#!/bin/bash

# Topic 25: case - real scenario: different deploy per environment

read -p "Environment (prod/staging/dev): " ENV

case "$ENV" in
  prod)
    echo "[$(date '+%H:%M:%S')] PRODUCTION deploy - double-check..."
    echo "  Target: https://app.company.com"
    echo "  Rolling deploy: 3 nodes"
    echo "[$(date '+%H:%M:%S')] Deploy complete."
    ;;
  staging)
    echo "[$(date '+%H:%M:%S')] Staging deploy..."
    echo "  Target: https://staging.app.company.com"
    echo "  Single node"
    echo "[$(date '+%H:%M:%S')] Deploy complete."
    ;;
  dev)
    echo "[$(date '+%H:%M:%S')] Dev deploy..."
    echo "  Target: http://localhost:8080"
    echo "[$(date '+%H:%M:%S')] Deploy complete."
    ;;
  *)
    echo "Error: use prod, staging, or dev."
    ;;
esac
