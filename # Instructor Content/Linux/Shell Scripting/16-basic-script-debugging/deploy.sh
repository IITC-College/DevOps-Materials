#!/bin/bash

# Layer: Basic debugging - echo to see what's happening
# Real case: deploy fails - why? Check vars and path

APP_NAME="myapp"
CONFIG="config.txt"

# Debug: uncomment to see values before condition
# echo "DEBUG: APP_NAME=$APP_NAME CONFIG=$CONFIG"

if [ -f "$CONFIG" ]; then
  echo "Deploying $APP_NAME..."
  echo "Deploy complete."
else
  echo "Error: $CONFIG not found."
  # Debug: where are we? what files exist?
  # echo "DEBUG: pwd=$(pwd)"
  # ls -l
fi
