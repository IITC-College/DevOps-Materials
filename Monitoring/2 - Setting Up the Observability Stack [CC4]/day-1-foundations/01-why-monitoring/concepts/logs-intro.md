# Logs: Quick Introduction

## What Are Logs?

Logs are text records of events that happen in your system.

**Example:**
```
2026-07-03T14:23:45.123Z INFO [api-server] Request started: GET /users?id=123
2026-07-03T14:23:45.250Z DEBUG [db-client] Query: SELECT * FROM users WHERE id=123
2026-07-03T14:23:45.350Z DEBUG [db-client] Query took 100ms
2026-07-03T14:23:45.351Z INFO [api-server] Response: 200 OK, 1.2KB
```

---

## Why Logs?

When metrics tell you **THAT** something went wrong, logs tell you **WHY**.

### Metrics → Logs Workflow

```
Metrics say: "Database latency spiked to 5 seconds"
   ↓
You look at logs: "ERROR: Connection pool exhausted"
   ↓
You understand: Connection leak in recent code
```

---

## Types of Log Levels

| Level | Purpose | Example |
|-------|---------|---------|
| DEBUG | Dev debugging | "Starting database connection pool" |
| INFO | Normal events | "Server started on port 8080" |
| WARNING | Something unusual | "Connection pool at 90% capacity" |
| ERROR | Something failed | "Database connection timeout" |
| CRITICAL | System failure | "Disk full, stopping" |

---

## Logs vs Metrics

| Aspect | Metrics | Logs |
|--------|---------|------|
| Data type | Numbers | Text |
| Purpose | Trends, alerts | Details, debugging |
| Query | "How much?" | "What happened?" |
| Example | CPU: 80% | "ERROR: OOM killer" |
| Volume | Small | Large |
| Storage | Cheap | Expensive |

---

## When You Need Logs

✅ "What was the exact error message?"  
✅ "When did pod X crash and why?"  
✅ "Show me all requests from user 123"  
✅ "What did the code do step-by-step?"  

---

## Tools for Logs (Coming Day 2)

Today we're using **Prometheus** for metrics.  
Tomorrow we'll use **Loki** for logs.

---

## Key Takeaway for Today

> **Metrics are your first tool. Use them first.**

If metrics don't answer your question, then search logs.

---

**Next:** [traces-intro.md](./traces-intro.md)
