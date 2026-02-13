#!/bin/bash

# Real case: different message for prod vs staging

read -p "Deploy to (prod/staging): " ENV

if [ "$ENV" = "prod" ]; then
  echo "Deploying to PRODUCTION..."
  echo "App deployed to prod."
elif [ "$ENV" = "staging" ]; then
  echo "Deploying to staging..."
  echo "App deployed to staging."
else
  echo "Error: use prod or staging."
fi
