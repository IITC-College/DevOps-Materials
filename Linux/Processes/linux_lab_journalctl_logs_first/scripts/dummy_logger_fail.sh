#!/bin/bash
# Lab dummy logger: logs an error and exits so students can find failure in logs.
# Stderr goes to journald when run as a systemd service.
echo "[INFO] lab-logger-fail starting..."
echo "[ERROR] lab-logger-fail: simulated failure - config file not found" >&2
exit 1
