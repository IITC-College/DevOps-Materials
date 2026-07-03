# Prometheus: Complete Guide

## What is Prometheus?

Prometheus is an **open-source monitoring and alerting system** designed for reliability engineering.

In simple terms:
- It **collects metrics** from your applications and infrastructure
- It **stores them** in a time-series database
- It **lets you query** the data with a powerful query language
- It **alerts you** when things go wrong

---

## How Prometheus Works

### The Pull Model

Unlike most systems that **push** data (agent sends data to server), Prometheus **pulls** data (server requests data from agent).

```
Traditional Push Model:
  Application → (sends data) → Monitoring System

Prometheus Pull Model:
  Application (listens on /metrics)
    ↑ (Prometheus scrapes every 15 seconds)
  Prometheus
```

### Why Pull?

✅ **Simpler** — No need for agents or TLS certificates  
✅ **Reliable** — Pull only fails if service is down  
✅ **More control** — You decide when to scrape  
✅ **Stateless** — Prometheus doesn't need persistent storage for collection  

---

## The Scraping Process

```
Step 1: Prometheus reads config
  └─ "Every 15 seconds, ask http://pod-1:8080/metrics for data"

Step 2: Prometheus sends HTTP GET request
  └─ GET http://pod-1:8080/metrics

Step 3: Application responds with metrics
  └─ cpu_usage_percent{pod="pod-1"} 42
  └─ memory_bytes{pod="pod-1"} 536870912
  └─ http_requests_total{pod="pod-1",method="GET"} 1000

Step 4: Prometheus stores in database
  └─ Timestamp + metric values saved

Step 5: Repeat every 15 seconds
```

---

## Metrics and Labels

### Format

```
metric_name{label1="value1",label2="value2"} numeric_value
```

### Example

```
http_requests_total{method="GET",path="/api/users",status="200"} 1050
http_requests_total{method="GET",path="/api/users",status="500"} 3
```

### Why Labels?

Labels let you **filter and aggregate** metrics.

```
Question: "How many GET requests succeeded?"
Answer:   sum(http_requests_total{method="GET",status="200"})
          = 1050

Question: "How many total requests?"
Answer:   sum(http_requests_total)
          = 1053
```

---

## Exporters: Making Metrics Prometheus-Compatible

Not all applications natively expose metrics. **Exporters** are programs that:

1. Connect to your application/system
2. Collect data
3. Convert to Prometheus format
4. Expose on `/metrics` endpoint

### Common Exporters

| System | Exporter | What it tracks |
|--------|----------|----------------|
| Linux Server | node-exporter | CPU, memory, disk, network |
| Docker | cadvisor | Container CPU, memory |
| PostgreSQL | postgres_exporter | Queries, connections, locks |
| Redis | redis_exporter | Keys, memory, connections |
| Kubernetes | kube-state-metrics | Pod status, resource usage |

### How They Work

```
PostgreSQL (no metrics)
  ↓
postgres_exporter (connects to PostgreSQL, queries status)
  ↓
Exposes: http://exporter:9187/metrics
  └─ pg_stat_activity_queries{datname="mydb"} 5
  └─ pg_connections_max 100
  └─ pg_up 1
  ↓
Prometheus scrapes /metrics
```

---

## Service Discovery in Kubernetes

In Kubernetes, pods come and go. Prometheus needs to find them automatically.

### Without Service Discovery

❌ Manual config:
```yaml
scrape_configs:
  - targets:
    - 'pod-1:8080'
    - 'pod-2:8080'
    - 'pod-3:8080'
    # Breaks when pods restart with new IPs
```

### With Service Discovery

✅ Automatic:
```yaml
scrape_configs:
  - kubernetes_sd_configs:
    - role: pod
    # Finds ALL pods automatically
    # Adds/removes scrape targets as pods scale
```

Prometheus **watches the Kubernetes API** and automatically:
- Discovers new pods
- Removes pods that are deleted
- Updates IP addresses when pods restart

---

## Metrics in Kubernetes

When you deploy kube-prometheus-stack, you automatically get metrics from:

```
kubelet
  └─ container_cpu_usage_seconds_total
  └─ container_memory_usage_bytes
  └─ kubelet_running_pods
  └─ kubelet_pod_worker_duration_seconds

kube-state-metrics
  └─ kube_pod_status_phase{phase="Running"}
  └─ kube_pod_container_status_restarts_total
  └─ kube_pod_labels
  └─ kube_node_status_allocatable

node-exporter (runs on each node)
  └─ node_cpu_seconds_total
  └─ node_memory_MemAvailable_bytes
  └─ node_disk_io_reads_total
  └─ node_network_receive_bytes_total
```

---

## The /metrics Endpoint

Any service that exposes metrics must have a `/metrics` endpoint.

### Example Response

```
# HELP http_requests_total Total HTTP requests
# TYPE http_requests_total counter
http_requests_total{method="GET",status="200"} 1050
http_requests_total{method="GET",status="500"} 3
http_requests_total{method="POST",status="201"} 42

# HELP http_request_duration_seconds HTTP request latency
# TYPE http_request_duration_seconds histogram
http_request_duration_seconds_bucket{le="0.05"} 500
http_request_duration_seconds_bucket{le="0.1"} 1500
http_request_duration_seconds_bucket{le="+Inf"} 2000
```

### How to Generate This (in your app)

We'll cover this in the Lab (Part 4), but the idea is simple:
- Use a Prometheus client library (prometheus_client for Python)
- Create metrics in your code
- They're automatically exposed on /metrics

---

## PromQL: Querying Prometheus

PromQL (Prometheus Query Language) lets you ask questions about your data.

### Three Essential Queries for Today

We'll cover these in detail in [promql-basics/](./promql-basics/):

1. **up** — Is a service running?
   ```
   up{job="prometheus"} → 1 (running) or 0 (down)
   ```

2. **rate()** — How fast is something changing?
   ```
   rate(http_requests_total[5m]) → requests per second over last 5 minutes
   ```

3. **sum()** — Total across multiple instances?
   ```
   sum(node_cpu_seconds_total) → Total CPU time across all nodes
   ```

---

## Prometheus Architecture

```
┌─────────────────────────────────────────┐
│ Prometheus Server                       │
├─────────────────────────────────────────┤
│                                         │
│  ┌─────────────────────────────────┐   │
│  │ Scrape Engine                   │   │
│  │ (pulls data from /metrics)      │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │ Time-Series Database            │   │
│  │ (stores metric data)            │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │ PromQL Engine                   │   │
│  │ (answers your queries)          │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │ Alert Engine                    │   │
│  │ (triggers alerts)               │   │
│  └─────────────────────────────────┘   │
│                                         │
└─────────────────────────────────────────┘
```

---

## Key Takeaways

1. **Prometheus pulls metrics** from services via HTTP
2. **Services expose /metrics** endpoints
3. **Labels allow powerful queries** (filter, aggregate, group)
4. **Service discovery automates scaling** in Kubernetes
5. **PromQL is simple** (just learn 3 queries for basics)

---

## Next Steps

1. Read [concepts/](./concepts/) for detailed info on:
   - Metric types
   - Pull model details
   - Exporters
   - Service discovery
   - Prometheus config

2. Learn PromQL basics:
   - [promql-basics/up-query.md](./promql-basics/up-query.md)
   - [promql-basics/rate-query.md](./promql-basics/rate-query.md)
   - [promql-basics/sum-query.md](./promql-basics/sum-query.md)

3. See examples: [examples/sample-prometheus-queries.md](./examples/sample-prometheus-queries.md)

---

**Next part:** → [../../03-grafana/](../../03-grafana/)
