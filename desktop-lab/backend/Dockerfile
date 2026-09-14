FROM node:24-bookworm-slim AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci --ignore-scripts
COPY tsconfig.json ./
COPY src ./src
COPY backend ./backend
COPY scripts/build-server.mjs ./scripts/build-server.mjs
RUN node scripts/build-server.mjs

FROM node:24-bookworm-slim
ENV NODE_ENV=production HOST=0.0.0.0 PORT=4318 KLAB_SERVER_DATA_DIR=/data
WORKDIR /app
COPY --from=build /app/dist/server ./dist/server
COPY labs ./labs
RUN mkdir /data && chown node:node /data
USER node
EXPOSE 4318
VOLUME ["/data"]
HEALTHCHECK --interval=30s --timeout=5s CMD node -e "fetch('http://127.0.0.1:4318/health').then(r=>process.exit(r.ok?0:1)).catch(()=>process.exit(1))"
CMD ["node", "dist/server/main.mjs"]
