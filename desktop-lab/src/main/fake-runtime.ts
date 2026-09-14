// Used only by unpackaged Electron UI tests. Production builds always use Runtime.
import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { Runtime } from "./runtime.js";
export class FakeRuntime extends Runtime {
  override async start(starter: string) {
    await this.prepareFiles(starter);
    this.run.worker = "test-worker";
    this.run.controlPlane = "test-control-plane";
    this.run.clusterUID = "test-cluster";
  }
  override async health() {}
  override async stop() {}
  override async resume() {}
  override async destroy() {}
  override async kube(args: string[]) {
    if (args.includes("pods"))
      return JSON.stringify({
        kind: "List",
        items: [
          "kube-apiserver",
          "kube-controller-manager",
          "etcd",
          "kube-proxy",
        ].map((c) => ({
          metadata: {
            name: c,
            uid: c,
            namespace: "kube-system",
            labels: { component: c },
          },
        })),
      });
    try {
      return await readFile(join(this.workspace, ".test-pod.json"), "utf8");
    } catch {
      return "";
    }
  }
}
