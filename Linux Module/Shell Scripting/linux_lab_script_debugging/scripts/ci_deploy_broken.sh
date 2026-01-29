#!/bin/bash
# BROKEN - find and fix: missing "then" after if

CONFIG="../data/configs/build_config.txt"

if [ -f "$CONFIG" ]
  echo "Deploying..."
  echo "Deploy complete."
else
  echo "Config not found."
fi
