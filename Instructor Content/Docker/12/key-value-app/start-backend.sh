#! /bin/bash

# Load database configuration
source .env.db

# Load network configuration
source .env.network

# Connectivity
LOCALHOST_PORT=3000
CONTAINER_PORT=3000

BACKEND_IMAGE_NAME="key-value-backend"
BACKEND_TAG="latest"
BACKEND_CONTAINER_NAME="backend"

MONGODB_HOST="MongoDB"

# Disable MSYS path conversion for Docker volume mounts
export MSYS_NO_PATHCONV=1

# Check if the container already exists
if [ "$(docker ps -q -f name=$BACKEND_CONTAINER_NAME)" ]; then
  echo "Container already exists."
  echo "To stop it run: docker kill $BACKEND_CONTAINER_NAME"
  exit 1
fi

# Build the image
docker build -t $BACKEND_IMAGE_NAME:$BACKEND_TAG \
    -f backend/Dockerfile.dev \
    backend

# Start the container
docker run -d --rm --name $BACKEND_CONTAINER_NAME \
    -e KEY_VALUE_DB=$KEY_VALUE_DB \
    -e KEY_VALUE_USER=$KEY_VALUE_USER \
    -e KEY_VALUE_PASSWORD=$KEY_VALUE_PASSWORD \
    -e PORT=$CONTAINER_PORT \
    -e MONGODB_HOST=$MONGODB_HOST \
    -p $LOCALHOST_PORT:$CONTAINER_PORT \
    -v ./backend/src:/app/src \
    --network $NETWORK_NAME \
    $BACKEND_IMAGE_NAME:$BACKEND_TAG
    

# Wait few seconds to let the container start
echo "Waiting for the container to start..."
sleep 5

# Check if the container is running
if [ $(docker ps -q -f name=$DB_CONTAINER_NAME) ]; then
    # Health check
    curl -X GET http://localhost:3000/health
    if [ $? -eq 0 ]; then
        echo "Health check passed"
    else
        echo "Health check failed"
    fi
else
  echo "Container $DB_CONTAINER_NAME is not running"
fi