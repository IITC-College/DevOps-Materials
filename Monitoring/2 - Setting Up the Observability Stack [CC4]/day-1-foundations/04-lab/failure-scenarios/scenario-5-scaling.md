# Scenario 5: Scaling (Horizontal Pod Autoscaling)

## Problem Description

Scale the deployment up and down, observing how metrics change:
- Pod count increases/decreases
- Load distributes across replicas
- Metrics reflect the changes

This helps you practice:
- Understanding load distribution
- Monitoring capacity changes
- Correlating deployment changes with metrics

---

## Trigger the Scenario

### Step 1: Scale Up

```bash
# Current replicas (should be 2)
kubectl get deployment flask-app -n monitoring-lab

# Scale to 4 replicas
kubectl scale deployment flask-app -n monitoring-lab --replicas=4
```

### Step 2: Observe New Pods Starting

```bash
# Watch pods come up
kubectl get pods -n monitoring-lab -w
# Press Ctrl+C to stop watching
```

### Step 3: Generate Traffic

```bash
# Steady traffic across all pods
for i in {1..1000}; do
  curl -s http://localhost:8080/ > /dev/null
  sleep 0.1
done &
```

### Step 4: Scale Down

After observing the scaled-up state:

```bash
kubectl scale deployment flask-app -n monitoring-lab --replicas=2
```

Watch as pods terminate and load shifts.

---

## Investigation

### Query 1: Pod Count
```
count(kube_pod_status_phase{app="flask-app", phase="Running"})
```

Should jump from 2 → 4 → 2 as you scale.

### Query 2: Available Replicas
```
kube_deployment_status_replicas_available{deployment="flask-app"}
```

Reflects actual replicas ready to serve traffic.

### Query 3: Request Rate Per Pod (Scale Up)
```
rate(flask_http_requests_total[1m]) by (pod)
```

Before scaling: 2 pods each get ~500 req/s (1000 total)  
After scaling: 4 pods each get ~250 req/s (1000 total)  
Load evenly distributed!

### Query 4: CPU Per Pod (Scale Up)
```
rate(container_cpu_usage_seconds_total{app="flask-app"}[1m]) by (pod)
```

CPU per pod decreases as load distributes.

### Query 5: Total Pod CPU (Should Stay Same)
```
sum(rate(container_cpu_usage_seconds_total{app="flask-app"}[1m]))
```

Total CPU effort stays the same, but spread across more pods.

### Query 6: Memory Per Pod
```
container_memory_usage_bytes{app="flask-app"} by (pod)
```

New pods have low memory (just started).

---

## What to Observe

**When scaling UP (2 → 4):**
✅ Pod count increases  
✅ New pods appear in metrics  
✅ Pod ages vary (new ones are young)  
✅ Request rate per pod decreases  
✅ CPU per pod decreases  
✅ Total system CPU stays ~same  

**When scaling DOWN (4 → 2):**
✅ Pod count decreases  
✅ Pods terminate gracefully  
✅ Request rate per pod increases  
✅ CPU per pod increases  
✅ Remaining pods handle more load  

---

## Questions to Answer

1. **How long did it take new pods to become ready?**
   - Check timestamp when pod count changed

2. **How did load distribution change after scaling up?**
   - Compare request rates before/after

3. **Was there any downtime during scale-down?**
   - No, if requests were balanced
   - Yes, if you had only 1 replica

4. **What's the relationship between replica count and latency?**
   - More replicas → better latency (less queuing)
   - Fewer replicas → higher latency (more queuing)

---

## Cleanup

Reset to normal:

```bash
kubectl scale deployment flask-app -n monitoring-lab --replicas=2
```

Stop any background traffic generation.

---

## Real-World Relevance

Scaling scenarios are common when:
- Traffic increases (auto-scaler kicks in)
- Planned maintenance (scale up for safety, then update, then scale down)
- Cost optimization (scale down during low traffic)
- Rolling updates (scale up, then roll, then scale down)

**Benefits of monitoring scaling:**
- Verify load is distributed correctly
- Detect if autoscaler is working
- Spot pods that crash during scale-down
- Monitor cascading failures (if scaling triggers other issues)

**Metrics to alert on:**
- Pod count < expected
- Replica unavailable
- Pending pods not becoming ready

---

## Advanced: Autoscaling

This lab uses manual scaling. In production, use Horizontal Pod Autoscaler (HPA):

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: flask-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: flask-app
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

HPA automatically scales based on metrics!

---

**Scenarios complete!** → [../../final-exercise/](../../final-exercise/)
