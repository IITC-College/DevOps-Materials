# Scenario 1: High CPU Usage

## Problem Description

The Flask app has a CPU-intensive endpoint. When triggered, it will consume significant CPU.

This helps you practice:
- Detecting CPU spikes in metrics
- Understanding resource contention
- Correlating high CPU with application behavior

---

## Trigger the Scenario

### Step 1: Start a background request

Open a new terminal and continuously hit the CPU-intensive endpoint:

```bash
# Start the traffic
while true; do
  curl -s http://localhost:8080/cpu-heavy &
  sleep 2
done
```

This will make repeated requests to the CPU-heavy endpoint.

### Step 2: Observe in Grafana

1. Open Grafana: http://localhost:3000
2. Go to: Dashboards → Browse → "Kubernetes / Cluster"
3. Look for: CPU panels
4. Observe:
   - CPU usage per node
   - CPU usage per pod
   - Should show spike for flask-app pods

---

## Investigation

Use these queries in Grafana to understand what's happening:

### Query 1: Pod CPU Usage
```
rate(container_cpu_usage_seconds_total{pod="flask-app-xxxxx"}[1m])
```

You should see ~0.5 cores for the CPU-heavy pod.

### Query 2: Request Rate
```
rate(flask_http_requests_total[5m])
```

Should be the same or lower than CPU spike, indicating CPU usage isn't due to traffic.

### Query 3: All Flask Pods CPU
```
rate(container_cpu_usage_seconds_total{app="flask-app"}[1m]) by (pod)
```

Shows CPU per replica. One should be higher than others.

---

## What to Observe

✅ CPU usage graph shows spike  
✅ Specific pod shows high CPU  
✅ Other pods show normal CPU (not all are affected)  
✅ Memory usage stays normal  
✅ Pod restarts: 0 (pod doesn't crash from CPU)  

---

## Questions to Answer

1. **Which pod(s) used the most CPU?**
   - Look at the `by (pod)` query results

2. **When did the CPU spike start?**
   - Note the timestamp on the graph

3. **Did the pod restart?**
   - Check `kube_pod_container_status_restarts_total`

4. **What's the difference between high CPU and normal CPU?**
   - Note the values

---

## Cleanup

Stop the background requests:

```bash
# Kill the loop (Ctrl+C in the terminal where you started it)
# OR
pkill curl
```

Verify CPU returns to normal:
- Refresh Grafana
- CPU spike should disappear

---

## Real-World Relevance

High CPU scenarios occur when:
- Code is inefficient (busy loop)
- Concurrency is too high (too many parallel requests)
- Memory is fragmented (forcing GC to work harder)
- Third-party library has a bug

**Metrics tell you:** There's high CPU.  
**Next step:** Logs tell you which code is running.  
**Final step:** Traces show you where time is spent.

---

**Next scenario:** [scenario-2-oomkilled.md](./scenario-2-oomkilled.md)
