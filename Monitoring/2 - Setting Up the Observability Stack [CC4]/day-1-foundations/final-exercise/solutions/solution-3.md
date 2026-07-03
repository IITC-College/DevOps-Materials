# Solution 3: The Cascading Failure

## Expected Answer

**Primary failure:** Pod crashes (CrashLoopBackOff) due to corrupted command

**Cascading effect:** Other pod is stressed (higher CPU, higher latency) from handling all traffic

**Root cause chain:**
1. Deployment is broken (bad command)
2. All new pods fail to start
3. Existing replica(s) are still running, handling traffic
4. One pod now receives ALL traffic (2x or more)
5. Latency increases, CPU spikes
6. Eventually, the remaining pod might crash from overload

---

## How to Find This in Grafana

### Step 1: Spot the crash loop

Query:
```
kube_pod_status_phase{app="flask-app"}
```

Result: New pods show `CrashLoopBackOff`, existing pods show `Running`.

### Step 2: Check available replicas

Query:
```
kube_deployment_status_replicas_available{deployment="flask-app"}
```

Result: Drops from 2 to 1 (or whatever your scale was).

### Step 3: Monitor request rate per pod

Query:
```
rate(flask_http_requests_total[1m]) by (pod)
```

Result:
- Before: Both pods get ~50% of traffic each (500 req/s each)
- After: Surviving pod gets 100% of traffic (1000 req/s)
- New pods: Never start, so no traffic

### Step 4: Check latency impact

Query:
```
rate(flask_http_request_duration_seconds_count[5m])
```

Result: Latency increases as single pod is overloaded.

### Step 5: Monitor the surviving pod's CPU

Query:
```
rate(container_cpu_usage_seconds_total{pod="flask-app-xxxxx"}[1m])
```

Result: CPU spikes (pod is working harder to handle all traffic).

---

## The Cascading Story

```
Time 1: Deployment is broken
  → Kubernetes tries to replace old pods
  → New pods fail to start (CrashLoopBackOff)
  → Old pods still running (still serving traffic)

Time 2: Traffic shifts
  → Old pods must now handle ALL traffic
  → Request rate per pod doubles
  → CPU per pod doubles
  → Latency increases

Time 3: Overload risk
  → If load is too high, surviving pods might:
    - Crash from resource exhaustion
    - Become slow (affecting customers)
    - Cascade to other services

Time 4: Fix
  → Fix the deployment
  → New pods start successfully
  → Load redistributes
  → Latency drops
```

---

## Key Insights

✅ **Cascading failures are the worst** — One problem causes another.

✅ **Redundancy only helps if both replicas are healthy** — 1 pod + 0 pods ≠ resilience.

✅ **Early detection is critical** — Alert on "available replicas < desired replicas"

✅ **Metric correlation tells the story** — Pod crash + request rate change + latency spike = cascading failure.

---

## Alerts to Prevent This

```
Alert: Pod CrashLoopBackOff
Condition: kube_pod_status_phase == "CrashLoopBackOff"
For: 1 minute
Action: Page on-call immediately

Alert: Replicas unavailable
Condition: kube_deployment_status_replicas_available < kube_deployment_spec_replicas
For: 2 minutes
Action: Page on-call, check logs

Alert: High latency with low replica count
Condition: (latency > baseline) AND (replicas_available < replicas_desired)
Action: Emergency page
```

---

## Recovery Metrics

When you fix the deployment:

1. **Watch new pods start:** kube_pod_status_phase transitions to Running
2. **Available replicas increase:** kube_deployment_status_replicas_available rises
3. **Load redistributes:** rate(requests)[pod] decreases per pod
4. **Latency recovers:** Request duration drops
5. **CPU normalizes:** Per-pod CPU usage drops

---

## Common Mistakes

❌ "Both pods crashed" — No, old pods were still running. Only new pods failed.

❌ "Latency spiked because of traffic increase" — No, request rate was constant. It's because of pod failure.

❌ "The problem fixed itself" — No, you had to manually fix the deployment.

❌ "This wouldn't happen in production" — **It happens all the time!** This is why redundancy, monitoring, and alerts matter.

---

## Bonus: Defense in Depth

To prevent cascading failures:

1. **Readiness probes** — Don't send traffic to unhealthy pods
2. **Multiple replicas** — If one dies, others can handle it (barely)
3. **Circuit breakers** — If load is too high, reject gracefully
4. **Alerts** — Know IMMEDIATELY when a replica fails
5. **Auto-restart** — Kubernetes does this automatically (but monitor it!)
6. **Resource limits** — Ensure pods don't use more than their fair share
7. **Load testing** — Know how much load a single pod can handle

---

**Congratulations on completing the final exercise!** 🎉

You've learned to think like an SRE: **Observability + Metrics + Alerts = Reliability**.

---

**Next:** [../../README.md](../../README.md) — Reflect on Day 1, then move to Day 2 (Alerts & Logs)
