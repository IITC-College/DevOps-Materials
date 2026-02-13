#!/bin/bash

# Real case: multiple conditions - config file AND env not empty

CONFIG="config.txt"
ENV="${1:-}"

if [ -z "$ENV" ]; then
  echo "Error: pass env as argument. Example: ./validate_before_deploy.sh prod"
elif [ ! -f "$CONFIG" ]; then
  echo "Error: $CONFIG not found."
else
  echo "Config OK. Env: $ENV. Ready to deploy."
fi
