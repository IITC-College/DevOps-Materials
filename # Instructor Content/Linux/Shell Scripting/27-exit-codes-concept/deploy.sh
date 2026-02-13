#!/bin/bash

# Topic 27: Exit codes - deploy fails without config
# Caller (pipeline, human) checks $? to know success/failure

CONFIG="${1:-config.txt}"
LOG_PREFIX="[$(date '+%Y-%m-%d %H:%M:%S')] [deploy]"

echo "$LOG_PREFIX Deploy using config: $CONFIG"

# Step 1: Config must exist
if [ ! -f "$CONFIG" ]; then
  echo "$LOG_PREFIX ERROR: Config file not found: $CONFIG"
  echo "$LOG_PREFIX Cannot deploy without config. Create it and retry."
  exit 1
fi

# Step 2: Load and validate (simulated)
echo "$LOG_PREFIX Loading $CONFIG..."
if ! grep -q "APP_NAME" "$CONFIG" 2>/dev/null; then
  echo "$LOG_PREFIX ERROR: APP_NAME not set in config"
  exit 1
fi

# Step 3: Pre-deploy check - disk space (simulated)
echo "$LOG_PREFIX Checking disk space..."
echo "$LOG_PREFIX Disk: 45% used - OK"

# Step 4: Deploy
echo "$LOG_PREFIX Deploying application..."
echo "$LOG_PREFIX   Stopping old process..."
echo "$LOG_PREFIX   Copying artifacts..."
echo "$LOG_PREFIX   Starting new process..."
echo "$LOG_PREFIX   Waiting for health check..."

# Step 5: Post-deploy health check (simulated)
echo "$LOG_PREFIX Health check: HTTP 200 /health - OK"

echo "$LOG_PREFIX Deploy complete."
exit 0
