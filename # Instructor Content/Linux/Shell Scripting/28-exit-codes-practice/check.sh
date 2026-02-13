#!/bin/bash

# Real scenario: explicit exit 0/1 for every branch

read -p "Service (nginx/postgres/app): " SERVICE

if [ -z "$SERVICE" ]; then
  echo "Error: service required."
  exit 1
fi

case "$SERVICE" in
  nginx)
    echo "nginx: listening 80/443 - OK"
    exit 0
    ;;
  postgres)
    echo "postgres: 12 connections - OK"
    exit 0
    ;;
  app)
    echo "app: HTTP 200 /health - OK"
    exit 0
    ;;
  *)
    echo "Unknown service."
    exit 1
    ;;
esac
