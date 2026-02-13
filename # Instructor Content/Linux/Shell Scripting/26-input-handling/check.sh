#!/bin/bash

# Real scenario: only allow known services

read -p "Service (nginx/postgres/redis/app): " SERVICE

case "$SERVICE" in
  nginx|postgres|redis|app)
    echo "[$(date '+%H:%M:%S')] Checking $SERVICE..."
    echo "  $SERVICE: OK"
    ;;
  *)
    echo "Error: use nginx, postgres, redis, or app."
    exit 1
    ;;
esac
