import assert from "node:assert/strict";
import { resolve, join } from "node:path";
import { mkdir, writeFile, readFile } from "node:fs/promises";
import { Manager } from "../src/main/manager.js";
import { loadLab } from "../src/main/lab-loader.js";

const root = resolve(".state/integration");
await mkdir(root, { recursive: true });
const lab = await loadLab(resolve("labs/manual-scheduling"));
const manager = new Manager(root, lab, resolve("runtime"));
await manager.init();
manager.on("snapshot", () => {});
const seen = new Set<string>();
manager.on("snapshot", (s) => {
  for (const l of s.logs)
    if (!seen.has(l)) {
      seen.add(l);
      console.log(l);
    }
});
let passed = false;
try {
  if (manager.session) await manager.reset();
  else await manager.start();
  const rt = manager.runtime!;
  const fail = async (step: string) => {
    await manager.check(step, { timeout: 0, interval: 0 });
    assert.ok(
      !manager.session!.progress.checkpoints[step],
      `${step} should fail`,
    );
    assert.ok(
      manager.results.some((r) => r.status === "unmet"),
      JSON.stringify(manager.results),
    );
    await assert.rejects(() => manager.next(), /not passed/);
    console.log(`PASS: ${step} rejects incorrect work and keeps Next locked`);
  };
  const pass = async (step: string) => {
    await manager.check(step);
    assert.ok(
      manager.session!.progress.checkpoints[step],
      JSON.stringify(manager.results),
    );
    console.log(`PASS: ${step} accepts correct live-cluster evidence`);
  };
  const pod = (node?: string) => ({
    apiVersion: "v1",
    kind: "Pod",
    metadata: { name: "nginx", namespace: "default" },
    spec: {
      ...(node ? { nodeName: node } : {}),
      containers: [
        {
          name: "nginx",
          image: lab.definition.runtime.nginxImage,
          imagePullPolicy: "IfNotPresent",
        },
      ],
    },
  });
  const recreate = async (node?: string) => {
    await rt.toolbox([
      "kubectl",
      "delete",
      "pod",
      "nginx",
      "--ignore-not-found=true",
      "--wait=true",
      "--grace-period=1",
    ]);
    await writeFile(
      join(rt.workspace, "nginx.yaml"),
      JSON.stringify(pod(node), null, 2),
    );
    await rt.toolbox(["kubectl", "create", "-f", "nginx.yaml"]);
  };
  await assert.rejects(() => manager.check("worker"), /locked/);
  await fail("create");
  await recreate();
  await pass("create");
  await manager.next();
  await fail("inspect");
  await rt.toolbox([
    "bash",
    "-lc",
    "kubectl get pod nginx -n default -o json > diagnostics/pod.json && kubectl get pods -n kube-system -o json > diagnostics/system-pods.json",
  ]);
  await pass("inspect");
  await manager.next();
  await fail("worker");
  await recreate(rt.run.worker);
  await pass("worker");
  await manager.next();
  await fail("control-plane");
  await recreate(rt.run.controlPlane);
  await pass("control-plane");
  assert.equal(manager.snapshot.status, "completed");
  assert.equal(Object.keys(manager.snapshot.progress.checkpoints).length, 4);
  const persisted = JSON.parse(
    await readFile(join(root, "session.json"), "utf8"),
  );
  assert.equal(Object.keys(persisted.progress.checkpoints).length, 4);
  await writeFile(
    join(root, "result.json"),
    JSON.stringify(
      {
        passed: true,
        at: new Date().toISOString(),
        profile: rt.run.profile,
        checkpoints: manager.snapshot.progress.checkpoints,
      },
      null,
      2,
    ),
  );
  passed = true;
  console.log("PASS: all four steps completed and persisted on a real cluster");
} finally {
  if (process.env.KLAB_KEEP_RUN === "1" && passed)
    console.log(
      `Keeping owned integration run for packaging/recovery tests: ${root}`,
    );
  else if (manager.runtime) {
    await manager.runtime.destroy();
    await writeFile(join(root, "session.json"), "null");
    console.log("Removed integration cluster.");
  }
}
