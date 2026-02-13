#!/bin/bash

# CI/CD Pipeline: validate -> build -> test -> deploy
# Each step depends on previous. Exit 1 at any step stops the pipeline.

set -e
PIPELINE_START=$(date '+%Y-%m-%d %H:%M:%S')
CONFIG="${1:-config.txt}"
ENV="${2:-staging}"

echo "=============================================="
echo "  CI/CD Pipeline started at $PIPELINE_START"
echo "  Config: $CONFIG  Env: $ENV"
echo "=============================================="
echo ""

run_step() {
  local name="$1"
  local cmd="$2"
  echo "[$(date '+%H:%M:%S')] >>> Running step: $name"
  if $cmd; then
    echo "[$(date '+%H:%M:%S')] <<< $name passed"
    echo ""
    return 0
  else
    echo "[$(date '+%H:%M:%S')] <<< $name FAILED - pipeline aborted"
    echo ""
    return 1
  fi
}

# Step 1: Validate
run_step "validate" "./ci_validate.sh $CONFIG" || exit 1

# Step 2: Build
run_step "build" "./ci_build.sh $CONFIG" || exit 1

# Step 3: Test
run_step "test" "./ci_test.sh $CONFIG" || exit 1

# Step 4: Deploy
run_step "deploy" "./ci_deploy.sh $CONFIG $ENV" || exit 1

echo "=============================================="
echo "  Pipeline SUCCESS - finished at $(date '+%Y-%m-%d %H:%M:%S')"
echo "=============================================="
exit 0
