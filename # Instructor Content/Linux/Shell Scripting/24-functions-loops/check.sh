#!/bin/bash

# Real scenario: loop over hosts, same check function

check_host() {
  echo "  $1: ping OK, SSH OK, disk $(echo "45%")"
}

HOSTS="web-01 web-02 db-01"
echo "[$(date '+%H:%M:%S')] Checking hosts..."
for HOST in $HOSTS; do
  check_host "$HOST"
done
echo "[$(date '+%H:%M:%S')] All hosts OK."
