# PromQL Basic: The `rate()` Query

## What Does `rate()` Do?

**`rate()`** calculates how fast a counter is increasing over time.

```
rate(http_requests_total[5m])
→ How many requests per second over the last 5 minutes?
```

---

## Real-World Example

Your app has a counter: `http_requests_total = 1,000,000`

5 minutes later: `http_requests_total = 1,000,500`

```
rate(http_requests_total[5m])
= (1,000,500 - 1,000,000) / (5 * 60 seconds)
= 500 requests / 300 seconds
= 1.67 requests/second
```

---

## Common Use Cases

### 1. Request Rate
```
rate(http_requests_total[5m])
Result: 100 requests/sec
```

### 2. Error Rate
```
rate(http_requests_failed_total[5m])
Result: 2 errors/sec
```

### 3. Traffic Trend
```
Query every 5 minutes:
  rate(http_requests_total[5m])
  
Results over time:
  10:00 → 100 req/sec
  10:05 → 150 req/sec  ← Traffic increasing
  10:10 → 200 req/sec  ← Still rising
```

---

## Syntax

```
rate(metric_name[time_window])

time_window options:
  [1m]   = last 1 minute
  [5m]   = last 5 minutes
  [1h]   = last 1 hour
  [24h]  = last 24 hours
```

---

## Why It's Useful

✅ Understand traffic patterns  
✅ Detect sudden spikes  
✅ Track error trends  
✅ Alerting: "Alert if error rate > 1%"  

---

## Real Lab Example

When you run the lab, you'll query:
```
rate(http_requests_total[5m])  → See requests per second
rate(http_errors_total[5m])    → See errors per second
```

---

## Advanced: By Labels

```
rate(http_requests_total[5m]) by (method)
Result:
  {method="GET"}  100 req/sec
  {method="POST"} 20 req/sec
```

---

**See also:**
- [up-query.md](./up-query.md)
- [sum-query.md](./sum-query.md)
