#!/bin/bash

# Layer: Input validation thinking
# Real case: deploy to env - what if user types nothing or typo?

read -p "Enter app name: " APP_NAME
read -p "Enter version: " VERSION
read -p "Environment (prod/staging): " ENV

echo "Deploying $APP_NAME v$VERSION to $ENV..."
echo "Deploy complete."
# No check: empty APP_NAME? wrong ENV? version format?
