import { it, expect, beforeEach, afterEach } from "vitest";
import { mkdtemp, rm, readFile, writeFile } from "node:fs/promises";
import { join, resolve } from "node:path";
import { tmpdir } from "node:os";
import { Manager } from "../src/main/manager.js";
import { FakeRuntime } from "../src/main/fake-runtime.js";
import { loadLab } from "../src/main/lab-loader.js";
const lab = await loadLab(resolve("labs/manual-scheduling"));
let root: string;
const create = () =>
  new Manager(
    root,
    lab,
    resolve("runtime"),
    (run, config, log) => new FakeRuntime(run, config, undefined, log),
  );
beforeEach(async () => {
  root = await mkdtemp(join(tmpdir(), "klab-manager-"));
});
afterEach(() => rm(root, { recursive: true, force: true }));
it("permits only one active run", async () => {
  const manager = create();
  await manager.start();
  await expect(manager.start()).rejects.toThrow("already exists");
});
it("keeps the same UID for the resource snapshot that actually passed", async () => {
  const manager = create();
  await manager.start();
  const pod = {
    kind: "Pod",
    metadata: { name: "nginx", namespace: "default", uid: "first" },
    spec: {
      containers: [{ name: "nginx", image: lab.definition.runtime.nginxImage }],
    },
    status: { phase: "Pending" },
  };
  await writeFile(
    join(manager.runtime!.workspace, ".test-pod.json"),
    JSON.stringify(pod),
  );
  await manager.check("create", { timeout: 0, interval: 0 });
  expect(manager.snapshot.progress.checkpoints.create.podUID).toBe("first");
  const restored = create();
  await restored.init();
  expect(restored.snapshot.status).toBe("resumable");
  expect(restored.snapshot.progress.checkpoints.create.podUID).toBe("first");
});
it("does not let a cancelled check affect a reset run", async () => {
  const manager = create();
  await manager.start();
  const oldId = manager.session!.run.id;
  let release!: (v: string) => void;
  const pending = new Promise<string>((r) => (release = r));
  manager.runtime!.kube = async () => pending;
  const checking = manager.check("create", { timeout: 0, interval: 0 });
  await new Promise((resolve) => setTimeout(resolve, 5));
  await manager.reset();
  release("");
  await checking;
  expect(manager.session!.run.id).not.toBe(oldId);
  expect(manager.snapshot.progress.checkpoints).toEqual({});
  const disk = JSON.parse(await readFile(join(root, "session.json"), "utf8"));
  expect(disk.run.id).toBe(manager.session!.run.id);
  expect(disk.progress.checkpoints).toEqual({});
});
it("reports environment errors without awarding a pass", async () => {
  const manager = create();
  await manager.start();
  manager.runtime!.health = async () => {
    throw new Error("Docker is unavailable");
  };
  await manager.check("create", { timeout: 0, interval: 0 });
  expect(manager.snapshot.results[0].status).toBe("error");
  expect(manager.snapshot.progress.checkpoints).toEqual({});
});
