import type { Lab, Progress, CheckResult, Variables } from "../shared/lab.js";
import { validate, type Evidence } from "./validator.js";
import { sleep } from "./command.js";

export class Engine {
  private generation = 0;
  checking = false;
  committing = false;
  constructor(
    public lab: Lab,
    public progress: Progress,
    private save: (progress: Progress) => Promise<void>,
  ) {}
  cancel() {
    // A successful check is committed atomically; cancellation applies to evaluation.
    if (this.committing) return;
    this.generation++;
    this.checking = false;
  }
  async next() {
    if (this.checking) throw new Error("Wait for the current check");
    const step = this.lab.steps[this.progress.current];
    if (!this.progress.checkpoints[step.id])
      throw new Error("This step has not passed");
    if (this.progress.current >= this.lab.steps.length - 1)
      throw new Error("Lab is already complete");
    const next = { ...this.progress, current: this.progress.current + 1 };
    await this.save(next);
    this.progress = next;
  }
  async check(
    stepId: string,
    evidence: Evidence,
    vars: Variables,
    onUpdate: (results: CheckResult[]) => void = () => {},
    options = { timeout: 60_000, interval: 2000 },
  ) {
    if (this.checking) throw new Error("A check is already running");
    const step = this.lab.steps[this.progress.current];
    if (step.id !== stepId) throw new Error("Step is locked");
    this.checking = true;
    const generation = ++this.generation;
    const started = Date.now();
    try {
      while (true) {
        const cache = new Map<string, Promise<any>>();
        const snapshotEvidence: Evidence = {
          ...evidence,
          resource: (target) => {
            const key = JSON.stringify(target);
            if (!cache.has(key)) cache.set(key, evidence.resource(target));
            return cache.get(key)!;
          },
        };
        const results = await validate(
          step.checks,
          snapshotEvidence,
          vars,
          this.progress.checkpoints,
        );
        if (generation !== this.generation) return null;
        onUpdate(results);
        if (results.every((r) => r.status === "passed")) {
          const pod = await snapshotEvidence.resource({
            resource: "pod",
            name: "nginx",
            namespace: "default",
          });
          if (generation !== this.generation) return null;
          if (!pod?.metadata?.uid)
            throw new Error(
              "Pod disappeared before its checkpoint could be saved",
            );
          const next = {
            ...this.progress,
            checkpoints: {
              ...this.progress.checkpoints,
              [step.id]: {
                passedAt: new Date().toISOString(),
                podUID: pod.metadata.uid,
                results,
              },
            },
          };
          this.committing = true;
          await this.save(next);
          if (generation !== this.generation) return null;
          this.progress = next;
          return results;
        }
        if (
          results.some((r) => r.status === "error") ||
          Date.now() - started >= options.timeout
        )
          return results;
        await sleep(
          Math.min(
            options.interval,
            Math.max(0, options.timeout - (Date.now() - started)),
          ),
        );
        if (generation !== this.generation) return null;
      }
    } finally {
      if (generation === this.generation) {
        this.checking = false;
        this.committing = false;
      }
    }
  }
}
