#!/bin/bash

# CI/CD Step 3: Test - depends on build artifact
# Exit 0 = tests passed. Exit 1 = abort pipeline.

STAGE="test"
LOG_PREFIX="[$(date '+%Y-%m-%d %H:%M:%S')] [$STAGE]"

echo "$LOG_PREFIX Starting tests..."

# Must have build artifact
CONFIG_FILE="${1:-config.txt}"
APP_NAME=$(grep APP_NAME "$CONFIG_FILE" 2>/dev/null | cut -d= -f2) || APP_NAME="app"
ARTIFACT="build/${APP_NAME}.tar.gz"

if [ ! -f "$ARTIFACT" ]; then
  echo "$LOG_PREFIX ERROR: Artifact not found: $ARTIFACT"
  echo "$LOG_PREFIX Run ci_build.sh first (or pipeline.sh)"
  exit 1
fi
echo "$LOG_PREFIX Artifact found: $ARTIFACT"

# Simulate test suite
echo "$LOG_PREFIX Running unit tests..."
echo "$LOG_PREFIX   test_api... PASS"
echo "$LOG_PREFIX   test_config... PASS"
echo "$LOG_PREFIX Running integration tests..."
echo "$LOG_PREFIX   test_db_connection... PASS"
echo "$LOG_PREFIX Running smoke tests..."
echo "$LOG_PREFIX   test_health_endpoint... PASS"

# Simulate one test that can fail (e.g. pass always for demo, or use env)
if [ "${TEST_FAIL:-0}" = "1" ]; then
  echo "$LOG_PREFIX ERROR: test_deploy_ready FAILED"
  exit 1
fi

echo "$LOG_PREFIX All tests passed. Ready for deploy."
exit 0
