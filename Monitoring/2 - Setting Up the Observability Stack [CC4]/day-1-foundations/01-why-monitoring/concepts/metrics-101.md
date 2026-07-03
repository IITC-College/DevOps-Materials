# Metrics 101: What Are Metrics?

## Simple Definition

A **metric** is a number that changes over time.

```
Metric = Measurement + Timestamp

Example:
  Timestamp: 2026-07-03 14:23:45
  Metric: cpu_usage = 42%

Next second:
  Timestamp: 2026-07-03 14:23:46
  Metric: cpu_usage = 45%
```

---

## Types of Metrics

### 1. Gauge (Current Value)
A metric that goes up and down.

**Examples:**
- CPU usage: `42%`
- Memory used: `512 MB`
- Active connections: `127`
- Pod count: `5`

**Analogy:** Like a gas gauge in your car. It shows the current level.

```
Prometheus Format:
  cpu_usage_percent{instance="server-1"} 42
```

---

### 2. Counter (Always Increasing)
A metric that only goes up (or resets).

**Examples:**
- Total requests served: `1,000,000` (never decreases)
- Errors since startup: `42` (only increases)
- Bytes downloaded: `50 GB` (only increases)

**Analogy:** Like an odometer. It only counts forward.

```
Prometheus Format:
  http_requests_total{method="GET"} 1000000
```

---

### 3. Histogram (Distribution)
A metric that tracks the distribution of values.

**Example:** Request latency
- 50% of requests: < 50ms
- 90% of requests: < 200ms
- 99% of requests: < 500ms

**Use case:** Understanding performance percentiles.

```
Prometheus Format:
  http_request_duration_seconds_bucket{le="0.05"} 500
  http_request_duration_seconds_bucket{le="0.2"} 4500
  http_request_duration_seconds_bucket{le="0.5"} 4950
```

---

### 4. Summary (Quantiles)
Similar to histogram, but calculates percentiles on the client side.

**Example:** Database query time
- 50th percentile: 100ms
- 95th percentile: 200ms
- 99th percentile: 500ms

---

## How Metrics Help You

### 1. Know Your System's State
```
Question: "Is my database healthy?"
Answer (from metrics): "CPU: 45%, Memory: 60%, Connections: 120/300"
```

### 2. Spot Problems Fast
```
Question: "Why is the app slow?"
Answer (from metrics): "Load balancer CPU: 95%, requests: 10k/sec"
→ Need to scale horizontally
```

### 3. Make Decisions
```
Question: "Should we upgrade our server?"
Answer (from metrics): "CPU has been 80-90% for 3 weeks"
→ Yes, upgrade needed
```

### 4. Build Dashboards
```
You see: CPU, Memory, Request Rate, Error Rate
You understand: Everything at a glance
You act: Quickly, with confidence
```

---

## Common Kubernetes Metrics

Here are metrics you'll see in the lab:

| Metric | Meaning | Example |
|--------|---------|---------|
| `container_cpu_usage_seconds_total` | CPU time used | Increases as pod uses CPU |
| `container_memory_usage_bytes` | RAM used by container | 256MB, 512MB, etc. |
| `kubelet_running_pods` | Number of pods on node | 20 pods |
| `kubelet_pod_worker_duration_seconds` | Time to start pod | 5.2 seconds |
| `http_requests_total` | Total HTTP requests | 1,000,000 (counter) |
| `http_request_duration_seconds` | Request latency | 0.05s, 0.1s, 0.5s |

---

## Why Metrics (Not Logs)?

When you need **quick answers**:

| Question | Metrics | Logs |
|----------|---------|------|
| "Is it slow?" | ✅ Instant | ❌ Search all logs |
| "How many errors?" | ✅ One number | ❌ Count matching lines |
| "Trend over time?" | ✅ Graph | ❌ Tedious |
| "Alert me if bad?" | ✅ Simple | ❌ Complex |

Metrics are **optimized for questions like "how much" and "is it trending?"**

Logs are **optimized for questions like "what happened" and "show me the error"**

---

## What You'll Do Today

1. **Collect metrics** using Prometheus
2. **Store metrics** in time-series database
3. **Query metrics** using PromQL
4. **Visualize metrics** in Grafana dashboards
5. **Alert on metrics** (tomorrow!)

---

**Next:** [../logs-intro.md](../logs-intro.md)
