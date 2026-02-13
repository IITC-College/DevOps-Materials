#!/bin/bash

# BROKEN - find and fix (real check script mistakes)

read -p "Service: " SERVICE

if [ -z $SERVICE ]
  echo "Error: empty input"
else
  echo "Checking $SERVICE..."
  echo "Status: OK"
fi
