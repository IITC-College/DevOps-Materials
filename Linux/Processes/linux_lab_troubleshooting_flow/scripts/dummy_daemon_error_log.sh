#!/bin/bash
# Daemon that runs but writes ERROR to stdout (journal) – "running but app not responding" scenario.
# Students see service active but logs show error; next action = restart or investigate.
echo "lab-troubleshoot: started"
echo "ERROR: Application not responding – connection refused to backend" >&2
while true; do
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] WARN: health check failing" >&2
  sleep 3
done
