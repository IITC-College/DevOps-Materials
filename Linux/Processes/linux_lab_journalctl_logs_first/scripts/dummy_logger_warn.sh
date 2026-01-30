#!/bin/bash
# Lab dummy logger: logs warnings so students can see priority levels.
# Stderr goes to journald when run as a systemd service.
echo "[INFO] lab-logger-warn started"
echo "[WARN] lab-logger-warn: simulated warning - disk usage high" >&2
while true; do
  echo "[WARN] lab-logger-warn heartbeat warning" >&2
  sleep 5
done
