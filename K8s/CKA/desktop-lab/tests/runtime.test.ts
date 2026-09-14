import { describe, it, expect, vi } from "vitest";
import { Runtime, newRun } from "../src/main/runtime.js";
import type { Command } from "../src/main/command.js";
const config = {
  kubernetesVersion: "v1.37.0",
  nginxImage: "nginx@sha256:test",
  toolboxImage: "tools",
};
describe("runtime boundaries", () => {
  it("rejects existing user profile names", () => {
    expect(
      () => new Runtime({ ...newRun("/tmp/lab"), profile: "cka" }, config),
    ).toThrow("Invalid app-owned");
  });
  it("always selects the private kubeconfig and explicit context", async () => {
    const exec = vi.fn<Command>().mockResolvedValue("{}");
    const run = newRun("/tmp/lab");
    const rt = new Runtime(run, config, exec);
    await rt.json(["get", "pods"]);
    expect(exec.mock.calls[0][1]).toEqual([
      "--kubeconfig",
      rt.kubeconfig,
      "--context",
      run.profile,
      "get",
      "pods",
      "-o",
      "json",
    ]);
  });
  it("reports Docker resource shortage before setup", async () => {
    const exec: Command = async (bin) =>
      bin === "docker"
        ? JSON.stringify({
            OSType: "linux",
            Architecture: "aarch64",
            NCPU: 2,
            MemTotal: 2 * 1024 ** 3,
          })
        : "version";
    await expect(
      new Runtime(newRun("/tmp/lab"), config, exec).preflight(),
    ).rejects.toThrow("Allocate at least");
  });
  it("rejects a replaced cluster", async () => {
    const rt = new Runtime(
      { ...newRun("/tmp/lab"), clusterUID: "original" },
      config,
      async () => JSON.stringify({ metadata: { uid: "replacement" } }),
    );
    await expect(rt.health()).rejects.toThrow("Cluster identity changed");
  });
  it("accepts healthy nodes with the intentionally absent scheduler", async () => {
    const exec: Command = async (_bin, args) => {
      if (args.includes("namespace"))
        return JSON.stringify({ metadata: { uid: "original" } });
      if (args.includes("nodes"))
        return JSON.stringify({
          items: [1, 2].map(() => ({
            status: { conditions: [{ type: "Ready", status: "True" }] },
          })),
        });
      return JSON.stringify({ items: [] });
    };
    const rt = new Runtime(
      { ...newRun("/tmp/lab"), clusterUID: "original" },
      config,
      exec,
    );
    await expect(rt.health()).resolves.toBeUndefined();
  });
});

describe("runtime failures", () => {
  it("does not hide API failures during health checks", async () => {
    const rt = new Runtime(
      { ...newRun("/tmp/lab"), clusterUID: "original" },
      config,
      async () => {
        throw new Error("connection refused");
      },
    );
    await expect(rt.health()).rejects.toThrow("connection refused");
  });
  it("rejects a running scheduler", async () => {
    const exec: Command = async (_bin, args) => {
      if (args.includes("namespace"))
        return JSON.stringify({ metadata: { uid: "original" } });
      if (args.includes("nodes"))
        return JSON.stringify({
          items: [1, 2].map(() => ({
            status: { conditions: [{ type: "Ready", status: "True" }] },
          })),
        });
      return JSON.stringify({
        items: [{ metadata: { name: "kube-scheduler" } }],
      });
    };
    await expect(
      new Runtime(
        { ...newRun("/tmp/lab"), clusterUID: "original" },
        config,
        exec,
      ).health(),
    ).rejects.toThrow("scheduler is running");
  });
  it("does not treat malformed JSON as an empty resource list", async () => {
    const rt = new Runtime(
      newRun("/tmp/lab"),
      config,
      async () => "<html>error</html>",
    );
    await expect(rt.json(["get", "pods"])).rejects.toThrow();
  });
});

it("sets the toolbox current context even when the host context is preserved", async () => {
  const { mkdtemp, mkdir, readFile, rm } = await import("node:fs/promises");
  const { tmpdir } = await import("node:os");
  const { join } = await import("node:path");
  const root = await mkdtemp(join(tmpdir(), "klab-context-"));
  const run = { ...newRun(root), controlPlane: "cp", worker: "worker" };
  await mkdir(join(run.directory, "credentials"), { recursive: true });
  const exec: Command = async (bin, args) => {
    if (bin === "kubectl")
      return JSON.stringify({
        clusters: [{ cluster: { server: "https://127.0.0.1:12345" } }],
        contexts: [{ name: run.profile }],
        "current-context": "",
      });
    if (args[0] === "inspect")
      return JSON.stringify([
        {
          NetworkSettings: {
            Networks: { [run.network]: { IPAddress: "192.168.50.2" } },
          },
        },
      ]);
    return "{}";
  };
  try {
    await new Runtime(run, config, exec).createToolbox();
    const kube = JSON.parse(
      await readFile(
        join(run.directory, "credentials", "toolbox.yaml"),
        "utf8",
      ),
    );
    expect(kube["current-context"]).toBe(run.profile);
    expect(kube.clusters[0].cluster.server).toBe("https://192.168.50.2:8443");
    expect(
      kube.clusters[0].cluster["insecure-skip-tls-verify"],
    ).toBeUndefined();
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});
