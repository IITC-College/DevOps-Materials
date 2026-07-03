# Scenario 3: CrashLoopBackOff

## Problem Description

When a pod fails to start (or crashes immediately), Kubernetes enters a crash loop. It tries to restart, fails again, waits longer, tries again, and so on.

This helps you practice:
- Detecting unhealthy pods
- Understanding restart exponential backoff
- Correlating multiple restart cycles

---

## Trigger the Scenario

### Step 1: Modify deployment to crash

```bash
# This kills the main Flask process
kubectl exec -n monitoring-lab deployment/flask-app -- kill 1
```

Or manually scale the deployment down and back up:

```bash
kubectl scale deployment flask-app -n monitoring-lab --replicas=0
```

Edit the deployment to break it:
```bash
kubectl edit deployment flask-app -n monitoring-lab
```

Change `command` to something invalid that crashes:
```yaml
spec:
  containers:
  - name: flask-app
    image: flask-app:latest
    command: ["false"]  # This command immediately exits with error
```

### Step 2: Observe in Grafana

1. Pod status should show: `CrashLoopBackOff`
2. Ready count should be 0
3. Restart count should keep increasing

---

## Investigation

### Query 1: Pod Status
```
kube_pod_status_phase{pod="flask-app-xxxxx"}
```

Should show: `CrashLoopBackOff` (or transitions between `Pending` and `CrashLoopBackOff`)

### Query 2: Pod Ready Status
```
kube_pod_status_ready{pod="flask-app-xxxxx"}
```

Should be 0 (pod is not ready).

### Query 3: Restart Count
```
kube_pod_container_status_restarts_total{pod="flask-app-xxxxx"}
```

Should keep incrementing as Kubernetes retries.

### Query 4: Termination Reason
```
kube_pod_container_status_last_terminated_reason{pod="flask-app-xxxxx"}
```

Should show: `Error` or `ContainerCannotRun`

### Query 5: Available Replicas
```
kube_deployment_status_replicas_available{deployment="flask-app"}
```

Should be 0 or very low.

---

## What to Observe

✅ Pod status shows: CrashLoopBackOff  
✅ Ready count: 0 of N replicas  
✅ Restart count: Keeps increasing  
✅ Restart backoff: Wait times increase (1s, 2s, 4s, 8s, ...)  
✅ No requests being handled (traffic returns errors)  
✅ Errors spike in metrics  

---

## Questions to Answer

1. **How many times did the pod restart in 5 minutes?**

2. **What's the pattern of restarts (timing)?**

3. **When did you realize the deployment was broken?**
   - Was it the available replicas dropping to 0?
   - Or the error rate spiking?

4. **How many healthy replicas were serving traffic?**

---

## Cleanup

Fix the deployment:

```bash
# Scale back up (if you scaled down)
kubectl scale deployment flask-app -n monitoring-lab --replicas=2

# OR fix the deployment
kubectl edit deployment flask-app -n monitoring-lab
# Change command back to normal
# Remove the command line or restore it
```

Watch metrics return to normal.

---

## Real-World Relevance

CrashLoopBackOff occurs when:
- Configuration is wrong (missing env vars, bad config file)
- Code has a startup error (imports failed, syntax error)
- Service can't reach dependencies (database, cache)
- Resource limits are too low to start

**Metrics tell you:** Pod is in CrashLoopBackOff.  
**Logs tell you:** Startup error message.  
**Fix:** Address the root cause (config, code, dependencies).

---

**Next scenario:** [scenario-4-pod-crashing.md](./scenario-4-pod-crashing.md)
