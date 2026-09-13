# Hands-On: Manual Scheduling with the Binding API

**Section:** CKA / Scheduling
**Time:** ~25 minutes
**Goal:** Place Pods on nodes yourself - with `nodeName`, and with a `Binding` object - and understand when each one works.

## Before you start

This lab needs **more than one node**. A default minikube cluster has only one, so start a
3-node cluster (1 control plane + 2 workers). Each node is a separate container with its own
kubelet, so Pods really run where you put them.

```bash
minikube start -p cka --nodes 3 --driver=docker
kubectl config use-context cka
kubectl wait --for=condition=Ready node --all --timeout=180s
kubectl get nodes
```

```
NAME      STATUS   ROLES           AGE   VERSION
cka       Ready    control-plane   60s   v1.37.0
cka-m02   Ready    <none>          45s   v1.37.0
cka-m03   Ready    <none>          35s   v1.37.0
```

> Low on memory? Add `--cpus=2 --memory=2g`. Already created the cluster? `minikube start -p cka` restarts it.

minikube does **not** taint its control plane, unlike a kubeadm cluster (and the exam). Add the
taint so the scheduler only uses the workers, the way a real cluster behaves:

```bash
kubectl taint node cka node-role.kubernetes.io/control-plane:NoSchedule
```

Everything runs in the `default` namespace. The two workers are your targets:

- Node A: `cka-m02`
- Node B: `cka-m03`

---

## Task 1 - Watch the scheduler do its job

1. Create the Pod in `scheduled-pod.yaml`.
2. Find out **which node** it landed on.
3. Look at the Pod's events and find the line written by the scheduler.

> **Hints**
>
> - `kubectl get pod <name> -o wide` shows the node.
> - `kubectl describe pod <name>` - read the `Events` section at the bottom.
> - Who is the `From:` of the scheduling event?

---

## Task 2 - Bypass the scheduler with `nodeName`

1. Open `nodename-pod.yaml` and replace `CHANGE-ME` with **Node A**.
2. Create the Pod and verify it is running on the node you picked.
3. Describe it and compare the events with Task 1. **Which event is missing, and why?**

> **Hints**
>
> - `spec.nodeName` is normally filled in *by* the scheduler. Setting it yourself means the Pod is already assigned when it reaches the API server.
> - No scheduler ran, so there is no `Scheduled` event - the kubelet just picks the Pod up.

---

## Task 3 - Create a Pod that nobody will schedule

1. Look at `pending-pod.yaml` and find the field that makes this Pod different.
2. Create it, then check its status.
3. Describe the Pod. How many events does it have? Is there a `PodScheduled` condition?

> **Hints**
>
> - `spec.schedulerName: manual-scheduler` - there is no such scheduler running, so nothing claims the Pod.
> - The Pod stays `Pending` forever. This is exactly the state a Pod is in when you must place it by hand.

---

## Task 4 - Bind the Pod by hand

Now place `pending-pod` on **Node A** using the `Binding` object in `binding.yaml`:

```yaml
apiVersion: v1
kind: Binding
metadata:
  name: pending-pod # Must match the EXACT name of the Pod you want to bind
  namespace: default # Must match the namespace of the Pod
target:
  apiVersion: v1
  kind: Node
  name: CHANGE-ME # The name of the target Node you want to place the Pod on
```

1. Fill in the target node name.
2. Send the Binding to the API server with `kubectl create -f binding.yaml`. Read the output - what did kubectl say it created?
3. Verify the Pod is now `Running` on that node.
4. Describe it. **Is there a `Scheduled` event this time? Is the `PodScheduled` condition set?**
5. Run `kubectl get bindings`. What does the API server answer?

> **Hints**
>
> - The API server replies to a Binding with a `Status` object, not with the Binding - that is why kubectl prints something odd.
> - The `Scheduled` event is written by the **scheduler**, not by the API server. You are not the scheduler.
> - A `Binding` is a write-only resource: the API only accepts `POST` on it. There is nothing to `get`.
> - The `metadata.name` of the Binding **is** the Pod name. Get it wrong and you bind nothing (or the wrong Pod).

---

## Task 5 - Repetition drill (and the `apply` trap)

`rgb-pending-pods.yaml` contains three unschedulable Pods: `red-pod`, `green-pod`, `blue-pod`.

1. Create all three and confirm all three are `Pending`.
2. Bind **red** to Node A and **green** to Node B with `kubectl create`, one Binding at a time.
3. Bind **blue** to Node A, but this time use `kubectl apply`. Read the output. **Did it fail? Where is `blue-pod` now?**
4. Verify the placement of all three in a single command.
5. Count how many lab Pods each node is running.

> **Hints**
>
> - Copy `binding.yaml` per Pod, or edit and re-send the same file.
> - `apply` reports an error, but check the Pod before believing it. Retrying with `create` will tell you the truth.
> - `kubectl get pods -l lab=manual-scheduling -o wide`
> - Node column only: `kubectl get pods -l lab=manual-scheduling -o custom-columns=POD:.metadata.name,NODE:.spec.nodeName`

---

## Task 6 - Try to move a Pod

1. Write a new Binding that sends `red-pod` from Node A to Node B and create it. What does the API server answer?
2. Try `kubectl edit pod red-pod` and change `spec.nodeName` by hand. What happens when you save?
3. Move the Pod to Node B for real.

> **Hints**
>
> - An already-bound Pod is rejected: the API server returns a `409 Conflict` - the Pod is already assigned to a node.
> - `spec.nodeName` is immutable on an existing Pod. The edit is refused.
> - There is no "move" in Kubernetes: delete the Pod, recreate it, and bind it again.

---

## Task 7 - Bind to a node that does not exist

1. Delete `blue-pod` and recreate it from `rgb-pending-pods.yaml`.
2. Bind it to `cka-m04` - a node that is **not** in your cluster. Does the API server refuse?
3. Check the Pod's status, node and events.
4. Delete the Pod. What happens?

> **Hints**
>
> - The Binding API checks that the Pod exists and is unbound. It does not check the node.
> - No kubelet is watching `cka-m04`, so nobody starts the Pod - and nobody confirms it stopped either.
> - Kubernetes eventually cleans up Pods bound to nodes that don't exist. `kubectl delete pod blue-pod --force --grace-period=0` removes it immediately.

---

## Cleanup

```bash
kubectl delete pods -l lab=manual-scheduling
```

Keep the cluster for the next scheduling labs. When you are done for the day:

```bash
kubectl taint node cka node-role.kubernetes.io/control-plane:NoSchedule-   # optional: undo the taint
minikube stop -p cka      # or: minikube delete -p cka
```

---

## What you should be able to answer

- What does the scheduler actually *write* when it schedules a Pod?
- What is the difference between `nodeName` in the Pod spec and a `Binding` object?
- Why is there no `Scheduled` event on a Pod you bound yourself?
- Why does `kubectl apply` on a Binding print an error, and why should you not trust that error?
- Why does a `Binding` on an already-scheduled Pod fail?
- What does the API server *not* validate when you bind a Pod?
