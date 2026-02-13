#!/bin/bash

# Real case: different checks for web vs db

read -p "Service to check (web/db): " SERVICE

if [ "$SERVICE" = "web" ]; then
  echo "Checking web server..."
  echo "Web: OK"
elif [ "$SERVICE" = "db" ]; then
  echo "Checking database..."
  echo "Database: OK"
else
  echo "Unknown service. Use web or db."
fi
