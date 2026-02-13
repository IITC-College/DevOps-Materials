#!/bin/bash

# Layer: Common conditions - [ -f ] file exists
# Real case: do not deploy without config file

CONFIG_FILE="config.txt"

if [ -f "$CONFIG_FILE" ]; then
  echo "Config found. Deploying..."
  echo "Deploy complete."
else
  echo "Error: $CONFIG_FILE not found. Create config first."
fi
