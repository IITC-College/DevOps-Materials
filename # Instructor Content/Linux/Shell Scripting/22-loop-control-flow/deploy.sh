#!/bin/bash

# Topic 22: Loop control - real scenario: skip maintenance nodes

NODES="web-01 web-02 web-03 db-01"
MAINTENANCE="web-02"

echo "[$(date '+%H:%M:%S')] Deploying to cluster..."
for NODE in $NODES; do
  if [ "$NODE" = "$MAINTENANCE" ]; then
    echo "  Skipping $NODE (maintenance window)"
    continue
  fi
  echo "  Deploying to $NODE..."
  echo "  $NODE: deployed"
done
echo "[$(date '+%H:%M:%S')] Deploy complete."
