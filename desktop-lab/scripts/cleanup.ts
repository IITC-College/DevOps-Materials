import { resolve, join } from "node:path";
import { readFile, writeFile, rm } from "node:fs/promises";
import { Runtime } from "../src/main/runtime.js";
import { loadLab } from "../src/main/lab-loader.js";
const root = resolve(".state/integration");
const session = JSON.parse(await readFile(join(root, "session.json"), "utf8"));
if (session) {
  const lab = await loadLab(resolve("labs/manual-scheduling"));
  const rt = new Runtime(session.run, lab.definition.runtime);
  await rt.destroy();
  await writeFile(join(root, "session.json"), "null");
  await rm(session.run.directory, { recursive: true, force: true });
  console.log(
    "Removed the app-owned integration cluster, toolbox, network, and run credentials.",
  );
} else console.log("No integration run to clean up.");
