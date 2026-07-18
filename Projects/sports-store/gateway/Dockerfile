# Build context is the project root (see docker-compose.yml).
FROM node:20-alpine AS frontend-build

WORKDIR /app
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci
COPY frontend/ .
RUN npm run build

FROM nginx:1.27-alpine

COPY gateway/nginx.conf /etc/nginx/conf.d/default.conf
COPY gateway/proxy_params.conf /etc/nginx/proxy_params.conf
COPY --from=frontend-build /app/dist /usr/share/nginx/html

EXPOSE 80
