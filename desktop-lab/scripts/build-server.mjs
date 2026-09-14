import { build } from "esbuild";
await build({ entryPoints: ["backend/main.ts"], outfile: "dist/server/main.mjs", bundle: true, platform: "node", format: "esm", target: "node24" });
