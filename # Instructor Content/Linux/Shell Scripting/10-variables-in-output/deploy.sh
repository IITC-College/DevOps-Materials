#!/bin/bash

# Layer: Variables in output - text + $VAR together

APP_NAME="myapp"
VERSION="2.1"
ENV="production"

echo "Deploying $APP_NAME v$VERSION to $ENV..."
echo "Deploy complete at $(date +%H:%M:%S)."
