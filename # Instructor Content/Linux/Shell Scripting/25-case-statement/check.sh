#!/bin/bash

# Real scenario: service control - status / restart / logs

read -p "Action (status/restart/logs/tail): " ACTION

case "$ACTION" in
  status)
    echo "[$(date '+%H:%M:%S')] Service status:"
    echo "  nginx: running, pid 1234"
    echo "  postgres: running, 12 connections"
    echo "  app: running, pid 5678"
    ;;
  restart)
    echo "[$(date '+%H:%M:%S')] Restarting app..."
    echo "  Stopping app..."
    echo "  Starting app..."
    echo "[$(date '+%H:%M:%S')] App restarted."
    ;;
  logs)
    echo "[$(date '+%H:%M:%S')] Last 10 lines of /var/log/app/app.log:"
    echo "  [simulated] 2025-01-29 10:00:00 INFO  Request /health 200"
    echo "  [simulated] 2025-01-29 10:00:01 INFO  Request /api 200"
    ;;
  tail)
    echo "[$(date '+%H:%M:%S')] Tailing /var/log/app/app.log (Ctrl+C to stop)..."
    echo "  [simulated tail -f output]"
    ;;
  *)
    echo "Unknown action. Use status, restart, logs, or tail."
    ;;
esac
