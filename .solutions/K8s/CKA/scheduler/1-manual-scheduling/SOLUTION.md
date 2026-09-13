# Solution - Manual Scheduling with the Binding API

Verified on a 3-node minikube cluster (`minikube start -p cka --nodes 3`, Kubernetes v1.37)
with the control plane tainted. Node A is `cka-m02`, Node B is `cka-m03`.

Lab files: [K8s/CKA/scheduler/1-manual-scheduling/](../../../../../K8s/CKA/scheduler/1-manual-scheduling/).
Run every command below from **that** folder, not from here.

The approach is the one you use in the exam: open the YAML, edit it, send it with `kubectl`,
then check the result with `get -o wide` and `describe`.

## Setup

```bash
minikube start -p cka --nodes 3
kubectl config use-context cka
kubectl wait --for=condition=Ready nodes --all --timeout=180s
kubectl taint nodes cka node-role.kubernetes.io/control-plane:NoSchedule
kubectl get nodes
```

```
NAME      STATUS   ROLES           AGE   VERSION
cka       Ready    control-plane   2m    v1.37.0
cka-m02   Ready    <none>          2m    v1.37.0
cka-m03   Ready    <none>          2m    v1.37.0
```

Without the taint, the scheduler may also place Pods on `cka` in Task 1. The lab still
works, but it does not match a kubeadm cluster.

## Task 1 - Watch the scheduler do its job

```bash
kubectl apply -f scheduled-pod.yaml
kubectl get pod auto-pod -o wide
kubectl describe pod auto-pod
```

The Pod lands on `cka-m02` or `cka-m03`. At the bottom of `describe`, the first event
comes `From: default-scheduler`:

```
Events:
  Type    Reason     Age   From               Message
  Normal  Scheduled  5s    default-scheduler  Successfully assigned default/auto-pod to cka-m03
  Normal  Pulling    5s    kubelet            spec.containers{nginx}: Pulling image "nginx:1.27-alpine"
  Normal  Pulled     1s    kubelet            spec.containers{nginx}: Successfully pulled image ...
  Normal  Created    1s    kubelet            spec.containers{nginx}: Container created
  Normal  Started    0s    kubelet            spec.containers{nginx}: Container started
```

## Task 2 - Bypass the scheduler with `nodeName`

Edit `nodename-pod.yaml` and set `nodeName: cka-m02`, then:

```bash
kubectl apply -f nodename-pod.yaml
kubectl get pod nodename-pod -o wide
kubectl describe pod nodename-pod
```

```
Events:
  Type    Reason   Age   From     Message
  Normal  Pulling  5s    kubelet  spec.containers{nginx}: Pulling image "nginx:1.27-alpine"
  Normal  Pulled   0s    kubelet  spec.containers{nginx}: Successfully pulled image ...
  Normal  Created  0s    kubelet  spec.containers{nginx}: Container created
  Normal  Started  0s    kubelet  spec.containers{nginx}: Container started
```

There is **no `Scheduled` event**. Every event comes from the kubelet. The Pod arrived at
the API server already assigned, so the scheduler never looked at it.

**Bonus:** `nodeName` skips *all* scheduler logic, so taints, node selectors, affinity and
resource fit are not checked. To see it, delete the Pod, change `nodeName` to `cka`, and
apply again. The Pod runs on the tainted control plane anyway:

```bash
kubectl delete pod nodename-pod
# edit nodename-pod.yaml: nodeName: cka
kubectl apply -f nodename-pod.yaml
kubectl get pod nodename-pod -o wide    # NODE: cka
```

If the node cannot run the Pod, it fails on the node instead of staying `Pending`.

## Task 3 - Create a Pod that nobody will schedule

```bash
kubectl apply -f pending-pod.yaml
kubectl get pod pending-pod -o wide
kubectl describe pod pending-pod
kubectl get pod pending-pod -o yaml
```

- `get -o wide`: `STATUS Pending`, `NODE <none>`.
- `describe`: there is no `Conditions:` section, and the last line is `Events: <none>`.
- `-o yaml`: at the bottom, `status` only has `phase: Pending` and `qosClass: BestEffort`.

Because of `spec.schedulerName: manual-scheduler`, the default scheduler ignores the
Pod. It produces no `FailedScheduling` event, and there is no `PodScheduled` condition
at all, because nothing is watching this Pod.

## Task 4 - Bind the Pod by hand

Edit `binding.yaml` and set `target.name: cka-m02`, then:

```bash
kubectl create -f binding.yaml
```

```
status/<unknown> created
```

```bash
kubectl get pod pending-pod -o wide      # Running on cka-m02
kubectl describe pod pending-pod
kubectl get bindings
```

**The odd output:** the API server answers a Binding with a `Status` object
(`201 Created`), not with the Binding itself. kubectl prints the kind of what came back,
so you see `status/<unknown>`.

**No `Scheduled` event:** the events are only `Pulled` / `Created` / `Started` from the
kubelet. The `Scheduled` event is written by kube-scheduler after *it* binds a Pod. The
API server's binding endpoint writes no event. What the binding *does* write:

- `spec.nodeName: cka-m02` (the `Node:` line in `describe`)
- the `PodScheduled True` condition (under `Conditions:` in `describe`)

**`kubectl get bindings`:**

```
Error from server (MethodNotAllowed): the server does not allow this method on the requested resource
```

`kubectl api-resources -o wide` shows why: the only verb for `bindings` is `create`.
You can send a Binding, but you can never read one back.

## Task 5 - Repetition drill (and the `apply` trap)

```bash
kubectl apply -f rgb-pending-pods.yaml
kubectl get pods -l lab=manual-scheduling      # red / green / blue are Pending
```

Reuse `binding.yaml`. For each Pod, edit the two names and send the file again:

| Pod       | `metadata.name` | `target.name` | Command                          |
| --------- | --------------- | ------------- | -------------------------------- |
| red-pod   | `red-pod`       | `cka-m02`     | `kubectl create -f binding.yaml` |
| green-pod | `green-pod`     | `cka-m03`     | `kubectl create -f binding.yaml` |
| blue-pod  | `blue-pod`      | `cka-m02`     | `kubectl apply -f binding.yaml`  |

For `blue-pod`, `apply` prints:

```
error: object does not implement the Object interfaces
```

It looks like a failure, but check the Pods:

```bash
kubectl get pods -l lab=manual-scheduling -o wide
```

```
NAME        READY   STATUS    RESTARTS   AGE   IP            NODE      ...
blue-pod    1/1     Running   0          40s   10.244.1.11   cka-m02   ...   <- it was bound
green-pod   1/1     Running   0          40s   10.244.2.7    cka-m03   ...
red-pod     1/1     Running   0          40s   10.244.1.10   cka-m02   ...
```

Send the same file with `create` to confirm:

```bash
kubectl create -f binding.yaml
# Error from server (Conflict): error when creating "binding.yaml": Operation cannot be fulfilled
# on pods/binding "blue-pod": pod blue-pod is already assigned to node "cka-m02"
```

**What `apply` really did:** add `-v=6` to the `apply` command. Among the log lines, look
for these three:

```
GET  .../namespaces/default/bindings/blue-pod   404 Not Found   <- bindings cannot be read
POST .../namespaces/default/bindings            201 Created     <- "not found, so create it"
error: object does not implement the Object interfaces          <- the response is a Status, not a Binding
```

So `apply` binds the Pod and *then* fails while reading the response. In the exam, never
trust the error alone. Check the Pod's node, and use `kubectl create` for Bindings.

**Count Pods per node:** read the `NODE` column above, or ask for one node at a time:

```bash
kubectl get pods -l lab=manual-scheduling --field-selector spec.nodeName=cka-m02   # red, blue
kubectl get pods -l lab=manual-scheduling --field-selector spec.nodeName=cka-m03   # green
```

## Task 6 - Try to move a Pod

Edit `binding.yaml` to `metadata.name: red-pod` and `target.name: cka-m03`, then:

```bash
kubectl create -f binding.yaml
# Error from server (Conflict): error when creating "binding.yaml": Operation cannot be fulfilled
# on pods/binding "red-pod": pod red-pod is already assigned to node "cka-m02"
```

```bash
kubectl edit pod red-pod      # change spec.nodeName to cka-m03, save and quit
```

The save is rejected, and the editor opens again with the reason at the top, as a comment:

```
# pods "red-pod" was not valid:
# * spec: Forbidden: pod updates may not change fields other than `spec.containers[*].image`,
#   `spec.initContainers[*].image`,`spec.activeDeadlineSeconds`,`spec.tolerations`
#   (only additions to existing tolerations),`spec.terminationGracePeriodSeconds` ...
```

Quit without changing anything else. Nothing is applied:

```
error: pods "red-pod" is invalid
A copy of your changes has been stored to "/tmp/kubectl-edit-2945533738.yaml"
error: Edit cancelled, no valid changes were saved.
```

A scheduled Pod cannot be moved. Delete it and bind it again. `binding.yaml` already
points `red-pod` at `cka-m03`:

```bash
kubectl delete pod red-pod
kubectl apply -f rgb-pending-pods.yaml    # red-pod is Pending again, the others are unchanged
kubectl create -f binding.yaml
kubectl get pod red-pod -o wide           # NODE: cka-m03
```

## Task 7 - Bind to a node that does not exist

```bash
kubectl delete pod blue-pod
kubectl apply -f rgb-pending-pods.yaml
```

Edit `binding.yaml` to `metadata.name: blue-pod` and `target.name: cka-m04`, then:

```bash
kubectl create -f binding.yaml
# status/<unknown> created             <- accepted!

kubectl get pod blue-pod -o wide
# NAME       READY   STATUS    ...   NODE
# blue-pod   0/1     Pending   ...   cka-m04

kubectl describe pod blue-pod           # Node: cka-m04, Events: <none>
```

The binding endpoint only checks that the Pod exists and has no node yet. It does **not**
check that the node exists. The Pod is now assigned, so the scheduler will never fix it.
No kubelet watches `cka-m04`, so nothing starts it and no events appear.

```bash
kubectl delete pod blue-pod    # hangs: no kubelet is there to confirm the Pod stopped
```

Press `Ctrl+C`. The Pod garbage collector removes Pods bound to missing nodes on its own,
within about a minute. To remove it right away:

```bash
kubectl delete pod blue-pod --force --grace-period=0
```

A typo in `nodeName` or in a Binding target gives you the same stuck Pod.

## Cleanup

```bash
kubectl delete pods -l lab=manual-scheduling
kubectl taint nodes cka node-role.kubernetes.io/control-plane:NoSchedule-   # optional
minikube stop -p cka        # or: minikube delete -p cka
```

To run the lab again, put `CHANGE-ME` back in `nodename-pod.yaml` and `binding.yaml`.

## Teaching notes

- The whole point: **scheduling is just writing `spec.nodeName`.** The scheduler is an
  ordinary client that creates a Binding, and in this lab so are you. The `Scheduled`
  event is extra bookkeeping the scheduler adds, not part of the binding.
- `nodeName` is the shortcut you use when *creating* a Pod. A `Binding` is what you use for
  a Pod that **already exists** and is `Pending`.
- Without `schedulerName: manual-scheduler`, the default scheduler wins the race and there
  is nothing left to bind. That field is what makes the lab reproducible.
- Why minikube with `--nodes 3` and not fake nodes (e.g. KWOK): Task 2 and Task 4 depend on
  real kubelet events, and Task 7 depends on the difference between a real node and a
  missing one.
- Natural follow-ups for the next labs in this folder: `nodeSelector`, node affinity,
  taints and tolerations (the control-plane taint is already there), and running a second
  scheduler that actually answers to `manual-scheduler`.
