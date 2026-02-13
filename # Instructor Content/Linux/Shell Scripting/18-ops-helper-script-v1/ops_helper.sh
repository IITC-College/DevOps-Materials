#!/bin/bash

# Ops Helper Script (v1) - clear and useful
# Uses: read, if, echo, variables
# Final layer: one script that ties it all together

echo "=== Ops Helper ==="
echo ""
read -p "Action (deploy/check/backup): " ACTION

if [ -z "$ACTION" ]; then
  echo "Error: action cannot be empty."
elif [ "$ACTION" = "deploy" ]; then
  echo "Deploying..."
  echo "App deployed."
elif [ "$ACTION" = "check" ]; then
  echo "Checking services..."
  echo "Status: OK"
elif [ "$ACTION" = "backup" ]; then
  echo "Backing up..."
  echo "Backup finished."
else
  echo "Unknown action. Use deploy, check, or backup."
fi

echo ""
echo "Done."
