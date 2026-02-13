#!/bin/bash

# Topic 28: Exit codes - every path returns 0 or 1
# Used standalone or by pipeline.sh / chain.sh

CONFIG="config.txt"
LOG_PREFIX="[$(date '+%Y-%m-%d %H:%M:%S')] [deploy]"

echo "$LOG_PREFIX Deploy..."

if [ ! -f "$CONFIG" ]; then
  echo "$LOG_PREFIX ERROR: $CONFIG not found. Create it: echo 'APP_NAME=myapp' > config.txt"
  exit 1
fi

echo "$LOG_PREFIX Config loaded."
echo "$LOG_PREFIX Deploying to /opt/app..."
echo "$LOG_PREFIX Health check..."
echo "$LOG_PREFIX Deploy complete."
exit 0
