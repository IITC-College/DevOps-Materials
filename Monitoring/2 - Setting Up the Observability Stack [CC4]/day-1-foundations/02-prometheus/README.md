# Part 2: Prometheus Fundamentals

Learn how Prometheus collects metrics from your systems.

## 📌 What You'll Learn

- What is Prometheus?
- The Pull Model
- Metrics endpoints and Exporters
- Service Discovery in Kubernetes
- Basic PromQL queries

**Estimated time:** 40–60 minutes

---

## Files in This Section

1. **[prometheus-guide.md](./prometheus-guide.md)** — Main content
2. **[concepts/](./concepts/)** — Detailed concept files
3. **[promql-basics/](./promql-basics/)** — Three essential queries
4. **[examples/](./examples/)** — Sample Prometheus queries

---

## Quick Takeaway

Prometheus:
- **Pulls** metrics from your services
- **Scrapes** `/metrics` endpoints
- **Stores** them in a time-series database
- **Allows** you to query and alert on them

---

## Architecture

```
Your Services (expose /metrics)
    ↓
Prometheus (scrapes every 15s)
    ↓
Time-Series Database (stores metrics)
    ↓
PromQL Queries (query data)
    ↓
Grafana Dashboards (visualize)
    ↓
Alert Rules (notify you)
```

---

## Key Concepts

1. **Metrics** — Data points (numbers over time)
2. **Labels** — Tags to identify what the metric is about
3. **Scrape** — Prometheus pulling data from an endpoint
4. **Exporter** — Software that exposes metrics in Prometheus format
5. **PromQL** — Query language for Prometheus

---

**Let's start!** → [prometheus-guide.md](./prometheus-guide.md)
