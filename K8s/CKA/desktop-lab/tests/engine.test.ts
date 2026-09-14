import { describe, it, expect, vi } from "vitest";
import { loadLab } from "../src/main/lab-loader.js";
import { labSchema, type Progress } from "../src/shared/lab.js";
import { Engine } from "../src/main/engine.js";
import { validate, type Evidence } from "../src/main/validator.js";
const { definition: lab } = await loadLab("labs/manual-scheduling");
const vars = {
  worker: "worker",
  controlPlane: "cp",
  nginxImage: lab.runtime.nginxImage,
};
const pod = (overrides: any = {}) => ({
  kind: "Pod",
  metadata: { name: "nginx", namespace: "default", uid: "uid-1" },
  spec: { containers: [{ name: "nginx", image: vars.nginxImage }] },
  status: { phase: "Pending" },
  ...overrides,
});
const evidence = (p: any = pod()): Evidence => ({
  resource: async () => p,
  diagnostic: async () => {
    throw new Error("missing file");
  },
});
const progress = (): Progress => ({ current: 0, checkpoints: {} });
const options = { timeout: 0, interval: 0 };
describe("definitions", () => {
  it("rejects arbitrary setup scripts and unknown checks", () => {
    expect(() =>
      labSchema.parse({
        ...lab,
        runtime: { ...lab.runtime, setup: "rm -rf /" },
      }),
    ).toThrow();
    const bad = structuredClone(lab);
    (bad.steps[0].checks[0] as any).type = "exec";
    expect(() => labSchema.parse(bad)).toThrow();
  });
  it("rejects duplicate steps, future UID references, and path traversal", () => {
    expect(() =>
      labSchema.parse({ ...lab, steps: [lab.steps[0], lab.steps[0]] }),
    ).toThrow();
    const bad = structuredClone(lab);
    (bad.steps[2].checks.at(-1) as any).checkpoint = "control-plane";
    expect(() => labSchema.parse(bad)).toThrow();
    bad.steps[0].instructions = "../private.md";
    expect(() => labSchema.parse(bad)).toThrow();
  });
});
describe("resource validation", () => {
  it.each([
    ["missing Pod", null],
    [
      "wrong name",
      pod({ metadata: { name: "other", namespace: "default", uid: "1" } }),
    ],
    [
      "wrong namespace",
      pod({ metadata: { name: "nginx", namespace: "other", uid: "1" } }),
    ],
    [
      "wrong image",
      pod({ spec: { containers: [{ name: "nginx", image: "busybox" }] } }),
    ],
    ["assigned node", pod({ spec: { ...pod().spec, nodeName: "worker" } })],
    [
      "terminating",
      pod({ metadata: { ...pod().metadata, deletionTimestamp: "now" } }),
    ],
  ])("fails %s", async (_name, p) => {
    expect(
      (await validate(lab.steps[0].checks, evidence(p), vars, {})).some(
        (r) => r.status === "unmet",
      ),
    ).toBe(true);
  });
  it("does not require Running for the first step", async () => {
    expect(
      (await validate(lab.steps[0].checks, evidence(), vars, {})).every(
        (r) => r.status === "passed",
      ),
    ).toBe(true);
  });
  it("rejects wrong node and unchanged UID for worker placement", async () => {
    const p = pod({
      spec: { ...pod().spec, nodeName: "cp" },
      status: {
        phase: "Running",
        conditions: [{ type: "Ready", status: "True" }],
      },
    });
    const checkpoints = {
      create: { podUID: "uid-1", passedAt: "now", results: [] },
    };
    const results = await validate(
      lab.steps[2].checks,
      evidence(p),
      vars,
      checkpoints,
    );
    expect(results.find((r) => r.id === "node")?.status).toBe("unmet");
    expect(results.find((r) => r.id === "recreated")?.status).toBe("unmet");
  });
  it("reports API errors distinctly", async () => {
    const ev = {
      ...evidence(),
      resource: async () => {
        throw new Error("API unavailable");
      },
    };
    expect(
      (await validate(lab.steps[0].checks, ev, vars, {})).every(
        (r) => r.status === "error",
      ),
    ).toBe(true);
  });
});
describe("gating and persistence", () => {
  it("rejects locked checks and advancing without a pass", async () => {
    const engine = new Engine(lab, progress(), async () => {});
    await expect(engine.check("worker", evidence(), vars)).rejects.toThrow(
      "locked",
    );
    await expect(engine.next()).rejects.toThrow("not passed");
  });
  it("persists before unlocking, preserves previous passes, and resumes progress", async () => {
    const save = vi.fn(async () => {});
    const engine = new Engine(lab, progress(), save);
    await engine.check("create", evidence(), vars, () => {}, options);
    expect(save).toHaveBeenCalledTimes(1);
    expect(engine.progress.checkpoints.create.podUID).toBe("uid-1");
    await engine.next();
    const resumed = new Engine(lab, structuredClone(engine.progress), save);
    expect(resumed.progress.current).toBe(1);
    expect(resumed.progress.checkpoints.create).toBeDefined();
  });
  it("does not unlock if saving fails", async () => {
    const engine = new Engine(lab, progress(), async () => {
      throw new Error("disk full");
    });
    await expect(
      engine.check("create", evidence(), vars, () => {}, options),
    ).rejects.toThrow("disk full");
    expect(engine.progress.checkpoints).toEqual({});
  });
  it("discards a late result after cancellation/reset", async () => {
    let release!: (v: any) => void;
    const pending = new Promise((resolve) => (release = resolve));
    const save = vi.fn(async () => {});
    const engine = new Engine(lab, progress(), save);
    const checking = engine.check(
      "create",
      { ...evidence(), resource: async () => pending },
      vars,
      () => {},
      options,
    );
    engine.cancel();
    release(pod());
    expect(await checking).toBeNull();
    expect(save).not.toHaveBeenCalled();
    expect(engine.progress.checkpoints).toEqual({});
  });
  it("retries unmet conditions but never advances on timeout", async () => {
    const engine = new Engine(lab, progress(), async () => {});
    const update = vi.fn();
    await engine.check("create", evidence(null), vars, update, {
      timeout: 10,
      interval: 2,
    });
    expect(update.mock.calls.length).toBeGreaterThan(1);
    await expect(engine.next()).rejects.toThrow();
  });
});
describe("diagnostic evidence", () => {
  const system = {
    kind: "List",
    items: [
      "kube-apiserver",
      "kube-controller-manager",
      "etcd",
      "kube-proxy",
    ].map((c) => ({
      metadata: {
        name: c,
        namespace: "kube-system",
        uid: c,
        labels: { component: c },
      },
    })),
  };
  const ev = (doc: any): Evidence => ({
    resource: async (target) => (target.resource === "pods" ? system : pod()),
    diagnostic: async (path) =>
      path.endsWith("system-pods.json") ? system : doc,
  });
  it("accepts current diagnostics and rejects stale identity", async () => {
    expect(
      (await validate(lab.steps[1].checks, ev(pod()), vars, {})).every(
        (r) => r.status === "passed",
      ),
    ).toBe(true);
    expect(
      (
        await validate(
          lab.steps[1].checks,
          ev(pod({ metadata: { ...pod().metadata, uid: "old" } })),
          vars,
          {},
        )
      ).find((r) => r.id === "pod-evidence")?.status,
    ).toBe("unmet");
  });
  it("rejects malformed or missing diagnostics", async () => {
    expect(
      (await validate(lab.steps[1].checks, ev("not-json"), vars, {})).find(
        (r) => r.id === "pod-evidence",
      )?.status,
    ).toBe("unmet");
    expect(
      (await validate(lab.steps[1].checks, evidence(), vars, {})).find(
        (r) => r.id === "pod-evidence",
      )?.status,
    ).toBe("unmet");
  });
});

it("keeps Next locked until an in-flight successful checkpoint is saved", async () => {
  let finish!: () => void;
  const saving = new Promise<void>((resolve) => (finish = resolve));
  const engine = new Engine(lab, progress(), () => saving);
  const checking = engine.check("create", evidence(), vars, () => {}, options);
  await vi.waitFor(() => expect(engine.committing).toBe(true));
  engine.cancel();
  expect(engine.checking).toBe(true);
  await expect(engine.next()).rejects.toThrow("current check");
  expect(engine.progress.checkpoints).toEqual({});
  finish();
  await checking;
  expect(engine.committing).toBe(false);
  expect(engine.progress.checkpoints.create).toBeDefined();
});
