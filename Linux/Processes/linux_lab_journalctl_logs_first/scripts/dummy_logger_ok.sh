#!/bin/bash
# Lab dummy logger: logs success messages so students can filter by service.
# Stdout goes to journald when run as a systemd service.
echo "[INFO] lab-logger-ok started successfully"
while true; do
  echo "[INFO] lab-logger-ok heartbeat OK"
  sleep 5
done
