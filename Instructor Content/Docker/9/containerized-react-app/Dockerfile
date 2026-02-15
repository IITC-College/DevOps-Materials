# Development stage
FROM node:18-alpine AS build 

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# Production stage
FROM nginx:1.27.0

COPY --from=build /app/dist /usr/share/nginx/html