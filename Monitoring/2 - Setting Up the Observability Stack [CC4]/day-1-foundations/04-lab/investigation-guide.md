# Investigation Guide: How to Debug Using Metrics

When a failure scenario is triggered, use this guide to investigate using **only Grafana and Prometheus** (no logs).

---

## General Approach

1. **Open Grafana** (http://localhost:3000)
2. **Check the dashboard** for visual anomalies
3. **Write queries** to confirm your hypothesis
4. **Look for correlations** (when one metric changed, what else changed?)

---

## Key Kubernetes Metrics

### Pod Health

```
# Is the pod running?
kube_pod_info{pod="flask-app-xxxxx"}

# How many restarts?
kube_pod_container_status_restarts_total{pod="flask-app-xxxxx"}

# Pod status
kube_pod_status_phase{pod="flask-app-xxxxx", phase="Running"}
```

### Resource Usage

```
# CPU usage
rate(container_cpu_usage_seconds_total{pod="flask-app-xxxxx"}[5m])

# Memory usage (bytes)
container_memory_usage_bytes{pod="flask-app-xxxxx"}

# Memory percentage
container_memory_usage_bytes{pod="flask-app-xxxxx"} 
/ 
container_spec_memory_limit_bytes{pod="flask-app-xxxxx"}
* 100
```

### Pod Failures

```
# Why did it crash?
kube_pod_container_status_last_terminated_reason{pod="flask-app-xxxxx"}

# When did it restart?
kube_pod_container_status_last_terminated_timestamp{pod="flask-app-xxxxx"}
```

---

## Scenario-Specific Investigation

### High CPU Usage Scenario

**What to look for:**
1. CPU graph shows spike → Pod is using CPU
2. Request rate unchanged → CPU isn't due to traffic
3. Something in the pod is consuming CPU

**Queries:**
```
rate(container_cpu_usage_seconds_total{pod="flask-app-xxxxx"}[1m])
# See if it stays high

rate(flask_http_requests_total[5m])
# Compare request rate to CPU usage
```

---

### Out of Memory (OOMKilled) Scenario

**What to look for:**
1. Memory usage graph → Steadily increasing
2. Pod restarts → container_restarts_total increases
3. Restart reason: OOMKilled → Pod killed due to memory limit

**Queries:**
```
# Memory trend
container_memory_usage_bytes{pod="flask-app-xxxxx"}

# Restart reason
kube_pod_container_status_last_terminated_reason{pod="flask-app-xxxxx"}
# Should show: OOMKilled

# Restart count
kube_pod_container_status_restarts_total{pod="flask-app-xxxxx"}
```

---

### CrashLoopBackOff Scenario

**What to look for:**
1. Pod repeatedly crashes and restarts
2. Restart count keeps increasing
3. Pod never stays running for long

**Queries:**
```
# Restart count (increases rapidly)
kube_pod_container_status_restarts_total{pod="flask-app-xxxxx"}

# Pod status
kube_pod_status_phase{pod="flask-app-xxxxx", phase="CrashLoopBackOff"}

# Pod conditions
kube_pod_status_ready{pod="flask-app-xxxxx"}
# Should be 0 (not ready)
```

---

### Scaling Scenario

**What to look for:**
1. Pod count changes
2. New pods appear in metrics
3. Load distributed across replicas

**Queries:**
```
# Total pod count
count(kube_pod_status_phase{app="flask-app", phase="Running"})

# Request rate per pod
rate(flask_http_requests_total[5m]) by (pod)
# Should show load distributed

# CPU per pod
rate(container_cpu_usage_seconds_total{app="flask-app"}[1m]) by (pod)
```

---

## Debugging Workflow

```
1. Observe something unusual in dashboard
   ↓
2. Write query to confirm
   ↓
3. Compare with related metrics
   ↓
4. Identify correlation/cause
   ↓
5. Take action (scale, restart, etc.)
```

### Example Workflow

**Observation:** Requests are taking longer

**Step 1: Confirm latency spike**
```
rate(flask_http_request_duration_seconds_count[5m])
# Yes, latency increased
```

**Step 2: Check if it's due to traffic**
```
rate(flask_http_requests_total[5m])
# No change in request count, so not traffic-related
```

**Step 3: Check pod resources**
```
rate(container_cpu_usage_seconds_total{app="flask-app"}[1m]) by (pod)
rate(container_memory_usage_bytes{app="flask-app"}) by (pod)
# CPU and memory look normal
```

**Step 4: Check pod status**
```
kube_pod_status_phase{app="flask-app"}
# All running
```

**Step 5: Check if there are fewer pods**
```
count(kube_pod_status_phase{app="flask-app", phase="Running"})
# Count decreased! Possible pod failure
```

**Conclusion:** A pod crashed, reducing replica count. Load is now spread across fewer pods.

---

## Quick Reference Dashboard

For each scenario, monitor these panels:

| Metric | Panel Type | What It Shows |
|--------|-----------|---------------|
| Pod count | Stat | How many replicas? |
| Restarts | Counter | Is it crashing? |
| CPU usage | Graph | Is it hot? |
| Memory usage | Graph | Is it running out? |
| Request rate | Graph | Traffic volume |
| Request latency | Graph | Performance |
| Container status | Status | Health |

---

## Tips for Investigation

1. **Start broad, then zoom in**
   - First check: Pod count, CPU, Memory
   - Then: Specific pod metrics

2. **Compare with baseline**
   - Know what "normal" looks like
   - Easier to spot anomalies

3. **Look for timing correlation**
   - When did metric X change?
   - Did metric Y change at the same time?
   - Suggests cause-effect relationship

4. **Use time ranges**
   - Zoom to last 5 minutes (when did issue start?)
   - Compare to 1 hour ago (what changed?)

---

**See failure scenarios:** [failure-scenarios/](./failure-scenarios/)
