# Scenario 4: Single Pod Crashing

## Problem Description

Unlike CrashLoopBackOff (where every restart fails), this scenario simulates a single pod crashing unexpectedly. Kubernetes restarts it immediately, and it comes back healthy.

This is the most common failure: occasional crashes that self-recover.

This helps you practice:
- Detecting transient failures
- Understanding pod recovery
- Spotting brief outages in metrics

---

## Trigger the Scenario

### Step 1: Kill a pod

```bash
# Get the exact pod name
kubectl get pods -n monitoring-lab | grep flask-app

# Kill it (it will restart automatically)
kubectl delete pod -n monitoring-lab <pod-name>
```

For example:
```bash
kubectl delete pod -n monitoring-lab flask-app-abc123def456
```

### Step 2: Observe Immediately

The pod will:
1. Terminate instantly
2. Show as `Terminating`
3. Restart (new pod spawned)
4. Come back up as `Running`
5. Ready in 5-10 seconds

---

## Investigation

### Query 1: Pod Age
```
time() - kube_pod_created{pod="flask-app-xxxxx"}
```

Will show 0 seconds for the new pod (vs. hours for others).

### Query 2: Restart Count
```
kube_pod_container_status_restarts_total{pod="flask-app-xxxxx"}
```

Should increment by 1.

### Query 3: Pod Ready Status
```
kube_pod_status_ready{pod="flask-app-xxxxx"}
```

Drops to 0, then back to 1 within seconds.

### Query 4: Brief Unavailability
```
kube_deployment_status_replicas_available{deployment="flask-app"}
```

Should dip below expected replicas for a moment.

### Query 5: Request Errors During Outage
```
rate(flask_http_requests_failed_total[1m])
```

Might spike if requests hit during restart.

---

## What to Observe

✅ Pod restarts cleanly  
✅ Restart count increments by 1  
✅ Pod becomes ready within 10 seconds  
✅ New pod has young age  
✅ Brief spike in request errors (if any traffic was hitting it)  
✅ Deployment stays available (other replica handles load)  

---

## Questions to Answer

1. **How long was the pod unavailable?**

2. **Did requests fail during the outage?**
   - Yes, if all replicas went down
   - No, if other replicas were still running

3. **How did you know a pod crashed?**
   - Restart count increased?
   - Pod age reset?
   - Ready status dropped?

4. **Did your SLO survive?**
   - If you had 2 replicas, no downtime observed
   - If you had 1 replica, you saw brief errors

---

## Cleanup

Nothing needed! The pod recovered automatically.

Monitor for 1-2 minutes to ensure it stays healthy.

---

## Real-World Relevance

Single pod crashes occur when:
- Memory corruption (rare, usually a C library)
- Segmentation fault (rare, usually a native extension)
- Timeout in cleanup (pod gets slow shutting down)
- External signal sent (accidentally, or by orchestrator)

Good news: **Kubernetes auto-restarts**. This is why we run multiple replicas!

**Metrics tell you:** One pod restarted.  
**SLO impact:** None (if you have 2+ replicas).  
**Action:** Investigate only if it happens repeatedly.

---

**Next scenario:** [scenario-5-scaling.md](./scenario-5-scaling.md)
