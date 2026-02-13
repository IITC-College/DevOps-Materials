#!/bin/bash

# FIXED: quote $SERVICE, add then after condition

read -p "Service: " SERVICE

if [ -z "$SERVICE" ]; then
  echo "Error: empty input"
else
  echo "Checking $SERVICE..."
  echo "Status: OK"
fi
