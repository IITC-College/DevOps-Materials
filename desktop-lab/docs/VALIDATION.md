# Validation record

Validated on an Apple Silicon Mac on September 14, 2026.

| Layer         | Result                                                                                         |
| ------------- | ---------------------------------------------------------------------------------------------- |
| TypeScript    | Strict type check passed                                                                       |
| Unit tests    | 36 passed across engine, validators, runtime, manager, and workspace files                     |
| Electron UI   | 3 passed: terminal/gating, editor conflicts, reset confirmation                                |
| Runtime proof | Two real nodes, toolbox TLS, shared files, manual placement, scheduler recovery                |
| Full lab      | All four steps rejected incorrect work, then passed using live Kubernetes evidence             |
| Recovery      | Checkpoints restored after restart; stop/resume retained Pod UID; reset restored starter files |
| Packaged app  | Native terminal connected to Linux toolbox; all four steps completed; cluster stopped          |
| Dependencies  | npm audit reported zero known vulnerabilities                                                  |

Runtime: minikube **v1.39.0**, Kubernetes **v1.37.0**, Docker Desktop ARM64.
Desktop: Electron **44.3.0**, React **19.3.0**, Monaco **0.56.0**, node-pty **1.1.0**.
The nginx image and toolbox base image are pinned by digest in the lab bundle and Dockerfile.

The runtime proof compared the user's kubeconfig byte-for-byte and compared the existing
minikube profile configurations before and after. Those remained unchanged. All real
integration operations used separate, randomly named `klab-` resources.

Tests cover missing Pods, wrong name/namespace/image/node, termination, readiness, unchanged
UIDs, invalid/stale diagnostic files, API failures, locked-step requests, failed persistence,
late cancelled results, reset races, checkpoint-save cancellation, path traversal, symlinks,
and editor save conflicts.
Docker-unavailable failures are injected in tests rather than stopping the user's Docker
service. Cluster replacement detection is tested with a mismatched expected cluster UID.

[Desktop screenshot](app-screenshot.png)

The application bundle is a local ARM64 development build. Distribution signing and
notarization, Windows/Linux installers, and a multi-lab catalog are outside this release.
