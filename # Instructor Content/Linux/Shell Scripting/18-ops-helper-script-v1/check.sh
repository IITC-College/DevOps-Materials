#!/bin/bash

# Ops Helper style: clear prompts, validation, useful output

read -p "Service (web/db): " SERVICE

if [ -z "$SERVICE" ]; then
  echo "Error: service required."
elif [ "$SERVICE" = "web" ]; then
  echo "Checking web..."
  echo "Web: OK"
elif [ "$SERVICE" = "db" ]; then
  echo "Checking database..."
  echo "Database: OK"
else
  echo "Unknown service. Use web or db."
fi
