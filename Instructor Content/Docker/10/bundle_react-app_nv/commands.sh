docker volume create website-data

docker run --rm -d -p 3000:80 --name website-main -v website-data:/usr/share/nginx/html nginx:1.27.0

curl http://localhost:3000

# Create Few more websites
docker run --rm -d -p 3001:80 --name website-readonly1 -v website-data:/usr/share/nginx/html nginx:1.27.0
docker run --rm -d -p 3002:80 --name website-readonly2 -v website-data:/usr/share/nginx/html nginx:1.27.0
docker run --rm -d -p 3003:80 --name website-readonly3 -v website-data:/usr/share/nginx/html nginx:1.27.0

curl http://localhost:3001
curl http://localhost:3002
curl http://localhost:3003