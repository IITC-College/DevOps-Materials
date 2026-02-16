#! /bin/bash

# Load database configuration
source .env.db

# Load network configuration
source .env.network

# Setup the environment
source setup.sh

# Check if the container already exists
if [ "$(docker ps -q -f name=$DB_CONTAINER_NAME)" ]; then
  echo "Container already exists."
  echo "To stop it run: docker kill $DB_CONTAINER_NAME"
  exit 1
fi

# Get absolute path for init script (works on Windows Git Bash)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INIT_SCRIPT_PATH="$SCRIPT_DIR/db-config/mongo-init.js"

# Prevent Git Bash from converting paths on Windows
export MSYS_NO_PATHCONV=1

# Start the container
docker run -d --rm --name $DB_CONTAINER_NAME \
    -e MONGO_INITDB_ROOT_USERNAME=$ROOT_USER \
    -e MONGO_INITDB_ROOT_PASSWORD=$ROOT_PASSWORD \
    -e KEY_VALUE_DB=$KEY_VALUE_DB \
    -e KEY_VALUE_USER=$KEY_VALUE_USER \
    -e KEY_VALUE_PASSWORD=$KEY_VALUE_PASSWORD \
    -p $LOCALHOST_PORT:$CONTAINER_PORT \
    --network $NETWORK_NAME \
    -v $VOLUME_NAME:$VOLUME_CONTAINER_PATH \
    -v "$INIT_SCRIPT_PATH":/docker-entrypoint-initdb.d/mongo-init.js:ro \
    $MONGODB_IMAGE:$MONGODB_TAG
    
# Reset path conversion
unset MSYS_NO_PATHCONV 

# Wait few seconds to let the container start
echo "Waiting for the container to start..."
sleep 5

# Check if the container is running
if [ $(docker ps -q -f name=$DB_CONTAINER_NAME) ]; then
  echo "Container $DB_CONTAINER_NAME is running"
  echo "Root user: $ROOT_USER"
  echo "Root password: $ROOT_PASSWORD"
else
  echo "Container $DB_CONTAINER_NAME is not running"
fi