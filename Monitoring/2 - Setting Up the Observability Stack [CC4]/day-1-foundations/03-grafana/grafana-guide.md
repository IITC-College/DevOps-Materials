# Grafana: Complete Guide

## What is Grafana?

Grafana is a visualization and dashboard platform. It:
- Connects to data sources (Prometheus, Loki, etc.)
- Creates beautiful dashboards
- Shows real-time metrics
- Enables alerting
- Provides sharing and collaboration

Think of it as: **"The beautiful interface for Prometheus data"**

---

## Architecture

```
Prometheus
  (stores metric data)
    ↓
  (Grafana queries)
Grafana
  (visualizes data)
    ↓
  (you see dashboards)
You
  (understand your system)
```

---

## Key Concepts

### 1. Data Source

A **data source** is where Grafana fetches data from.

Common data sources:
- **Prometheus** — Metrics (what we're using)
- **Loki** — Logs
- **Tempo** — Traces
- **Elasticsearch** — Search/analytics
- **PostgreSQL** — Relational database

### Adding a Data Source

1. Go to: Configuration → Data Sources
2. Click: Add data source
3. Select: Prometheus
4. Enter: Prometheus URL (e.g., `http://prometheus:9090`)
5. Click: Save & test

---

### 2. Dashboard

A **dashboard** is a collection of visualizations (panels).

```
┌─────────────────────────────────────────┐
│ My Application Dashboard                │
├─────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐       │
│  │   Requests  │  │   Errors    │       │
│  │   1.2K/s    │  │   2/s       │       │
│  └─────────────┘  └─────────────┘       │
│  ┌──────────────────────────────┐       │
│  │     CPU Usage (graph)        │       │
│  │  ████████████████████░░░░    │       │
│  │  ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔    │       │
│  └──────────────────────────────┘       │
│  ┌──────────────────────────────┐       │
│  │     Memory Usage (gauge)     │       │
│  │  ████████░░░░░░░░░░░░░░░░    │       │
│  │  (2.5GB / 8GB)               │       │
│  └──────────────────────────────┘       │
└─────────────────────────────────────────┘
```

### Creating a Dashboard

1. Go to: Create → Dashboard
2. Click: Add panel
3. Choose: Visualization (Graph, Stat, Gauge, etc.)
4. Write: PromQL query
5. Customize: Title, colors, thresholds
6. Click: Save

---

### 3. Panel

A **panel** is a single visualization.

Types of panels:
- **Graph** — Line chart over time
- **Stat** — Single number (Requests: 1.2K)
- **Gauge** — Circular progress (CPU: 42%)
- **Table** — Data in rows/columns
- **Heatmap** — Patterns over time
- **Bar Chart** — Compare values
- **Pie Chart** — Part-to-whole

### Building a Panel: Step by Step

**Step 1: Query**
```
rate(http_requests_total[5m])
```

**Step 2: Visualization**
- Choose: Graph
- This shows requests over time as a line chart

**Step 3: Customize**
- Title: "Request Rate"
- Y-axis: "Requests/sec"
- Color: Blue

**Step 4: Save**
- Panel is now part of the dashboard

---

### 4. PromQL Query in Grafana

Writing queries in Grafana panels:

```
# Simple counter
http_requests_total{job="api"}

# Calculate rate
rate(http_requests_total{job="api"}[5m])

# Sum across pods
sum(rate(http_requests_total{job="api"}[5m])) by (pod)

# Error rate as percentage
sum(rate(http_requests_failed_total[5m])) / 
sum(rate(http_requests_total[5m])) * 100
```

---

### 5. Variables (Dynamic Filters)

Variables make dashboards dynamic.

**Without variables:**
- Dashboard shows: "requests for all pods"
- To see specific pod: Edit dashboard, change query

**With variables:**
- Dropdown: Select pod name
- Dashboard updates instantly
- Reusable dashboard for all pods

Example:
```
# Query with variable
rate(http_requests_total{pod="$pod"}[5m])

# At top of dashboard: 
# Dropdown: [Select pod: app-1, app-2, app-3, ...]
```

---

## Common Dashboard Patterns

### Pattern 1: System Health Dashboard

Panels:
- Pod count (stat)
- CPU usage (gauge)
- Memory usage (gauge)
- Disk usage (gauge)
- Network I/O (graph)

### Pattern 2: Application Performance Dashboard

Panels:
- Request rate (graph)
- Error rate (graph)
- Latency p50/p95/p99 (graph)
- Requests by endpoint (bar chart)
- Error types (pie chart)

### Pattern 3: Database Dashboard

Panels:
- Query rate (stat)
- Connection count (stat)
- Slow queries (table)
- Replication lag (graph)
- Cache hit ratio (gauge)

---

## Importing Pre-Built Dashboards

Grafana has a library of ready-made dashboards.

### How to Import

1. Go to: Dashboards → Browse → Import
2. Search: "Kubernetes" or "Prometheus"
3. Find: Dashboard you like (e.g., "Kubernetes cluster monitoring")
4. Click: Import
5. Select: Your Prometheus data source
6. Dashboard appears instantly

Common dashboards to import:
- **Kubernetes Cluster Monitoring** — Overall cluster health
- **Node Exporter** — Linux server metrics
- **Prometheus** — Prometheus internals

---

## Thresholds and Colors

Make dashboards more intuitive with colors:

```
Panel: CPU Usage

Thresholds:
  Green (good):    0-60%
  Yellow (warning): 61-80%
  Red (alert):     81-100%

Color mapping:
  0-60%   → Green ✅
  61-80%  → Yellow ⚠️
  81-100% → Red 🔴
```

Grafana automatically colors the panel based on value.

---

## Real-Time Updates

Dashboards update automatically:
- **Default:** Every 30 seconds
- **Customizable:** 1s, 5s, 10s, 30s, 1m, etc.

---

## Sharing Dashboards

- Generate link: Anyone with link can view
- Export JSON: Share dashboard definition
- Backup: Download dashboard as JSON

---

## Key Takeaways

1. **Grafana visualizes Prometheus data**
2. **Dashboards = Collections of panels**
3. **Panels show charts/gauges/tables**
4. **Write PromQL queries in panels**
5. **Variables make dashboards dynamic**
6. **Thresholds make trends obvious**
7. **Import pre-built dashboards to save time**

---

## Next Steps

1. Read [concepts/](./concepts/) for details on:
   - Data sources
   - Dashboards
   - Panels

2. Do the exercise: [exercises/first-dashboard-exercise.md](./exercises/first-dashboard-exercise.md)

3. Check the sample: [sample-dashboard-config.json](./sample-dashboard-config.json)

---

**Next part:** → [../../04-lab/](../../04-lab/)
