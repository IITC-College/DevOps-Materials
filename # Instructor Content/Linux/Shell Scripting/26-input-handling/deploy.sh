#!/bin/bash

# Topic 26: Input handling - real scenario: validate before deploy

read -p "App name: " APP_NAME
read -p "Environment (prod/staging): " ENV
read -p "Version tag (e.g. v1.2.3): " VERSION

if [ -z "$APP_NAME" ]; then
  echo "Error: app name required."
  exit 1
fi
if [ "$ENV" != "prod" ] && [ "$ENV" != "staging" ]; then
  echo "Error: use prod or staging."
  exit 1
fi
if [ -z "$VERSION" ]; then
  echo "Error: version tag required."
  exit 1
fi

echo "[$(date '+%H:%M:%S')] Deploying $APP_NAME $VERSION to $ENV..."
echo "  Pulling image: registry.company.com/$APP_NAME:$VERSION"
echo "  Rolling update..."
echo "[$(date '+%H:%M:%S')] Deploy complete."
