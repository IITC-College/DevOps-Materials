#!/bin/bash

# Build for development (with hot reload)
docker build -t react-app:alpine .

# Run development container
docker run --rm -it -p 3000:3000 react-app:alpine sh

# Part 2:
docker build -t react-app:nginx .

docker run --rm -it -d -p 9000:80 react-app:nginx


# RUUN AGAIN DOCKER BVUILD FOR NEW UY+UPDATED IMAGE
docker build -t react-app:blue .

docker run --rm -it -d -p 9001:80 react-app:blue