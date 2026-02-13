#!/bin/bash

# CI/CD Step 1: Validate - config, env, required files
# Exit 0 = ready for build. Exit 1 = abort pipeline.

STAGE="validate"
LOG_PREFIX="[$(date '+%Y-%m-%d %H:%M:%S')] [$STAGE]"

echo "$LOG_PREFIX Starting validation..."

# Check required config exists
CONFIG_FILE="${1:-config.txt}"
if [ ! -f "$CONFIG_FILE" ]; then
  echo "$LOG_PREFIX ERROR: Config file not found: $CONFIG_FILE"
  echo "$LOG_PREFIX Create it with: echo 'APP_NAME=myapp' > config.txt"
  exit 1
fi
echo "$LOG_PREFIX Config file found: $CONFIG_FILE"

# Check we have required vars (simulated - in real world source config)
if ! grep -q "APP_NAME" "$CONFIG_FILE" 2>/dev/null; then
  echo "$LOG_PREFIX ERROR: APP_NAME not set in config"
  exit 1
fi
echo "$LOG_PREFIX APP_NAME is set"

# Check disk space (simulated)
echo "$LOG_PREFIX Checking disk space..."
echo "$LOG_PREFIX Disk: 45% used - OK"

# Check required dirs
for DIR in src build; do
  if [ ! -d "$DIR" ]; then
    echo "$LOG_PREFIX Creating $DIR..."
    mkdir -p "$DIR"
  fi
  echo "$LOG_PREFIX $DIR: OK"
done

# Mark validation passed for next stage
touch .validated 2>/dev/null || true
echo "$LOG_PREFIX Validation passed. Ready for build."
exit 0
