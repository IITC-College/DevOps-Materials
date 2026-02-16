docker run -d --rm \
  --name mongodb \
  mongodb/mongodb-community-server:7.0-ubuntu2204


# Memory 1GB
docker run -d --rm \
  --name mongodb \
  --memory="20m" \
  mongodb/mongodb-community-server:7.0-ubuntu2204


