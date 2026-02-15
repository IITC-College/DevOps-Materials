# Build the development container
docker build -t react-app:dev -f Dockerfile.dev .

# Run the development container
docker run --rm -d -p 3000:3000 react-app:dev

# Inspect the containers
docker ps

# Get logs
docker logs -f <container_id>

# Stop the container`
docker stop <container_id>

# Add Volumes to the container
docker run --rm -d -p 3000:3000 -v ./public:/app/public -v ./src:/app/src react-app:dev