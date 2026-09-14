import { resolve } from "node:path";
import { loadLab } from "../src/main/lab-loader.js";
import { bundleDocument } from "../src/main/lab-document.js";
import { createCatalogServer } from "./server.js";
const { server } = await createCatalogServer({
  root: resolve(process.env.KLAB_SERVER_DATA_DIR ?? ".state/catalog-server"),
  adminPassword: process.env.KLAB_ADMIN_PASSWORD ?? "",
  template: await bundleDocument(await loadLab(resolve(process.env.KLAB_SEED_DIR ?? "labs/manual-scheduling"))),
});
const port = Number(process.env.PORT ?? 4318);
if (!Number.isInteger(port) || port < 1 || port > 65535) throw new Error("Invalid PORT");
server.listen(port, process.env.HOST ?? "127.0.0.1", () => console.log(`Lab catalog listening on port ${port}`));
for (const signal of ["SIGTERM", "SIGINT"] as const) process.on(signal, () => server.close());
