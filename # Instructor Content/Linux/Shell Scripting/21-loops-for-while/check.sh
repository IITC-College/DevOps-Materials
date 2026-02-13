#!/bin/bash

# Real scenario: health check across services (simulated status)

SERVICES="nginx postgres redis app"
echo "[$(date '+%H:%M:%S')] Health check..."
for SVC in $SERVICES; do
  case "$SVC" in
    nginx)   echo "  $SVC: listening on 80/443" ;;
    postgres) echo "  $SVC: connected, 12 connections" ;;
    redis)   echo "  $SVC: ping PONG, keys=42" ;;
    app)     echo "  $SVC: HTTP 200 /health" ;;
  esac
done
echo "[$(date '+%H:%M:%S')] All services OK."
