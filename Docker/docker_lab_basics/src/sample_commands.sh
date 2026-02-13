#!/bin/bash

# Docker Lab - Sample Commands Reference
# This file contains all the commands used in the lab for quick reference

echo "================================"
echo "Docker Lab - Sample Commands"
echo "================================"
echo ""

# Task 1: Hello World
echo "Task 1: Run Hello World"
echo "docker run hello-world"
echo ""

# Task 2: List Images
echo "Task 2: List Images"
echo "docker images"
echo ""

# Task 3: Run NGINX
echo "Task 3: Run NGINX Web Server"
echo "docker run -d -p 8080:80 --name my-nginx nginx"
echo "docker ps"
echo "curl http://localhost:8080"
echo ""

# Task 4: View Logs
echo "Task 4: View Container Logs"
echo "docker logs my-nginx"
echo ""

# Task 5: Execute Commands
echo "Task 5: Execute Commands Inside Container"
echo "docker exec -it my-nginx bash"
echo "# Inside container: ls /usr/share/nginx/html/"
echo "# Inside container: exit"
echo ""

# Task 6: Stop and Remove
echo "Task 6: Stop and Remove Containers"
echo "docker stop my-nginx"
echo "docker ps -a"
echo "docker rm my-nginx"
echo ""

# Task 7: PostgreSQL
echo "Task 7: Run PostgreSQL Database"
echo "docker run -d --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_DB=testdb -p 5432:5432 postgres"
echo "docker logs my-postgres"
echo "docker exec -it my-postgres psql -U postgres -d testdb"
echo ""

# Task 8: Inspect
echo "Task 8: Inspect Container"
echo "docker inspect my-postgres"
echo "docker stats my-postgres --no-stream"
echo ""

# Task 9: Multiple Containers
echo "Task 9: Run Multiple Containers"
echo "docker run -d -p 8081:80 --name nginx-2 nginx"
echo "docker ps"
echo ""

# Task 10: Cleanup
echo "Task 10: Clean Up Everything"
echo "docker stop my-postgres nginx-2"
echo "docker rm my-postgres nginx-2"
echo "docker rmi nginx postgres hello-world"
echo ""

echo "================================"
echo "Quick Reference Commands"
echo "================================"
echo "docker ps                # List running containers"
echo "docker ps -a             # List all containers"
echo "docker images            # List images"
echo "docker logs <name>       # View logs"
echo "docker stop <name>       # Stop container"
echo "docker rm <name>         # Remove container"
echo "docker rmi <image>       # Remove image"
echo "docker exec -it <name> bash  # Get shell in container"
echo ""
