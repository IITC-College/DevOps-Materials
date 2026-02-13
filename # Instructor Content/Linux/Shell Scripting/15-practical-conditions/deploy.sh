#!/bin/bash

# Layer: Practical conditions - create dir only if missing
# Real case: deploy dir must exist before copying artifacts

DEPLOY_DIR="deploy"

if [ ! -d "$DEPLOY_DIR" ]; then
  mkdir "$DEPLOY_DIR"
  echo "Created $DEPLOY_DIR"
fi

echo "Deploying to $DEPLOY_DIR..."
echo "Deploy complete."
