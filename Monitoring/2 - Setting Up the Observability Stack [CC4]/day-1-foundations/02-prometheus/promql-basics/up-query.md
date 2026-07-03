# PromQL Basic: The `up` Query

## What Does `up` Mean?

The **`up`** metric tells you if a service is **running** or **down**.

```
up{job="prometheus"} = 1    → Service is running ✅
up{job="prometheus"} = 0    → Service is down ❌
```

---

## Usage Examples

### Check If Prometheus Itself is Running
```
up{job="prometheus"}
Result: 1
```

### Check All Pods in a Namespace
```
up{job="kubernetes-pods", namespace="default"}
Result:
  up{pod="api-server-1", namespace="default"} 1
  up{pod="api-server-2", namespace="default"} 1
  up{pod="db-replica-1", namespace="default"} 0  ← This one is down!
```

### Count Running Services
```
count(up == 1)
Result: 42  (42 services are running)
```

### Find Down Services
```
up == 0
Result:
  up{pod="db-replica-1"} 0
```

---

## Why It's Useful

✅ Quick health check  
✅ Detect crashes immediately  
✅ Alert when services go down  
✅ Monitor redundancy (all replicas running?)  

---

## Alerting Example

In Prometheus alert rules (tomorrow):
```yaml
alert: ServiceDown
expr: up == 0
for: 1m
annotations:
  summary: "Service {{ $labels.pod }} is down!"
```

---

**See also:**
- [rate-query.md](./rate-query.md)
- [sum-query.md](./sum-query.md)
