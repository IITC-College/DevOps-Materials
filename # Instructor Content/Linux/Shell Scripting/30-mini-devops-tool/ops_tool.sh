#!/bin/bash

# Topic 30: Mini DevOps Tool - longer, real-world style
# Loops, functions, case, input, exit codes, multiple steps per action

LOG_PREFIX="[$(date '+%Y-%m-%d %H:%M:%S')]"

check_services() {
  echo "$LOG_PREFIX Health check..."
  for SVC in nginx postgres redis app; do
    echo "  Checking $SVC..."
    case "$SVC" in
      nginx)   echo "    nginx: listening 80/443 - OK" ;;
      postgres) echo "    postgres: 12 connections - OK" ;;
      redis)   echo "    redis: ping PONG - OK" ;;
      app)     echo "    app: HTTP 200 /health - OK" ;;
    esac
  done
  echo "$LOG_PREFIX All services OK."
  return 0
}

deploy_app() {
  echo "$LOG_PREFIX Deploy started..."
  echo "  Pre-check: disk space..."
  echo "  Disk: 45% - OK"
  echo "  Pulling image from registry..."
  echo "  Stopping old containers..."
  echo "  Starting new containers..."
  echo "  Waiting for health (max 30s)..."
  echo "  Health: OK"
  echo "$LOG_PREFIX Deploy complete."
  return 0
}

show_status() {
  echo "$LOG_PREFIX System status:"
  echo "  Hostname: $(hostname)"
  echo "  Uptime: $(uptime -p 2>/dev/null || uptime)"
  echo "  Disk: $(df -h . 2>/dev/null | tail -1)"
  echo "  Memory: $(free -h 2>/dev/null | grep Mem || echo 'N/A')"
  echo "  Date: $(date)"
  return 0
}

backup_now() {
  BACKUP_DIR="/backup/$(date +%Y-%m-%d-%H%M)"
  echo "$LOG_PREFIX Backup to $BACKUP_DIR..."
  echo "  Backing up /var/log/app..."
  echo "  Backing up /etc/app..."
  echo "  Backing up db dump..."
  echo "$LOG_PREFIX Backup done."
  return 0
}

# Pipeline: validate -> build -> test -> deploy (simulated in one function)
run_pipeline() {
  echo "$LOG_PREFIX === Pipeline (validate -> build -> test -> deploy) ==="
  echo "  [validate] Config OK, disk OK"
  echo "  [build] Artifact built"
  echo "  [test] Unit + integration passed"
  echo "  [deploy] Deployed to staging"
  echo "$LOG_PREFIX Pipeline complete."
  return 0
}

echo "=== Mini DevOps Tool ==="
echo "  check | deploy | status | backup | pipeline"
echo ""
read -p "Action: " ACTION

case "$ACTION" in
  check)
    check_services
    exit 0
    ;;
  deploy)
    deploy_app
    exit 0
    ;;
  status)
    show_status
    exit 0
    ;;
  backup)
    backup_now
    exit 0
    ;;
  pipeline)
    run_pipeline
    exit 0
    ;;
  *)
    echo "Error: use check, deploy, status, backup, or pipeline."
    exit 1
    ;;
esac
