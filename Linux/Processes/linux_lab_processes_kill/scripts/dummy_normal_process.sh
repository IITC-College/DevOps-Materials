#!/bin/bash
# Dummy process that responds to SIGTERM and exits gracefully.
trap 'echo "Received SIGTERM, shutting down..."; exit 0' TERM
while true; do sleep 1; done
