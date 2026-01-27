#!/bin/bash

# Web Application Deployment Script
# This script deploys the web application

echo "Deploying web application..."

# Check if config file exists
if [ ! -f "config.json" ]; then
    echo "Error: config.json not found"
    exit 1
fi

# Verify ownership
echo "Checking file ownership..."
ls -l config.json

# The web server needs to read this config file
# It should be owned by www-data:www-data

echo "Deployment complete!"
