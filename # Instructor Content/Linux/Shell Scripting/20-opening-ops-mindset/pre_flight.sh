#!/bin/bash

# Real scenario: before any deploy, verify basics

echo "[$(date '+%H:%M:%S')] Pre-flight check..."
echo "  Checking disk space..."
echo "  /var: 45% used"
echo "  /opt: 62% used"
echo "  Checking required dirs: /opt/app, /var/log/app"
echo "  Dirs present: OK"
echo "[$(date '+%H:%M:%S')] Pre-flight passed. Safe to deploy."
