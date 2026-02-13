#!/bin/bash

# Layer: Conditional logic - if / then / else / fi
# Real case: block deploy if app name empty

read -p "Enter app name: " APP_NAME

if [ -z "$APP_NAME" ]; then
  echo "Error: app name cannot be empty. Aborting deploy."
else
  echo "Deploying $APP_NAME..."
  echo "Deploy complete."
fi
