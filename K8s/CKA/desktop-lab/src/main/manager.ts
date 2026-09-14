import { EventEmitter } from "node:events";
import { readFile, mkdir } from "node:fs/promises";
import { join } from "node:path";
import { Runtime, newRun, type Run, type RuntimeConfig } from "./runtime.js";
import { Engine } from "./engine.js";
import { command } from "./command.js";
import {
  atomicJSON,
  readWorkspace,
  listWorkspace,
  saveWorkspace,
} from "./files.js";
import type { LoadedLab } from "./lab-loader.js";
import type { Progress, CheckResult, Variables } from "../shared/lab.js";
import type { Snapshot, Status } from "../shared/api.js";

interface Session {
  schemaVersion: 1;
  labVersion: string;
  run: Run;
  progress: Progress;
  status: Status;
}
export type RuntimeFactory = (
  run: Run,
  config: RuntimeConfig,
  log: (message: string) => void,
) => Runtime;
export class Manager extends EventEmitter {
  session?: Session;
  runtime?: Runtime;
  engine?: Engine;
  busy = false;
  logs: string[] = [];
  results: CheckResult[] = [];
  error?: string;
  private checkGeneration = 0;
  private writes: Promise<void> = Promise.resolve();
  constructor(
    public root: string,
    public lab: LoadedLab,
    private runtimeDirectory: string,
    private factory: RuntimeFactory = (run, config, log) =>
      new Runtime(run, config, command, log),
  ) {
    super();
  }
  get variables(): Variables {
    return {
      worker: this.session?.run.worker ?? "worker node",
      controlPlane: this.session?.run.controlPlane ?? "control-plane node",
      nginxImage: this.lab.definition.runtime.nginxImage,
    };
  }
  get snapshot(): Snapshot {
    return {
      lab: this.lab.definition,
      instructions: this.lab.instructions,
      status: this.session?.status ?? "idle",
      busy: this.busy,
      runId: this.session?.run.id,
      profile: this.session?.run.profile,
      progress: this.session?.progress ?? { current: 0, checkpoints: {} },
      variables: this.variables,
      results: this.results,
      logs: this.logs,
      error: this.error,
    };
  }
  emitState() {
    this.emit("snapshot", this.snapshot);
  }
  log = (message: string) => {
    this.logs.push(message);
    this.logs = this.logs.slice(-80);
    this.emitState();
  };
  private async persist() {
    const data = this.session ? structuredClone(this.session) : null;
    const write = this.writes
      .catch(() => {})
      .then(() => atomicJSON(join(this.root, "session.json"), data));
    this.writes = write;
    await write;
  }
  async init() {
    await mkdir(this.root, { recursive: true, mode: 0o700 });
    try {
      const session = JSON.parse(
        await readFile(join(this.root, "session.json"), "utf8"),
      ) as Session | null;
      if (!session) return;
      if (
        session.schemaVersion !== 1 ||
        !session.run?.id ||
        !session.progress ||
        !Number.isInteger(session.progress.current) ||
        session.progress.current < 0 ||
        session.progress.current >= this.lab.definition.steps.length
      )
        throw new Error("Saved run is invalid");
      this.session = session;
      this.attach();
      if (session.labVersion !== this.lab.definition.version) {
        session.status = "error";
        this.error =
          "The lab definition changed. Reset this run before continuing.";
      } else
        session.status = session.status === "stopped" ? "stopped" : "resumable";
    } catch (e) {
      if ((e as NodeJS.ErrnoException).code !== "ENOENT") {
        this.error = `Could not restore progress: ${(e as Error).message}`;
        throw e;
      }
    }
  }
  private attach() {
    const session = this.session!;
    this.runtime = this.factory(
      session.run,
      this.lab.definition.runtime,
      this.log,
    );
    this.engine = new Engine(
      this.lab.definition,
      session.progress,
      async (progress) => {
        if (this.session !== session)
          throw new Error("Run changed during checkpoint save");
        const previous = session.progress;
        session.progress = progress;
        try {
          await this.persist();
        } catch (e) {
          session.progress = previous;
          throw e;
        }
      },
    );
  }
  private async operation(action: () => Promise<void>) {
    if (this.busy) throw new Error("Another environment operation is running");
    if (this.engine?.committing)
      throw new Error(
        "Saving your checkpoint. Try again when the check finishes.",
      );
    this.cancelCheck();
    this.busy = true;
    this.error = undefined;
    this.emit("terminal-close");
    this.emitState();
    try {
      await action();
    } catch (e) {
      this.error = (e as Error).message;
      if (this.session) this.session.status = "error";
      throw e;
    } finally {
      this.busy = false;
      await this.persist();
      this.emitState();
    }
  }
  async start() {
    if (this.session)
      throw new Error("A run already exists. Resume or reset it.");
    await this.operation(() => this.fresh());
  }
  private async fresh() {
    this.results = [];
    this.logs = [];
    this.session = {
      schemaVersion: 1,
      labVersion: this.lab.definition.version,
      run: newRun(join(this.root, "runs")),
      progress: { current: 0, checkpoints: {} },
      status: "starting",
    };
    this.attach();
    await this.persist();
    // Record ownership before preflight so a failed first startup can be reset safely.
    await this.runtime!.prepareFiles(join(this.lab.directory, "starter"));
    await this.runtime!.start(
      join(this.lab.directory, "starter"),
      this.runtimeDirectory,
    );
    this.session.status = "ready";
  }
  async stop() {
    await this.operation(async () => {
      this.requireRun();
      await this.runtime!.stop();
      this.session!.status = "stopped";
      this.log("Lab stopped. Files and checkpoints are saved.");
    });
  }
  async resume() {
    await this.operation(async () => {
      this.requireRun();
      if (this.session!.labVersion !== this.lab.definition.version)
        throw new Error("Lab version changed. Reset this run.");
      await this.runtime!.resume();
      this.session!.status = this.complete() ? "completed" : "ready";
      this.log("Lab resumed with saved checkpoints.");
    });
  }
  async reset() {
    await this.operation(async () => {
      if (this.session) {
        this.log("Removing this run’s environment…");
        await this.runtime!.destroy();
        this.session = undefined;
        this.engine = undefined;
        this.runtime = undefined;
        await this.persist();
      }
      await this.fresh();
    });
  }
  private requireRun() {
    if (!this.runtime || !this.session) throw new Error("Start a lab first");
  }
  requireReady() {
    this.requireRun();
    if (
      this.busy ||
      !["ready", "checking", "completed"].includes(this.session!.status)
    )
      throw new Error("Resume the lab environment first");
  }
  complete() {
    return this.lab.definition.steps.every(
      (step) => !!this.session?.progress.checkpoints[step.id],
    );
  }
  async check(stepId: string, options?: { timeout: number; interval: number }) {
    this.requireReady();
    if (this.session!.status === "checking")
      throw new Error("A check is already running");
    const session = this.session!,
      engine = this.engine!,
      runtime = this.runtime!,
      generation = ++this.checkGeneration;
    if (this.lab.definition.steps[session.progress.current].id !== stepId)
      throw new Error("Step is locked");
    session.status = "checking";
    this.results = [];
    this.error = undefined;
    this.emitState();
    try {
      await runtime.health();
      if (generation !== this.checkGeneration) return;
      const evidence = {
        resource: async (target: {
          resource: string;
          name?: string;
          namespace: string;
        }) => {
          const output = await runtime.kube([
            "get",
            target.resource,
            ...(target.name ? [target.name] : []),
            "-n",
            target.namespace,
            "--ignore-not-found=true",
            "-o",
            "json",
          ]);
          if (!output) return null;
          const object = JSON.parse(output);
          if (
            typeof object !== "object" ||
            (!object?.metadata && !Array.isArray(object?.items))
          )
            throw new Error("Invalid Kubernetes resource response");
          return object;
        },
        diagnostic: async (path: string) =>
          JSON.parse((await readWorkspace(runtime.workspace, path)).content),
      };
      await engine.check(
        stepId,
        evidence,
        this.variables,
        (results) => {
          if (generation === this.checkGeneration) {
            this.results = results;
            this.emitState();
          }
        },
        options,
      );
    } catch (e) {
      if (generation === this.checkGeneration) {
        this.error = (e as Error).message;
        this.results = [
          {
            id: "infrastructure",
            label: "Environment check",
            status: "error",
            expected: "Reachable, healthy lab cluster",
            observed: this.error,
          },
        ];
      }
    } finally {
      if (generation === this.checkGeneration && this.session === session) {
        session.status = this.complete() ? "completed" : "ready";
        await this.persist();
        this.emitState();
      }
    }
  }
  cancelCheck() {
    if (this.engine?.committing) return;
    this.checkGeneration++;
    this.engine?.cancel();
    if (this.session?.status === "checking")
      this.session.status = this.complete() ? "completed" : "ready";
    this.emitState();
  }
  async next() {
    this.requireReady();
    if (this.session!.status === "checking")
      throw new Error("Wait for the check");
    await this.engine!.next();
    this.session!.progress = this.engine!.progress;
    this.results = [];
    await this.persist();
    this.emitState();
  }
  async files() {
    return this.runtime ? listWorkspace(this.runtime.workspace) : [];
  }
  async readFile(path: string) {
    this.requireRun();
    return readWorkspace(this.runtime!.workspace, path);
  }
  async saveFile(path: string, content: string, revision: string | null) {
    this.requireRun();
    if (this.busy) throw new Error("Wait for environment setup");
    return saveWorkspace(this.runtime!.workspace, path, content, revision);
  }
}
