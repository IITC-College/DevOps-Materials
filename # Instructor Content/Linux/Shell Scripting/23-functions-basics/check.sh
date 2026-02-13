#!/bin/bash

# Real scenario: check one service, reuse for many

check_service() {
  echo "  $1: $(date '+%H:%M:%S') - checking..."
  echo "  $1: OK"
}

echo "[$(date '+%H:%M:%S')] Health check..."
check_service nginx
check_service postgres
check_service redis
check_service app
echo "[$(date '+%H:%M:%S')] All OK."
