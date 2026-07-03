# Solution 2: The Slow Spiral

## Expected Answer

**Affected metric:** Memory usage (steadily increasing) OR Request latency (increases over time)

**Start time:** When you started the memory leak requests

**Resource issue:** Memory exhaustion (memory limit approached)

**Suspected cause:** Memory leak in application (memory-leak endpoint keeps 100MB)

---

## How to Find This in Grafana

### Step 1: Spot the latency increase

Query:
```
rate(flask_http_request_duration_seconds_count[5m])
```

Or look at graph:
```
histogram_quantile(0.95, rate(flask_http_request_duration_seconds_bucket[5m]))
```

Result: Latency climbs from ~50ms to 100-200ms over time.

### Step 2: Correlate with memory

Query:
```
container_memory_usage_bytes{pod="flask-app-xxxxx"}
/
container_spec_memory_limit_bytes{pod="flask-app-xxxxx"}
* 100
```

Result: Memory % climbs from ~10% to 90-100% over same time window.

### Step 3: Rule out traffic volume

Query:
```
rate(flask_http_requests_total[5m])
```

Result: Request rate stays constant. It's NOT because of more traffic.

### Step 4: Predict the crash

Query:
```
container_memory_usage_bytes{pod="flask-app-xxxxx"}
```

Result: Memory reaches limit (512MB), pod gets OOMKilled.

---

## The Story

1. App starts with ~50MB memory
2. Each `/memory-leak` request allocates 100MB
3. Memory isn't freed (it's held in the list)
4. Pod memory climbs: 50→150→250→350→450→512MB
5. At 512MB, Kubernetes kills it (OOMKilled)
6. Pod restarts with fresh memory
7. Cycle repeats

---

## Key Insights

✅ **Latency ≠ Traffic** — They're not always correlated.

✅ **Memory leaks are sneaky** — Gradual increase is hard to spot without graphs.

✅ **Time series databases shine here** — Trends over time are instant to see.

✅ **Prediction is possible** — You could set an alert at 80% memory to warn before crash.

---

## Alerts You'd Set

```
Alert: Pod memory high
Condition: container_memory_usage_bytes > container_spec_memory_limit_bytes * 0.8
For: 2 minutes
Action: Scale up, or alert on-call
```

```
Alert: Pod latency increasing
Condition: rate(latency[5m]) > baseline * 1.5
For: 5 minutes
Action: Investigate, maybe restart pod
```

---

## Common Mistakes

❌ "CPU is high" — No, CPU is normal. Memory is the issue.

❌ "Requests are increasing" — No, request rate is constant. It's not a traffic spike.

❌ "The pod crashed immediately" — No, it gradually degraded then crashed.

---

**Next scenario:** [solution-3.md](./solution-3.md)
