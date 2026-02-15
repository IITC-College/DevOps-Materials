#!/bin/bash

# Build for development (with hot reload)
docker build -t react-app:alpine .

# Run development container
docker run --rm -it     

# Build for production
docker build --target production -t react-vite-app:prod .

# Run production container
docker run -it --rm -p 8080:80 react-vite-app:prod
