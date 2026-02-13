#!/bin/bash

# BROKEN - find and fix (real deploy script mistakes)

APP_NAME = "myapp"
CONFIG="config.txt"

if [ -f $CONFIG ]; then
  echo "Deploying $APP_NAME..."
  echo "Deploy complete."
else
  echo "Error: config not found."
