#!/bin/bash

# Layer: User input - read, read -p

read -p "Enter app name: " APP_NAME
read -p "Enter version: " VERSION

echo "Deploying $APP_NAME v$VERSION..."
echo "Deploy complete."
