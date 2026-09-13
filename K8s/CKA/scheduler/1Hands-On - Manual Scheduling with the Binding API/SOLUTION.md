# Solution - Manual Scheduling with the Binding API

Node names below assume a 2-worker `kind` cluster (`kind-worker`, `kind-worker2`).
Replace them with your own.

## Task 1 - Watch the scheduler do its job

```bash
kubectl apply -f 01-scheduled-pod.yaml
kubectl get pod auto-pod -o wide
kubectl describe pod auto-pod | tail -10
```

The event comes `From: default-scheduler`:

```
Normal  Scheduled  10s   default-scheduler  Successfully assigned default/auto-pod to kind-worker
```

## Task 2 - Bypass the scheduler with `nodeName`

```bash
sed -i 's/CHANGE-ME/kind-worker/' 02-nodename-pod.yaml
kubectl apply -f 02-nodename-pod.yaml
kubectl get pod nodename-pod -o wide
kubectl describe pod nodename-pod | tail -10
```

There is **no `Scheduled` event** - the first event is `Pulling`/`Pulled` from the
kubelet. The Pod arrived at the API server already assigned, so the scheduler
never looked at it.

Note: `nodeName` skips *all* scheduler logic - taints, node selectors, affinity
and resource fit are not checked. If the node cannot run the Pod, it will fail
on the node instead of staying `Pending`.

## Task 3 - Create a Pod that nobody will schedule

```bash
kubectl apply -f 03-pending-pod.yaml
kubectl get pod pending-pod        # STATUS: Pending, NODE: <none>
kubectl describe pod pending-pod | tail -5   # Events: <none>
```

`spec.schedulerName: manual-scheduler` makes the default scheduler ignore the
Pod. Not even a `FailedScheduling` event is produced - nobody is watching.

## Task 4 - Bind the Pod by hand

```bash
sed -i 's/CHANGE-ME/kind-worker/' 03-binding.yaml

kubectl apply -f 03-binding.yaml
# error: resource mapping not found ... bindings is not supported by apply

kubectl create -f 03-binding.yaml
# binding.v1/pending-pod created

kubectl get pod pending-pod -o wide      # Running on kind-worker
```

Why: the `bindings` resource only accepts `POST`
(`/api/v1/namespaces/{namespace}/bindings`). It has no `GET`, and `apply` must
read the current object before patching it.

The equivalent raw call, useful when you want to see what `create` does:

```bash
kubectl create --raw /api/v1/namespaces/default/pods/pending-pod/binding \
  -f /dev/stdin <<'JSON'
{
  "apiVersion": "v1",
  "kind": "Binding",
  "metadata": { "name": "pending-pod", "namespace": "default" },
  "target": { "apiVersion": "v1", "kind": "Node", "name": "kind-worker" }
}
JSON
```

`kubectl describe pod pending-pod` now shows a `Scheduled` event whose source is
`binding` / your user, **not** `default-scheduler`.

## Task 5 - Repetition drill

```bash
kubectl apply -f 04-rgb-pending-pods.yaml
kubectl get pods -l lab=manual-scheduling      # red/green/blue Pending

for pair in "red-pod kind-worker" "green-pod kind-worker2" "blue-pod kind-worker"; do
  set -- $pair
  cat <<YAML | kubectl create -f -
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
done

kubectl get pods -l lab=manual-scheduling -o wide
kubectl get pods -l lab=manual-scheduling \
  -o custom-columns=POD:.metadata.name,NODE:.spec.nodeName
```

## Task 6 - Try to move a Pod

```bash
cat <<'YAML' | kubectl create -f -
apiVersion: v1
kind: Binding
metadata:
  name: red-pod
  namespace: default
target:
  apiVersion: v1
  kind: Node
  name: kind-worker2
YAML
# Error from server (Conflict): pod red-pod is already assigned to node "kind-worker"
```

```bash
kubectl edit pod red-pod
# error: Pod "red-pod" is invalid: spec: Forbidden: pod updates may not change
# fields other than `spec.containers[*].image`, `spec.tolerations` (...)
```

A scheduled Pod cannot be moved. Recreate it:

```bash
kubectl delete pod red-pod
kubectl apply -f 04-rgb-pending-pods.yaml    # red-pod is Pending again
# ...then bind it to kind-worker2 as above.
```

## Cleanup

```bash
kubectl delete pods -l lab=manual-scheduling
```

## Teaching notes

- The whole point: **scheduling is just writing `spec.nodeName`.** The scheduler
  is a normal client doing a `POST` to `bindings`, and so are you in this lab.
- `nodeName` is the shortcut you use when *creating* a Pod; a `Binding` is what
  you use for a Pod that **already exists** and is `Pending`.
- Without `schedulerName: manual-scheduler`, the default scheduler wins the race
  and there is nothing left to bind - that field is what makes the lab
  reproducible.
- Natural follow-ups for the next labs in this folder: `nodeSelector`, node
  affinity, taints and tolerations, and running a second scheduler that actually
  answers to `manual-scheduler`.
