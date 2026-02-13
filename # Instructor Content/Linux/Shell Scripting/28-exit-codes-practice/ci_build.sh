#!/bin/bash

# CI/CD Step 2: Build - depends on validate passing
# Exit 0 = build artifact ready. Exit 1 = abort pipeline.

STAGE="build"
LOG_PREFIX="[$(date '+%Y-%m-%d %H:%M:%S')] [$STAGE]"

echo "$LOG_PREFIX Starting build..."

# Must have passed validate first
if [ ! -f .validated ]; then
  echo "$LOG_PREFIX ERROR: Run ci_validate.sh first (or pipeline.sh)"
  exit 1
fi

# Load config
CONFIG_FILE="${1:-config.txt}"
if [ ! -f "$CONFIG_FILE" ]; then
  echo "$LOG_PREFIX ERROR: Config not found: $CONFIG_FILE"
  exit 1
fi
APP_NAME=$(grep APP_NAME "$CONFIG_FILE" 2>/dev/null | cut -d= -f2) || APP_NAME="app"
echo "$LOG_PREFIX Building $APP_NAME..."

# Simulate build steps
echo "$LOG_PREFIX Installing dependencies..."
echo "$LOG_PREFIX Compiling..."
echo "$LOG_PREFIX Packaging..."

# Create build artifact (real pipeline would have real artifact)
BUILD_DIR="build"
ARTIFACT="$BUILD_DIR/${APP_NAME}.tar.gz"
mkdir -p "$BUILD_DIR"
echo "Built at $(date)" > "$BUILD_DIR/build.info"
echo "Version: 1.0.0" >> "$BUILD_DIR/build.info"
echo "simulated-artifact-$(date +%s)" > "$ARTIFACT"

if [ ! -f "$ARTIFACT" ]; then
  echo "$LOG_PREFIX ERROR: Build failed - no artifact: $ARTIFACT"
  exit 1
fi

echo "$LOG_PREFIX Artifact: $ARTIFACT"
echo "$LOG_PREFIX Build passed. Ready for test."
exit 0
