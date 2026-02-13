# Hints

## Task 1 - Hello World Container
- The `docker run` command pulls the image if it's not already on your system
- If you see "Unable to find image locally", that's normal - Docker will download it
- The hello-world container exits immediately after printing its message
- This is a test container designed to verify Docker is working correctly

## Task 2 - List Images
- `docker images` shows all images stored locally on your machine
- The TAG column usually shows "latest" for the most recent version
- Image IDs are unique identifiers (like a hash)
- Size shows how much disk space the image uses
- Images are templates used to create containers

## Task 3 - Run NGINX Web Server
- The `-d` flag means "detached" - runs in the background
- Without `-d`, the container output would fill your terminal
- Port mapping format: `-p HOST_PORT:CONTAINER_PORT`
- Port 8080 on your computer → Port 80 inside the container
- `--name` is optional but makes containers easier to reference
- If port 8080 is already in use, try 8081, 8082, etc.

## Task 4 - View Container Logs
- Logs show everything the container writes to stdout/stderr
- For web servers, logs show HTTP requests
- Use `docker logs -f my-nginx` to follow logs in real-time (Ctrl+C to stop)
- Logs persist even if the container stops
- This is crucial for debugging container issues

## Task 5 - Execute Commands Inside Container
- `docker exec` runs a command in an already running container
- `-it` means interactive terminal (you can type commands)
- Without `-it`, you can run single commands like: `docker exec my-nginx ls /etc`
- The container's filesystem is separate from your host
- You're running bash inside a Linux container
- Type `exit` to leave the container shell

## Task 6 - Stop and Remove Containers
- `docker stop` gracefully shuts down the container (sends SIGTERM)
- `docker ps` shows only running containers
- `docker ps -a` shows all containers (running and stopped)
- Stopped containers still exist and can be started again with `docker start`
- `docker rm` permanently deletes a stopped container
- You can't remove a running container (stop it first, or use `docker rm -f`)

## Task 7 - PostgreSQL Database Container
- Environment variables (`-e`) configure the container
- `POSTGRES_PASSWORD` is required for the postgres image
- The database takes a few seconds to initialize
- Default PostgreSQL port is 5432
- `psql` is the PostgreSQL command-line client
- `-U postgres` means connect as the "postgres" user
- SQL commands must end with a semicolon (;)
- Backslash commands (\l, \dt, \q) don't need semicolons

## Task 8 - Inspect Container Details
- `docker inspect` returns a huge JSON object with all container details
- Use `grep` or `jq` to filter specific information
- The IP address is the container's internal IP on the Docker network
- `docker stats` shows live resource usage
- `--no-stream` shows one snapshot instead of continuous updates

## Task 9 - Run Multiple Containers
- Each container needs a unique name
- Each container using host ports needs a different port number
- You can't map two containers to the same host port
- Containers are isolated from each other by default
- You can run dozens of containers simultaneously

## Task 10 - Clean Up Everything
- Always clean up after labs to free resources
- You can stop multiple containers in one command: `docker stop container1 container2`
- Same for remove: `docker rm container1 container2`
- Removing containers doesn't remove their images
- Images can be safely removed if no containers are using them
- Use `docker system prune` to clean up everything (be careful!)

## General Tips

### Docker Run Flags
- `-d` : Detached mode (background)
- `-p` : Port mapping (host:container)
- `-e` : Environment variable
- `--name` : Give container a friendly name
- `-it` : Interactive terminal
- `--rm` : Automatically remove container when it stops
- `-v` : Volume mount (not covered in this lab)

### Common Docker Commands
```bash
# Container Management
docker run <image>          # Create and start a container
docker start <container>    # Start a stopped container
docker stop <container>     # Stop a running container
docker restart <container>  # Restart a container
docker rm <container>       # Remove a container
docker ps                   # List running containers
docker ps -a                # List all containers

# Image Management
docker images               # List images
docker pull <image>         # Download an image
docker rmi <image>          # Remove an image

# Information & Debugging
docker logs <container>     # View container logs
docker logs -f <container>  # Follow logs in real-time
docker exec -it <container> bash  # Get a shell inside container
docker inspect <container>  # View detailed info
docker stats <container>    # View resource usage

# Cleanup
docker stop $(docker ps -aq)      # Stop all containers
docker rm $(docker ps -aq)        # Remove all containers
docker system prune               # Remove unused data
docker system prune -a            # Remove all unused images too
```

### Troubleshooting Tips

**"Cannot connect to the Docker daemon"**
- Check if Docker is running: `sudo systemctl status docker`
- Start Docker: `sudo systemctl start docker`
- You might need to add your user to the docker group: `sudo usermod -aG docker $USER`

**"Port is already in use"**
- Another container or process is using that port
- Use a different port: `-p 8081:80` instead of `-p 8080:80`
- Or stop the conflicting container/process

**"Container name already in use"**
- A container with that name exists (even if stopped)
- Remove it: `docker rm container-name`
- Or use a different name: `--name my-nginx-2`

**Container exits immediately**
- Check the logs: `docker logs container-name`
- Some images need environment variables or specific commands
- Use `docker ps -a` to see the exit code

**"Unable to find image locally"**
- This is normal! Docker will pull the image from Docker Hub
- Make sure you have internet connection
- The first run takes longer while downloading

### Best Practices
- Always give containers meaningful names
- Use `-d` for long-running services (web servers, databases)
- Clean up containers you're not using
- Check logs when something doesn't work as expected
- Use `docker ps` frequently to see what's running
- Read image documentation on Docker Hub for specific configuration options

### Understanding Container vs Image
- **Image**: A template/blueprint (like a class in programming)
- **Container**: A running instance of an image (like an object)
- One image can create many containers
- Deleting a container doesn't delete its image
- Images are read-only; containers have a writable layer

### Port Mapping Explained
```
-p 8080:80
   ↑    ↑
   |    |
   |    └─ Port inside container (where nginx listens)
   |
   └─ Port on your host machine (where you connect)
```

You connect to localhost:8080, Docker forwards it to port 80 inside the container.
