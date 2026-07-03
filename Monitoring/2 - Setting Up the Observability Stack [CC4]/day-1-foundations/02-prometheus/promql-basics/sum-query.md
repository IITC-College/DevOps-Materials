# PromQL Basic: The `sum()` Query

## What Does `sum()` Do?

**`sum()`** adds up metric values across all instances.

---

## Example

Your app runs on 5 pods:

```
http_requests_total{pod="app-1"} = 1000
http_requests_total{pod="app-2"} = 1200
http_requests_total{pod="app-3"} = 900
http_requests_total{pod="app-4"} = 1100
http_requests_total{pod="app-5"} = 800
```

### Without sum():
Result: 5 separate metrics (not useful for total)

### With sum():
```
sum(http_requests_total)
= 1000 + 1200 + 900 + 1100 + 800
= 5000 total requests
```

---

## Common Use Cases

### 1. Total Requests Across All Pods
```
sum(rate(http_requests_total[5m]))
Result: 500 total requests/sec (all pods combined)
```

### 2. Total Memory Usage
```
sum(container_memory_bytes)
Result: 5.2 GB (all containers combined)
```

### 3. Total CPU Time
```
sum(rate(container_cpu_seconds_total[5m]))
Result: 8.5 cores (all pods combined)
```

---

## Syntax

```
sum(metric_name)
→ Add all values

sum(metric_name) by (label)
→ Add all values, grouped by label
```

---

## Advanced: Group By

```
sum(http_requests_total) by (method)
Result:
  {method="GET"}  3500 requests
  {method="POST"} 1500 requests
```

```
sum(container_memory_bytes) by (pod)
Result:
  {pod="app-1"} 512MB
  {pod="app-2"} 768MB
  {pod="app-3"} 640MB
```

---

## Why It's Useful

✅ Understand total resource usage  
✅ Capacity planning  
✅ Cost calculation  
✅ SLO tracking: "Is total error rate below 0.1%?"  

---

## Real Lab Example

```
sum(rate(http_requests_total[5m]))
→ Total requests per second across all app instances

sum(container_memory_bytes) / sum(container_memory_limit_bytes) * 100
→ Total memory utilization percentage
```

---

## Combining Queries

```
sum(rate(http_errors_total[5m])) / sum(rate(http_requests_total[5m])) * 100
→ Error rate as percentage (useful for SLOs)
```

---

**See also:**
- [up-query.md](./up-query.md)
- [rate-query.md](./rate-query.md)
