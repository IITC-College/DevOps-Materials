# Solution 1: The Quiet Restart

## Expected Answer

**Pod name:** `flask-app-<random>` (the one you deleted)

**Restart count:** Should have incremented by 1 (0→1, or 1→2, etc.)

**Reason:** `Normal` (clean restart, no error)

**Root cause:** Pod was intentionally deleted (or natural eviction)

---

## How to Find This in Grafana

### Step 1: Find the restarted pod

Query:
```
kube_pod_container_status_restarts_total{app="flask-app"}
```

Result: Shows one pod with a higher restart count than others.

### Step 2: Check the pod's age

Query:
```
time() - kube_pod_created{pod="flask-app-xxxxx"}
```

Result: New pod shows low age (minutes), old pods show hours.

### Step 3: Find the reason

Query:
```
kube_pod_container_status_last_terminated_reason{pod="flask-app-xxxxx"}
```

Result: Should show `ContainerStatusUnknown` (for deletion) or `Error` if it crashed.

---

## Key Insights

✅ **Kubernetes auto-restarts terminated pods** — This is expected behavior.

✅ **Restart count is cumulative** — Never resets (unless pod is deleted).

✅ **Age resets on restart** — Compare pod age to restart count.

✅ **Reason tells the story** — `Error` vs `Normal` tells you if it crashed.

---

## Common Mistakes

❌ "Both pods restarted" — No, only one changed restart count.

❌ "It was OOMKilled" — Check the reason field carefully.

❌ "The pod is down" — No, Kubernetes auto-restarted it. Both replicas are serving traffic.

---

## If You Got It Wrong

If you identified a different pod or wrong reason:

1. **Check pod labels** — Make sure you're querying the right deployment
2. **Check timestamps** — When did the restart happen? Correlate to when you deleted the pod
3. **Look at multiple pods** — Compare restart counts across all replicas

---

**Next scenario:** [solution-2.md](./solution-2.md)
