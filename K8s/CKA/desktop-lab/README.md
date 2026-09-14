# Kubernetes Lab

An English-language desktop workspace for real local Kubernetes exercises. It creates an
isolated minikube cluster, provides a Linux terminal and YAML editor, and checks the live
cluster before unlocking each next step.

## Run locally

Requirements: Apple Silicon Mac, Docker Desktop running with at least 4 CPUs and 6 GiB
allocated, minikube, and kubectl. Other running containers also consume Docker resources.
Initial cluster and toolbox downloads need internet access. The tested Kubernetes version
and pinned nginx image are recorded in `labs/manual-scheduling/lab.yaml`.

```bash
cd desktop-lab
npm ci
npm run dev
```

Use **Start lab** to create the environment. Edit `nginx.yaml`, save it, and run commands in
the Linux terminal. **Check** polls the real cluster for up to 60 seconds. Every requirement
must pass before **Next** unlocks. Hints are available without revealing complete solutions.

**Stop** preserves your files and checkpoints. **Resume** verifies the saved cluster before
continuing. Closing the window keeps the cluster running. **Reset Lab** asks for confirmation
and replaces only this application's lab resources with a fresh run.

The first lab covers creating a pending nginx Pod, saving diagnostic evidence, and manually
recreating it on the worker and control-plane nodes. Node names appear in the instructions
and are also available as `$WORKER_NODE` and `$CONTROL_PLANE_NODE` in the terminal.

## Build the desktop app

```bash
npm run package
```

The local ARM64 application is created at `release/mac-arm64/Kubernetes Lab.app`. This is a
local development build, without a distribution signing identity or notarization.

## Validation

```bash
npm test                  # Engine, validation, lifecycle, and file handling
npm run test:e2e           # Electron UI with disposable fake workspaces
npm run test:runtime       # Disposable real minikube runtime proof
npm run test:integration   # Full graded lab on a disposable real minikube cluster
```

The runtime proof initially resolves its nginx image from `nginx:1.28.0`, so pull that tag
before invoking it: `docker pull nginx:1.28.0`. Regular app startup and integration tests use
the digest already committed in the lab bundle. Integration tests use the real validators,
intentionally fail every step, and then complete it correctly. Tests never adopt `cka` or
`minikube`. Generated test credentials and logs stay in ignored `.state/` directories.

## Add or change a lab

A bundle contains `lab.yaml`, Markdown instructions, and `starter/` files. The first bundle
is `labs/manual-scheduling/`. It is deliberately the only bundled lab in this release.
To author a new bundle, copy its structure, assign a new ID/version, and select that bundle
in the main-process loader. A catalog selection UI is a later extension.

`schemaVersion: 1` definitions declare ordered steps. Each step has a stable ID, title,
instruction path, hint, and a nonempty list of checks. Supported checks:

| Type         | What it checks                                                             |
| ------------ | -------------------------------------------------------------------------- |
| `exists`     | A named Kubernetes resource exists                                         |
| `field`      | A dotted object field equals a value; null also matches an absent field    |
| `container`  | A named container has the required image                                   |
| `condition`  | A Kubernetes condition has the required status                             |
| `uidChanged` | A Pod UID differs from a prior checkpoint                                  |
| `diagnostic` | A saved Pod or kube-system JSON inventory matches current cluster evidence |

Use `{{worker}}`, `{{controlPlane}}`, and `{{nginxImage}}` in instructions or expected values.
UID comparisons must refer to an earlier step. Setup operations are registered in code;
lab files cannot supply host shell scripts. The v1 setup recipe is `manual-scheduling`,
which prepares two nodes and removes the scheduler's static manifest from its watched
folder. This initial recipe and checkpoint capture are Pod-oriented; additional scenarios
may require new registered setup operations or validators.

## Runtime boundaries

Electron's isolated renderer calls narrow, validated IPC methods. The main process owns
cluster lifecycle and grading. It reads Kubernetes JSON through its own kubectl process;
terminal output is never treated as proof of success.

Every run has a random `klab-` profile and Docker network. All host Kubernetes operations use
an explicit private kubeconfig and context. The Linux toolbox shares only that run's
workspace and a read-only lab kubeconfig; it has no host home directory or Docker socket.
The app verifies profile/network/container ownership before removing resources.

App state lives in Electron’s per-user application directory under
`~/Library/Application Support/` on macOS. A
`KLAB_DATA_DIR` environment override is available for isolated development/test sessions.
The fake runtime is enabled only for unpackaged Electron UI tests with `KLAB_FAKE=1` and
is ignored by the packaged app. This is a local practice tool, not a tamper-proof exam.

If Docker is unavailable, start Docker Desktop and use **Resume**. If the lab cluster was
removed or replaced, use **Reset Lab**. A failed setup exposes the error and leaves the
run available for reset; unrelated clusters are never automatically stopped or deleted.

For the full recovery and packaged-app sequence, retain the integration run temporarily:

```bash
KLAB_KEEP_RUN=1 npm run test:integration
npm run test:recovery
npm run package
npm run test:packaged
npm run test:cleanup
```

Recovery checks retain a fresh run for the packaged test. The packaged test uses that real
run, completes all four steps through the desktop app, captures `docs/app-screenshot.png`,
and stops the cluster. Cleanup removes only the recorded app-owned integration resources.
Test evidence is summarized in [docs/VALIDATION.md](docs/VALIDATION.md).
