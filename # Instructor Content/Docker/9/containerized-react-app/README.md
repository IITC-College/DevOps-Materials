# Containerized React + Vite App

A modern React application built with Vite and containerized with Docker. This setup includes both development and production configurations.

## Features

- ⚡ **Vite** - Lightning fast build tool and dev server
- ⚛️ **React 18** - Latest React with TypeScript
- 🐳 **Multi-stage Docker** - Separate dev and prod builds
- 🔥 **Hot Module Replacement** - Instant updates in development
- 🚀 **Nginx Production** - Lightweight production server

## Quick Start

### Development Mode

Build and run with hot reload:

```bash
# Build development image
docker build --target development -t react-vite-app:dev .

# Run with volume mounting for hot reload
docker run -it --rm -p 3000:3000 -v "$(pwd)/src:/app/src" react-vite-app:dev
```

Access the app at http://localhost:3000

### Production Mode

Build and run optimized production build:

```bash
# Build production image
docker build --target production -t react-vite-app:prod .

# Run production container
docker run -it --rm -p 8080:80 react-vite-app:prod
```

Access the app at http://localhost:8080

## Docker Stages

The Dockerfile uses multi-stage builds:

1. **Development** - Node.js with Vite dev server and HMR
2. **Build** - Compiles TypeScript and builds optimized bundle
3. **Production** - Nginx serving static files (smallest image)

## Local Development (without Docker)

```bash
# Install dependencies
npm install

# Start dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Project Structure

```
├── src/
│   ├── App.tsx          # Main App component
│   ├── App.css          # App styles
│   ├── main.tsx         # Entry point
│   └── index.css        # Global styles
├── public/              # Static assets
├── Dockerfile           # Multi-stage Docker configuration
├── vite.config.ts       # Vite configuration
├── tsconfig.json        # TypeScript configuration
└── package.json         # Dependencies and scripts
```

## Why Vite?

- **Faster** - 10-100x faster than traditional bundlers
- **Modern** - Uses native ES modules
- **Optimized** - Lightning-fast HMR
- **Smaller** - Optimized production builds
- **Better DX** - Instant server start

## Docker Benefits

- **Consistency** - Same environment everywhere
- **Isolation** - No local dependency conflicts
- **Portability** - Deploy anywhere Docker runs
- **Multi-stage** - Optimized image sizes
