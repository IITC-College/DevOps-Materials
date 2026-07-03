# Scenario 2: OOMKilled (Out of Memory)

## Problem Description

The Flask app has an endpoint that allocates memory and keeps it. When triggered repeatedly, it will exhaust the memory limit and the Kubernetes OOMKiller will terminate the pod.

This helps you practice:
- Detecting memory leaks
- Understanding pod restarts due to OOM
- Recognizing termination reasons in metrics

---

## Trigger the Scenario

### Step 1: Start memory-intensive requests

```bash
# Allocate memory multiple times
for i in {1..10}; do
  curl -s http://localhost:8080/memory-leak &
  sleep 1
done
```

This will make requests that allocate ~100MB each, eventually hitting the 512MB limit.

### Step 2: Observe in Grafana

1. Open Grafana: http://localhost:3000
2. Watch memory panels
3. Observe:
   - Memory usage climbing
   - Eventually hitting the limit
   - Pod restarting
   - Restart counter incrementing

---

## Investigation

### Query 1: Memory Usage Trend
```
container_memory_usage_bytes{pod="flask-app-xxxxx"}
```

Watch this climb until it hits the limit (~512MB).

### Query 2: Memory Limit
```
container_spec_memory_limit_bytes{pod="flask-app-xxxxx"}
```

Should be 512MB (512 * 1024 * 1024 bytes).

### Query 3: Memory Percentage
```
container_memory_usage_bytes{pod="flask-app-xxxxx"}
/
container_spec_memory_limit_bytes{pod="flask-app-xxxxx"}
* 100
```

Should climb to 100%.

### Query 4: Restart Reason
```
kube_pod_container_status_last_terminated_reason{pod="flask-app-xxxxx"}
```

Should show: `OOMKilled`

### Query 5: Restart Count
```
kube_pod_container_status_restarts_total{pod="flask-app-xxxxx"}
```

Should increment each time pod is killed.

---

## What to Observe

✅ Memory usage graph shows steady increase  
✅ Memory reaches 100% of limit  
✅ Pod restarts (kube_pod_status_ready drops to 0, then back to 1)  
✅ Restart count increments  
✅ Last termination reason shows: `OOMKilled`  
✅ CPU drops back to normal (pod restarted)  

---

## Questions to Answer

1. **When did memory usage start increasing?**

2. **How high did it climb before restart?**

3. **How many times did the pod restart?**

4. **What was the termination reason?**

5. **Did other pods in the deployment stay healthy?**

---

## Cleanup

The pod will automatically recover after each restart. The memory leak endpoints will continue failing, so:

1. Stop any running requests
2. Monitor: Pod should stabilize after 1-2 minutes

---

## Real-World Relevance

OOMKilled scenarios occur when:
- Memory leak in application (holding references)
- Cache growing without bounds
- Request buffering without cleanup
- Third-party library has a leak

**Metrics tell you:** Pod was OOMKilled.  
**Logs tell you:** Which allocation triggered it.  
**Fix:** Find and plug the leak.

---

**Next scenario:** [scenario-3-crashloopbackoff.md](./scenario-3-crashloopbackoff.md)
