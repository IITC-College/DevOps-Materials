# Hands-On: Manual Scheduling with the Binding API

**Section:** CKA / Scheduling
**Time:** ~25 minutes
**Goal:** Place Pods on nodes yourself - with `nodeName`, and with a `Binding` object - and understand when each one works.

> **How to use this lab:** the hints name the command to reach for, never the full command line.
> Build it yourself from `--help` and `kubectl explain`. In the exam, those are your documentation.
> Stuck for more than a few minutes? The solution lives in a separate folder at the root of the repo:
> [.solutions/K8s/CKA/scheduler/1-manual-scheduling/SOLUTION.md](../../../../.solutions/K8s/CKA/scheduler/1-manual-scheduling/SOLUTION.md)

## Before you start

This lab needs **more than one node**. A default minikube cluster has only one, so create a
cluster with **3 nodes** (1 control plane + 2 workers) under the profile name **`cka`**. Each
node is a separate container with its own kubelet, so Pods really run where you put them.

1. Start the cluster, then make sure `kubectl` points at it.
2. Wait until all 3 nodes are `Ready` before you continue.
3. minikube does **not** taint its control plane, unlike a kubeadm cluster (and the exam). Add the
   taint `node-role.kubernetes.io/control-plane` with effect `NoSchedule` to the node `cka`, so the
   scheduler only uses the workers.

> **Hints**
>
> - `minikube start --help` - look for the flag that sets the **number of nodes**.
> - The **profile** flag is global, so it is not in that list: `minikube options`.
> - `kubectl config --help` - which subcommand switches context?
> - `kubectl wait --help` - you can wait on a node condition too, not only on Pods.
> - `kubectl taint --help` - the examples show the `key=value:Effect` format. The value is optional.
> - Short on memory? `minikube start --help` also has flags for CPUs and memory.

When `kubectl get nodes` shows three nodes, write down your two workers:

- Node A: `cka-m02`
- Node B: `cka-m03`

Everything runs in the `default` namespace.

---

## Task 1 - Watch the scheduler do its job

1. Create the Pod in `scheduled-pod.yaml`.
2. Find out **which node** it landed on.
3. Look at the Pod's events and find the line written by the scheduler.

> **Hints**
>
> - `kubectl get --help` - find the output format that adds a NODE column.
> - `kubectl describe` - read the `Events` section at the bottom.
> - Who is the `From:` of the scheduling event?

---

## Task 2 - Bypass the scheduler with `nodeName`

1. Open `nodename-pod.yaml` and replace `CHANGE-ME` with **Node A**.
2. Create the Pod and verify it is running on the node you picked.
3. Describe it and compare the events with Task 1. **Which event is missing, and why?**
4. Bonus: what would happen if you set `nodeName` to the tainted node `cka`?

> **Hints**
>
> - `kubectl explain pod.spec.nodeName` - read who normally fills this field in.
> - If a Pod is already assigned when it reaches the API server, does the scheduler need to look at it?

---

## Task 3 - Create a Pod that nobody will schedule

1. Look at `pending-pod.yaml` and find the field that makes this Pod different.
2. Create it, then check its status.
3. Describe the Pod. How many events does it have? Is there a `PodScheduled` condition?

> **Hints**
>
> - `kubectl explain pod.spec.schedulerName`
> - Is there a scheduler in your cluster that answers to that name? `kubectl get pods -n kube-system`
> - To see the raw status, use `kubectl get --help` and look at the `-o jsonpath` examples.

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
2. Send the Binding to the API server with `kubectl create`. Read the output - what did kubectl say it created?
3. Verify the Pod is now `Running` on that node.
4. Describe it. **Is there a `Scheduled` event this time? Is the `PodScheduled` condition set?**
5. Try to list the Bindings in the namespace. What does the API server answer?

> **Hints**
>
> - `kubectl explain binding` - what are the fields, and what does the description say this object is for?
> - `kubectl api-resources` - find `bindings`. Then run it again with `-o wide` and read the **VERBS** column.
> - Who writes the `Scheduled` event: the API server, or the scheduler?
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
> - `apply` reports an error, but check the Pod before believing it. Then try `create` for the same Pod.
> - Want to see what `apply` really sent? `kubectl options` - look for the log verbosity flag, and try level 6.
> - All three lab Pods share the label `lab=manual-scheduling`. `kubectl get --help` - find the label selector flag.
> - For a POD / NODE table only, `kubectl get --help` - look at `-o custom-columns`.

---

## Task 6 - Try to move a Pod

1. Write a new Binding that sends `red-pod` from Node A to Node B and create it. What does the API server answer?
2. Try `kubectl edit` on `red-pod` and change `spec.nodeName` by hand. What happens when you save?
3. Move the Pod to Node B for real.

> **Hints**
>
> - Read the error messages completely - both tell you exactly which rule you broke.
> - Which Pod fields may be changed after creation? The `edit` error lists them.
> - Kubernetes has no "move" for Pods. What is left?

---

## Task 7 - Bind to a node that does not exist

1. Delete `blue-pod` and recreate it from `rgb-pending-pods.yaml`.
2. Bind it to `cka-m04` - a node that is **not** in your cluster. Does the API server refuse?
3. Check the Pod's status, node and events.
4. Delete the Pod. What happens?

> **Hints**
>
> - What does the Binding API validate: the Pod, the node, or both?
> - Who confirms that a Pod has stopped before it disappears from the API?
> - `kubectl delete --help` - look at `--force` and `--grace-period`, and read the warning in the help text.

---

## Cleanup

1. Delete every lab Pod in one command.
2. Keep the cluster for the next scheduling labs. When you are done for the day, stop it (or delete it).
3. Optional: remove the control-plane taint.

> **Hints**
>
> - `kubectl delete --help` - it takes a label selector too.
> - `minikube --help` - which command stops a profile, and which one deletes it?
> - `kubectl taint --help` - how do you *remove* a taint?

---

## What you should be able to answer

- What does the scheduler actually *write* when it schedules a Pod?
- What is the difference between `nodeName` in the Pod spec and a `Binding` object?
- Why is there no `Scheduled` event on a Pod you bound yourself?
- Why does `kubectl apply` on a Binding print an error, and why should you not trust that error?
- Why does a `Binding` on an already-scheduled Pod fail?
- What does the API server *not* validate when you bind a Pod?
