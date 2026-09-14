import { mkdir, writeFile, readFile, cp, chmod } from "node:fs/promises";
import { join } from "node:path";
import { randomUUID } from "node:crypto";
import { command, sleep, type Command } from "./command.js";

export interface Run {
  id: string;
  profile: string;
  network: string;
  toolbox: string;
  directory: string;
  clusterUID?: string;
  worker?: string;
  controlPlane?: string;
}
export interface RuntimeConfig {
  kubernetesVersion: string;
  nginxImage: string;
  toolboxImage: string;
}
export const newRun = (root: string): Run => {
  const id = randomUUID();
  const name = `klab-${id.slice(0, 12)}`;
  return {
    id,
    profile: name,
    network: name,
    toolbox: `${name}-tools`,
    directory: join(root, id),
  };
};
const BACKUP = "/var/lib/kubernetes-lab-backup/kube-scheduler.yaml";
const MANIFEST = "/etc/kubernetes/manifests/kube-scheduler.yaml";
export class Runtime {
  constructor(
    public run: Run,
    public config: RuntimeConfig,
    private execute: Command = command,
    private log: (message: string) => void = () => {},
  ) {
    if (
      !/^klab-[0-9a-f]{8}-[0-9a-f]{3}$/.test(run.profile) ||
      run.network !== run.profile ||
      run.toolbox !== `${run.profile}-tools` ||
      !run.id.startsWith(run.profile.slice(5))
    )
      throw new Error("Invalid app-owned run identity");
  }
  get workspace() {
    return join(this.run.directory, "workspace");
  }
  get kubeconfig() {
    return join(this.run.directory, "credentials", "host.yaml");
  }
  get env() {
    return { KUBECONFIG: this.kubeconfig };
  }
  async kube(args: string[], input?: string) {
    return this.execute(
      "kubectl",
      ["--kubeconfig", this.kubeconfig, "--context", this.run.profile, ...args],
      { timeout: 30_000, input },
    );
  }
  async json(args: string[]) {
    return JSON.parse(await this.kube([...args, "-o", "json"]));
  }
  async preflight() {
    const versions = await Promise.all(
      ["minikube", "kubectl"].map((bin) =>
        this.execute(
          bin,
          bin === "minikube"
            ? ["version", "--short"]
            : ["version", "--client", "-o", "json"],
        ),
      ),
    );
    const docker = JSON.parse(
      await this.execute("docker", ["info", "--format", "{{json .}}"]),
    );
    if (
      docker.OSType !== "linux" ||
      !["aarch64", "arm64"].includes(docker.Architecture)
    )
      throw new Error(
        "This release requires a local ARM64 Linux Docker engine. Start Docker Desktop on your Apple Silicon Mac.",
      );
    if (docker.NCPU < 4 || docker.MemTotal < 6 * 1024 ** 3)
      throw new Error(
        "Allocate at least 4 CPUs and 6 GiB memory to Docker Desktop for the two-node lab.",
      );
    this.log(
      `Preflight passed: ${docker.NCPU} CPUs, ${(docker.MemTotal / 1024 ** 3).toFixed(1)} GiB Docker memory. Other running workloads also use these resources.`,
    );
    return { versions, cpus: docker.NCPU, memory: docker.MemTotal };
  }
  async prepareFiles(starter: string) {
    await mkdir(join(this.run.directory, "credentials"), {
      recursive: true,
      mode: 0o700,
    });
    await mkdir(this.workspace, { recursive: true });
    await cp(starter, this.workspace, { recursive: true });
    await mkdir(join(this.workspace, "diagnostics"), { recursive: true });
    await writeFile(
      join(this.run.directory, "owner.json"),
      JSON.stringify({ id: this.run.id, profile: this.run.profile }),
      { mode: 0o600 },
    );
  }
  private async ownership() {
    const owner = JSON.parse(
      await readFile(join(this.run.directory, "owner.json"), "utf8"),
    );
    if (owner.id !== this.run.id || owner.profile !== this.run.profile)
      throw new Error("Run ownership could not be verified");
    const profiles = JSON.parse(
      await this.execute("minikube", ["profile", "list", "-o", "json"]),
    );
    const profile = profiles.valid?.find(
      (p: any) => p.Name === this.run.profile,
    );
    if (profile && profile.Config.Network !== this.run.network)
      throw new Error("Profile network does not match this run");
  }
  async start(starter: string, runtimeDirectory: string) {
    await this.preflight();
    await this.prepareFiles(starter);
    const profiles = JSON.parse(
      await this.execute("minikube", ["profile", "list", "-o", "json"]),
    );
    if (
      [...(profiles.valid ?? []), ...(profiles.invalid ?? [])].some(
        (p: any) => p.Name === this.run.profile,
      )
    )
      throw new Error("Profile already exists; refusing to adopt it");
    this.log("Creating private lab network…");
    await this.execute("docker", [
      "network",
      "create",
      "--label",
      `dev.kubernetes-lab.run=${this.run.id}`,
      this.run.network,
    ]);
    this.log(
      "Starting two Kubernetes nodes. First startup may take several minutes…",
    );
    await this.execute(
      "minikube",
      [
        "start",
        "-p",
        this.run.profile,
        "--driver=docker",
        `--network=${this.run.network}`,
        "--nodes=2",
        "--cpus=2",
        "--memory=2048mb",
        `--kubernetes-version=${this.config.kubernetesVersion}`,
        "--keep-context",
        "--embed-certs",
        "--interactive=false",
        "--wait=apiserver,node_ready,system_pods",
        "--wait-timeout=6m",
      ],
      { env: this.env, timeout: 600_000 },
    );
    await chmod(this.kubeconfig, 0o600);
    const nodes = (await this.json(["get", "nodes"])).items;
    this.run.controlPlane = nodes.find(
      (node: any) =>
        "node-role.kubernetes.io/control-plane" in node.metadata.labels,
    )?.metadata.name;
    this.run.worker = nodes.find(
      (node: any) =>
        !("node-role.kubernetes.io/control-plane" in node.metadata.labels),
    )?.metadata.name;
    if (!this.run.worker || !this.run.controlPlane)
      throw new Error("Expected one control-plane node and one worker");
    this.run.clusterUID = (
      await this.json(["get", "namespace", "kube-system"])
    ).metadata.uid;
    this.log("Preparing the pinned nginx image on both nodes…");
    await this.execute(
      "minikube",
      ["-p", this.run.profile, "image", "load", this.config.nginxImage],
      { env: this.env, timeout: 300_000 },
    );
    this.log("Building the Linux toolbox…");
    await this.execute(
      "docker",
      [
        "build",
        "--build-arg",
        `KUBERNETES_VERSION=${this.config.kubernetesVersion}`,
        "-t",
        this.config.toolboxImage,
        runtimeDirectory,
      ],
      { timeout: 600_000 },
    );
    await this.createToolbox();
    await this.disableScheduler();
    await this.health();
    this.log("Lab environment is ready.");
  }
  async createToolbox() {
    const config = JSON.parse(
      await this.kube(["config", "view", "--raw", "--flatten", "-o", "json"]),
    );
    const info = JSON.parse(
      await this.execute("docker", ["inspect", this.run.controlPlane!]),
    )[0];
    const ip = info.NetworkSettings.Networks[this.run.network]?.IPAddress;
    if (!ip)
      throw new Error("Control plane is not connected to the lab network");
    config.clusters[0].cluster.server = `https://${ip}:8443`;
    config["current-context"] = this.run.profile;
    await writeFile(
      join(this.run.directory, "credentials", "toolbox.yaml"),
      JSON.stringify(config),
      { mode: 0o600 },
    );
    await this.execute("docker", [
      "run",
      "-d",
      "--name",
      this.run.toolbox,
      "--label",
      `dev.kubernetes-lab.run=${this.run.id}`,
      "--network",
      this.run.network,
      "--cap-drop=ALL",
      "--security-opt=no-new-privileges",
      "--mount",
      `type=bind,src=${this.workspace},dst=/workspace`,
      "--mount",
      `type=bind,src=${join(this.run.directory, "credentials", "toolbox.yaml")},dst=/lab/kubeconfig,readonly`,
      "-e",
      "KUBECONFIG=/lab/kubeconfig",
      "-e",
      `WORKER_NODE=${this.run.worker}`,
      "-e",
      `CONTROL_PLANE_NODE=${this.run.controlPlane}`,
      "-w",
      "/workspace",
      this.config.toolboxImage,
      "sleep",
      "infinity",
    ]);
    await this.toolbox(["kubectl", "get", "nodes", "-o", "json"]);
  }
  async toolbox(args: string[]) {
    return this.execute("docker", ["exec", this.run.toolbox, ...args], {
      timeout: 30_000,
    });
  }
  async node(commandText: string) {
    return this.execute(
      "minikube",
      [
        "-p",
        this.run.profile,
        "ssh",
        "--node",
        this.run.controlPlane!,
        "--",
        commandText,
      ],
      { env: this.env },
    );
  }
  async disableScheduler() {
    this.log("Preparing the missing-scheduler scenario…");
    await this.node(
      `sudo mkdir -p /var/lib/kubernetes-lab-backup && if sudo test -f ${MANIFEST}; then sudo mv ${MANIFEST} ${BACKUP}; fi; sudo test -f ${BACKUP}`,
    );
    for (let i = 0; i < 45; i++) {
      if (
        (
          await this.json([
            "get",
            "pods",
            "-n",
            "kube-system",
            "-l",
            "component=kube-scheduler",
          ])
        ).items.length === 0
      )
        return;
      await sleep(2000);
    }
    throw new Error("Scheduler did not stop");
  }
  async restoreScheduler() {
    await this.node(`sudo test -f ${BACKUP} && sudo mv ${BACKUP} ${MANIFEST}`);
    for (let i = 0; i < 45; i++) {
      const pods = (
        await this.json([
          "get",
          "pods",
          "-n",
          "kube-system",
          "-l",
          "component=kube-scheduler",
        ])
      ).items;
      if (
        pods.some((p: any) =>
          p.status.conditions?.some(
            (c: any) => c.type === "Ready" && c.status === "True",
          ),
        )
      )
        return;
      await sleep(2000);
    }
    throw new Error("Scheduler did not recover");
  }
  async health() {
    const uid = (await this.json(["get", "namespace", "kube-system"])).metadata
      .uid;
    if (uid !== this.run.clusterUID)
      throw new Error(
        "Cluster identity changed. Reset the lab to begin a fresh run.",
      );
    const nodes = (await this.json(["get", "nodes"])).items;
    if (
      nodes.length !== 2 ||
      nodes.some(
        (n: any) =>
          !n.status.conditions.some(
            (c: any) => c.type === "Ready" && c.status === "True",
          ),
      )
    )
      throw new Error("Both lab nodes must be Ready");
    if (
      (
        await this.json([
          "get",
          "pods",
          "-n",
          "kube-system",
          "-l",
          "component=kube-scheduler",
        ])
      ).items.length
    )
      throw new Error(
        "The scheduler is running; reset the lab to restore the exercise.",
      );
  }
  async stop() {
    await this.ownership();
    await this.execute("docker", ["stop", this.run.toolbox]);
    await this.execute("minikube", ["stop", "-p", this.run.profile], {
      env: this.env,
      timeout: 180_000,
    });
  }
  async resume() {
    await this.preflight();
    await this.ownership();
    const profiles = JSON.parse(
      await this.execute("minikube", ["profile", "list", "-o", "json"]),
    );
    if (!profiles.valid?.some((p: any) => p.Name === this.run.profile))
      throw new Error("Lab cluster is missing. Reset to begin a fresh run.");
    await this.execute(
      "minikube",
      [
        "start",
        "-p",
        this.run.profile,
        "--keep-context",
        "--embed-certs",
        "--interactive=false",
        "--wait=apiserver,node_ready",
      ],
      { env: this.env, timeout: 600_000 },
    );
    await this.health();
    // Recreate only the toolbox to refresh its API endpoint after a Docker restart.
    await this.removeContainer();
    await this.createToolbox();
  }
  private async removeContainer() {
    const containers = JSON.parse(
      await this.execute("docker", [
        "container",
        "ls",
        "-a",
        "--filter",
        `name=^/${this.run.toolbox}$`,
        "--format",
        "json",
      ]).then((s) => `[${s.split("\n").filter(Boolean).join(",")}]`),
    );
    if (!containers.length) return;
    const info = JSON.parse(
      await this.execute("docker", ["inspect", this.run.toolbox]),
    )[0];
    if (info.Config.Labels?.["dev.kubernetes-lab.run"] !== this.run.id)
      throw new Error("Toolbox ownership mismatch");
    await this.execute("docker", ["rm", "-f", this.run.toolbox]);
  }
  async destroy() {
    await this.ownership();
    await this.removeContainer();
    await this.execute("minikube", ["delete", "-p", this.run.profile], {
      env: this.env,
      timeout: 180_000,
    });
    const networks = await this.execute("docker", [
      "network",
      "ls",
      "--filter",
      `name=^${this.run.network}$`,
      "--format",
      "{{.Name}}",
    ]);
    if (networks) {
      const network = JSON.parse(
        await this.execute("docker", ["network", "inspect", this.run.network]),
      )[0];
      if (network.Labels?.["dev.kubernetes-lab.run"] !== this.run.id)
        throw new Error("Network ownership mismatch");
      await this.execute("docker", ["network", "rm", this.run.network]);
    }
  }
}
