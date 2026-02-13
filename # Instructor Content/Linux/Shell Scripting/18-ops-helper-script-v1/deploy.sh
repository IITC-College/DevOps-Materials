#!/bin/bash

# Ops Helper style: read, validate, act

read -p "App name: " APP_NAME
read -p "Environment (prod/staging): " ENV

if [ -z "$APP_NAME" ]; then
  echo "Error: app name required."
elif [ "$ENV" != "prod" ] && [ "$ENV" != "staging" ]; then
  echo "Error: use prod or staging."
else
  echo "Deploying $APP_NAME to $ENV..."
  echo "Deploy complete."
fi
