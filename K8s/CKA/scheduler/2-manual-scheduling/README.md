# [CKA] Class-Lab 1.1: Manual Scheduling

## Lab environment

Use a two-node practice cluster with one control-plane node and one worker node. The `kube-scheduler` must be absent or stopped in this lab environment. Preparing that cluster is outside this exercise; with an active scheduler, the Pod may be scheduled automatically instead of remaining pending.

Use the provided [nginx.yaml](nginx.yaml). Perform all Pod operations in the `default` namespace.

## Task 1: Create the Pod

### Actions

1. List the cluster nodes and record the worker and control-plane node names.
2. Open `nginx.yaml` and verify that it defines a Pod named `nginx`, using the `nginx` container image, with no node assignment.
3. Create the Pod from the file.

### Expected behavior

The Pod is created but has not been assigned to a node.

## Task 2: Inspect the pending Pod

### Actions

1. Display the status of the Pod you created.
2. Inspect its details and events, and verify that no node is assigned.
3. List the Pods in the `kube-system` namespace and verify that `kube-scheduler` is not running in the lab environment.

Hint: Use the `get` and `describe` subcommands of `kubectl`; the `-n` flag selects a namespace.

### Expected behavior

The Pod remains `Pending` without a node assignment. In this environment, no scheduler is running to assign it.

## Task 3: Manually schedule the Pod on the worker

### Actions

1. Edit `nginx.yaml` and add the `nodeName` field under `spec`.
2. Set its value to the worker node name you recorded. The original lab uses `node01`; use your actual worker node name if it differs.
3. Delete the existing Pod and recreate it from the updated file. Use separate delete and create operations, or a replacement operation that deletes and recreates the Pod.
4. Watch the Pod status continuously until it reaches `Running`.
5. Display the Pod with its node information and verify that it is running on your chosen worker.

Hints: Check `kubectl replace` help for `--force`, and `kubectl get` help for `--watch` and `-o wide`.

### Expected behavior

The new Pod is assigned to the worker through `nodeName`. It may initially show `ContainerCreating` before the container starts running.

## Task 4: Recreate the Pod on the control-plane node

### Actions

1. Edit `nginx.yaml` again and change `spec.nodeName` to the control-plane node name. The original lab uses `controlplane`; adapt it to your cluster.
2. Delete and recreate the Pod using the updated file.
3. Wait for deletion to finish and for the new Pod to start.
4. Display its status and assigned node. Verify that it is `Running` on the control-plane node.

### Expected behavior

The previous Pod is deleted, and a new Pod with the same name is created on the control-plane node. Changing placement requires recreation; the running Pod is not moved between nodes. Container shutdown can take time, so a delay during deletion does not necessarily indicate a problem.
