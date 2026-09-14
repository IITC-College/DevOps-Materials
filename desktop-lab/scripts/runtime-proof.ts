import { readFile, writeFile, mkdir } from "node:fs/promises";
import { join, resolve } from "node:path";
import { homedir } from "node:os";
import assert from "node:assert/strict";
import { Runtime, newRun } from "../src/main/runtime.js";
import { command, sleep } from "../src/main/command.js";

const root = resolve(".state/proof");
await mkdir(root, { recursive: true });
const run = newRun(root);
const nginx = (
  await command("docker", [
    "image",
    "inspect",
    "nginx:1.28.0",
    "--format",
    "{{index .RepoDigests 0}}",
  ])
).trim();
const config = {
  kubernetesVersion: "v1.37.0",
  nginxImage: nginx,
  toolboxImage: "kubernetes-lab-toolbox:0.1.0",
};
await writeFile("runtime/config.json", JSON.stringify(config, null, 2) + "\n");
const originalKubeconfig = await readFile(join(homedir(), ".kube/config"));
const profilesBefore = JSON.parse(
  await command("minikube", ["profile", "list", "-o", "json"]),
).valid.map((p: any) => ({ Name: p.Name, Config: p.Config }));
const rt = new Runtime(run, config, command, console.log);
await writeFile(join(root, "run.json"), JSON.stringify(run));
try {
  await rt.start(resolve("labs/manual-scheduling/starter"), resolve("runtime"));
  await writeFile(join(root, "run.json"), JSON.stringify(run));
  assert.deepEqual(
    await readFile(join(homedir(), ".kube/config")),
    originalKubeconfig,
  );
  console.log("PASS: default kubeconfig unchanged");
  await rt.toolbox(["bash", "-lc", "printf toolbox > /workspace/shared.txt"]);
  assert.equal(
    await readFile(join(rt.workspace, "shared.txt"), "utf8"),
    "toolbox",
  );
  await writeFile(join(rt.workspace, "shared.txt"), "editor");
  assert.equal(await rt.toolbox(["cat", "/workspace/shared.txt"]), "editor");
  console.log("PASS: shared files and toolbox TLS connectivity");
  const pod = (node?: string) => ({
    apiVersion: "v1",
    kind: "Pod",
    metadata: { name: "nginx", namespace: "default" },
    spec: {
      ...(node ? { nodeName: node } : {}),
      containers: [
        { name: "nginx", image: nginx, imagePullPolicy: "IfNotPresent" },
      ],
    },
  });
  await rt.kube(["create", "-f", "-"], JSON.stringify(pod()));
  assert.equal(
    (await rt.json(["get", "pod", "nginx"])).status.phase,
    "Pending",
  );
  for (const node of [run.worker, run.controlPlane]) {
    await rt.kube([
      "delete",
      "pod",
      "nginx",
      "--wait=true",
      "--grace-period=1",
    ]);
    await rt.kube(["create", "-f", "-"], JSON.stringify(pod(node)));
    for (let i = 0; i < 45; i++) {
      const p = await rt.json(["get", "pod", "nginx"]);
      if (
        p.status.conditions?.some(
          (c: any) => c.type === "Ready" && c.status === "True",
        )
      )
        break;
      await sleep(2000);
    }
    const p = await rt.json(["get", "pod", "nginx"]);
    assert.equal(p.spec.nodeName, node);
    assert.equal(p.status.phase, "Running");
    assert.ok(
      p.status.conditions.some(
        (c: any) => c.type === "Ready" && c.status === "True",
      ),
    );
    console.log(`PASS: nginx Running and Ready on ${node}`);
  }
  await rt.restoreScheduler();
  console.log("PASS: scheduler restored");
  await rt.disableScheduler();
  console.log("PASS: scheduler removed again");
  assert.deepEqual(
    await readFile(join(homedir(), ".kube/config")),
    originalKubeconfig,
  );
  const profilesAfter = JSON.parse(
    await command("minikube", ["profile", "list", "-o", "json"]),
  ).valid;
  for (const p of profilesBefore)
    assert.deepEqual(
      profilesAfter.find((x: any) => x.Name === p.Name)?.Config,
      p.Config,
    );
  console.log("PASS: existing profiles unchanged");
  await writeFile(
    join(root, "result.json"),
    JSON.stringify(
      { passed: true, config, run, at: new Date().toISOString() },
      null,
      2,
    ),
  );
} finally {
  await rt.destroy();
  console.log("Removed runtime proof cluster and toolbox.");
}
