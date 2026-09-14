import assert from "node:assert/strict";
import { resolve, join } from "node:path";
import { readFile, writeFile } from "node:fs/promises";
import { Manager } from "../src/main/manager.js";
import { loadLab } from "../src/main/lab-loader.js";
const root = resolve(".state/integration");
const lab = await loadLab(resolve("labs/manual-scheduling"));
const manager = new Manager(root, lab, resolve("runtime"));
await manager.init();
const seen = new Set<string>();
manager.on("snapshot", (s) => {
  for (const line of s.logs)
    if (!seen.has(line)) {
      seen.add(line);
      console.log(line);
    }
});
assert.equal(manager.snapshot.status, "resumable");
assert.equal(Object.keys(manager.snapshot.progress.checkpoints).length, 4);
await manager.resume();
assert.equal(manager.snapshot.status, "completed");
console.log("PASS: app restart restores all checkpoints");
const uid = (await manager.runtime!.json(["get", "pod", "nginx"])).metadata.uid;
await manager.stop();
assert.equal(manager.snapshot.status, "stopped");
await manager.resume();
assert.equal(manager.snapshot.status, "completed");
assert.equal(
  (await manager.runtime!.json(["get", "pod", "nginx"])).metadata.uid,
  uid,
);
console.log("PASS: stop/resume preserves Pod identity and progress");
const clusterUID = manager.session!.run.clusterUID;
manager.session!.run.clusterUID = "unexpected-replacement";
await assert.rejects(() => manager.runtime!.health(), /identity changed/);
manager.session!.run.clusterUID = clusterUID;
console.log(
  "PASS: live cluster identity is checked against the saved identity",
);
const oldId = manager.session!.run.id;
await manager.reset();
assert.notEqual(manager.session!.run.id, oldId);
assert.equal(manager.snapshot.status, "ready");
assert.deepEqual(manager.snapshot.progress.checkpoints, {});
assert.equal(
  await readFile(join(manager.runtime!.workspace, "nginx.yaml"), "utf8"),
  await readFile(join(lab.directory, "starter/nginx.yaml"), "utf8"),
);
assert.equal(
  await manager.runtime!.kube([
    "get",
    "pod",
    "nginx",
    "--ignore-not-found=true",
    "-o",
    "json",
  ]),
  "",
);
await manager.runtime!.health();
console.log(
  "PASS: reset creates a fresh unscheduled lab and restores starter files",
);
await writeFile(
  join(root, "recovery-result.json"),
  JSON.stringify(
    {
      passed: true,
      at: new Date().toISOString(),
      profile: manager.session!.run.profile,
    },
    null,
    2,
  ),
);
console.log(`Fresh run retained for packaged-app test: ${root}`);
