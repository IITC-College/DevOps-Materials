#!/bin/bash

# FIXED: no spaces in VAR=value, quote $CONFIG, add fi

APP_NAME="myapp"
CONFIG="config.txt"

if [ -f "$CONFIG" ]; then
  echo "Deploying $APP_NAME..."
  echo "Deploy complete."
else
  echo "Error: config not found."
fi
