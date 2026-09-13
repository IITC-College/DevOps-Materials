# Solution - Manual Scheduling with the Binding API

Verified on a 3-node minikube cluster (`minikube start -p cka --nodes 3`, Kubernetes v1.37)
with the control plane tainted. Node A is `cka-m02`, Node B is `cka-m03`.

Lab files: [K8s/CKA/scheduler/1-manual-scheduling/](../../../../../K8s/CKA/scheduler/1-manual-scheduling/).
Run every command below from **that** folder, not from here.

The commands below use `sed ... | kubectl ... -f -` to fill in `CHANGE-ME` without editing the
files. It works with both macOS and GNU `sed`, and the YAML stays reusable.

## Setup

```bash
minikube start -p cka --nodes 3 --driver=docker
kubectl config use-context cka
kubectl wait --for=condition=Ready node --all --timeout=180s
kubectl taint node cka node-role.kubernetes.io/control-plane:NoSchedule
```

Without the taint, the scheduler may also place Pods on `cka` in Task 1. The lab still
works, but it does not match a kubeadm cluster.

## Task 1 - Watch the scheduler do its job

```bash
kubectl apply -f scheduled-pod.yaml
kubectl get pod auto-pod -o wide
kubectl describe pod auto-pod | sed -n '/Events:/,$p'
```

The Pod lands on `cka-m02` or `cka-m03`. The first event comes `From: default-scheduler`:

```
Type    Reason     Age   From               Message
Normal  Scheduled  5s    default-scheduler  Successfully assigned default/auto-pod to cka-m03
Normal  Pulling    5s    kubelet            spec.containers{nginx}: Pulling image "nginx:1.27-alpine"
Normal  Pulled     1s    kubelet            spec.containers{nginx}: Successfully pulled image ...
Normal  Created    1s    kubelet            spec.containers{nginx}: Container created
Normal  Started    0s    kubelet            spec.containers{nginx}: Container started
```

## Task 2 - Bypass the scheduler with `nodeName`

```bash
sed 's/CHANGE-ME/cka-m02/' nodename-pod.yaml | kubectl apply -f -
kubectl get pod nodename-pod -o wide
kubectl describe pod nodename-pod | sed -n '/Events:/,$p'
```

```
Type    Reason   Age   From     Message
Normal  Pulling  5s    kubelet  spec.containers{nginx}: Pulling image "nginx:1.27-alpine"
Normal  Pulled   0s    kubelet  spec.containers{nginx}: Successfully pulled image ...
Normal  Created  0s    kubelet  spec.containers{nginx}: Container created
Normal  Started  0s    kubelet  spec.containers{nginx}: Container started
```

There is **no `Scheduled` event**. Every event comes from the kubelet. The Pod arrived at
the API server already assigned, so the scheduler never looked at it.

Note: `nodeName` skips *all* scheduler logic, so taints, node selectors, affinity and resource
fit are not checked. Try `sed 's/CHANGE-ME/cka/'` and the Pod runs on the tainted control
plane anyway. If the node cannot run the Pod, it fails on the node instead of staying `Pending`.

## Task 3 - Create a Pod that nobody will schedule

```bash
kubectl apply -f pending-pod.yaml
kubectl get pod pending-pod -o wide                    # STATUS: Pending, NODE: <none>
kubectl describe pod pending-pod | tail -1             # Events: <none>
kubectl get pod pending-pod -o jsonpath='{.status}'    # {"phase":"Pending","qosClass":"BestEffort"}
```

Because of `spec.schedulerName: manual-scheduler`, the default scheduler ignores the
Pod. It produces no `FailedScheduling` event, and there is no `PodScheduled` condition
at all, because nothing is watching this Pod.

## Task 4 - Bind the Pod by hand

```bash
sed 's/CHANGE-ME/cka-m02/' binding.yaml | kubectl create -f -
# status/<unknown> created

kubectl get pod pending-pod -o wide      # Running on cka-m02
kubectl describe pod pending-pod
```

**The odd output:** the API server answers a Binding `POST` with a `Status` object
(`201 Created`), not with the Binding. kubectl prints the kind of what came back, so you
see `status/<unknown>`.

**No `Scheduled` event:** the events are only `Pulled` / `Created` / `Started` from the
kubelet. The `Scheduled` event is emitted by kube-scheduler after *it* binds a Pod. The
API server's binding endpoint writes no event. What the binding endpoint *does* write:

- `spec.nodeName: cka-m02`
- the `PodScheduled: True` condition (visible under `Conditions:` in `describe`)

**`kubectl get bindings`:**

```
Error from server (MethodNotAllowed): the server does not allow this method on the requested resource
```

`bindings` only supports `create`, which is `POST` to
`/api/v1/namespaces/{namespace}/bindings` (or `/pods/{name}/binding`). The equivalent raw
call:

```bash
kubectl create --raw /api/v1/namespaces/default/pods/pending-pod/binding \
  -f /dev/stdin <<'JSON'
{
  "apiVersion": "v1",
  "kind": "Binding",
  "metadata": { "name": "pending-pod", "namespace": "default" },
  "target": { "apiVersion": "v1", "kind": "Node", "name": "cka-m02" }
}
JSON
```

## Task 5 - Repetition drill (and the `apply` trap)

A small helper saves typing:

```bash
bindpod() {  # usage: bindpod <pod> <node> [create|apply]
  cat <<YAML | kubectl "${3:-create}" -f -
apiVersion: v1
kind: Binding
metadata:
  name: $1
  namespace: default
target:
  apiVersion: v1
  kind: Node
  name: $2
YAML
}
```

```bash
kubectl apply -f rgb-pending-pods.yaml
kubectl get pods -l lab=manual-scheduling      # red/green/blue Pending

bindpod red-pod   cka-m02
bindpod green-pod cka-m03
bindpod blue-pod  cka-m02 apply
# error: object does not implement the Object interfaces
```

It looks like a failure, but check the Pod:

```bash
kubectl get pods -l lab=manual-scheduling \
  -o custom-columns=POD:.metadata.name,NODE:.spec.nodeName
```

```
POD          NODE
blue-pod     cka-m02      <- it was bound
green-pod    cka-m03
red-pod      cka-m02
```

Retrying with `create` proves it: `409 Conflict ... already assigned to node "cka-m02"`.

What `apply` actually did (`kubectl apply -v=6`):

```
GET  /api/v1/namespaces/default/bindings/blue-pod   404 Not Found   <- no GET on bindings
POST /api/v1/namespaces/default/bindings            201 Created     <- "not found, so create it"
error: object does not implement the Object interfaces              <- response is a Status, not a Binding
```

So `apply` binds the Pod and *then* errors while reading the response. In the exam, never
trust the error alone. Check `spec.nodeName`, and use `kubectl create` for Bindings.

Count Pods per node:

```bash
kubectl get pods -l lab=manual-scheduling -o jsonpath='{range .items[*]}{.spec.nodeName}{"\n"}{end}' \
  | sort | uniq -c
```

## Task 6 - Try to move a Pod

```bash
bindpod red-pod cka-m03
# Error from server (Conflict): error when creating "STDIN": Operation cannot be fulfilled on
# pods/binding "red-pod": pod red-pod is already assigned to node "cka-m02"
```

```bash
kubectl edit pod red-pod      # change spec.nodeName, save
# The Pod "red-pod" is invalid: spec: Forbidden: pod updates may not change fields other than
# `spec.containers[*].image`,`spec.initContainers[*].image`,`spec.activeDeadlineSeconds`,
# `spec.tolerations` (only additions to existing tolerations), ...
```

A scheduled Pod cannot be moved. Recreate it:

```bash
kubectl delete pod red-pod
kubectl apply -f rgb-pending-pods.yaml    # red-pod is Pending again, the others are unchanged
bindpod red-pod cka-m03
```

## Task 7 - Bind to a node that does not exist

```bash
kubectl delete pod blue-pod
kubectl apply -f rgb-pending-pods.yaml
bindpod blue-pod cka-m04
# status/<unknown> created             <- accepted!

kubectl get pod blue-pod -o wide
# NAME       READY   STATUS    NODE
# blue-pod   0/1     Pending   cka-m04
```

The binding endpoint only checks that the Pod exists and has no node yet. It does **not**
check that the node exists. The Pod is now assigned, so the scheduler will never fix it.
No kubelet watches `cka-m04`, so nothing starts it and no events appear.

```bash
kubectl delete pod blue-pod    # hangs: no kubelet is there to confirm the Pod stopped
```

The Pod garbage collector deletes Pods bound to missing nodes on its own, within about a
minute. To remove it immediately:

```bash
kubectl delete pod blue-pod --force --grace-period=0
```

A typo in `nodeName` or in a Binding target gives you the same stuck Pod.

## Cleanup

```bash
kubectl delete pods -l lab=manual-scheduling
kubectl taint node cka node-role.kubernetes.io/control-plane:NoSchedule-   # optional
minikube stop -p cka
```

## Teaching notes

- The whole point: **scheduling is just writing `spec.nodeName`.** The scheduler is an
  ordinary client that sends a `POST` to `bindings`, and in this lab so are you. The
  `Scheduled` event is extra bookkeeping the scheduler adds, not part of the binding.
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
