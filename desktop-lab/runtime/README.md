# Lab runtime

The app creates one two-node minikube profile and a dedicated Docker bridge network per run.
All names begin with `klab-` and include a random run identifier. Credentials live outside the
learner workspace. The Linux toolbox gets only that workspace and a read-only lab kubeconfig.
It has no Docker socket, host home mount, or host shell.

`npm run test:runtime` creates a disposable profile, checks TLS connectivity, shared files,
manual Pod placement, scheduler restoration, and preservation of existing profiles and the
user kubeconfig. It removes the proof cluster in `finally`. The test requires Docker access,
ARM64 macOS, minikube, kubectl, and the pinned nginx image (initially pulled as `nginx:1.28.0`).
The tested image digest and Kubernetes version are recorded in `config.json`.

A learner has administrative access to this practice cluster. Container isolation is for
separating practice work from the host; this is not a hostile-code execution service.
