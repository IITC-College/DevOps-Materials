# Traces: Quick Introduction

## What Are Traces?

A **trace** is a record of a single request as it travels through your entire system.

**Example: User places an order**

```
User: POST /checkout
  ↓
[Load Balancer]  (1ms)
  ↓
[API Gateway]    (2ms)
  ├─ Auth check   (10ms)
  ├─ Inventory    (20ms, slow!)
  └─ Payment      (15ms)
  ↓
[Response]       (48ms total)
```

Each hop in the journey is part of the **trace**.

---

## Why Traces?

When a request is slow, traces show **where** it's slow.

### Metrics → Logs → Traces Workflow

```
Metrics say: "Checkout latency is 500ms (should be 50ms)"
   ↓
Logs say: "No errors in logs"
   ↓
Traces say: "Inventory service took 450ms, payment took 50ms"
   ↓
You understand: Inventory service is the bottleneck
```

---

## Common Use Cases

✅ "Why is this request slow?"  
✅ "Which microservice is bottlenecking?"  
✅ "Did the database cause the delay?"  
✅ "How many hops did this request take?"  

---

## Tracing Tools (Future Focus)

- **Jaeger** — Most common open-source tracer
- **Zipkin** — Another popular option
- **Tempo** — Grafana's tracer

---

## Traces vs Metrics vs Logs

| Aspect | Metrics | Logs | Traces |
|--------|---------|------|--------|
| Question | "How much?" | "What happened?" | "How slow?" |
| Data | Numbers | Text | Request path |
| Time to see | Instant | Search | Correlate |
| Use when | Quick overview | Debugging | Latency issues |

---

## Key Takeaway for Today

> **Traces are powerful but complex. Start with metrics and logs first.**

Most problems (80%+) are solved with metrics alone.

---

## For the Curious

The detective mindset in SRE:

```
1. See a problem
   ↓
2. Check METRICS  ← Usually here (80% of time)
   ↓
3. If needed: Search LOGS
   ↓
4. If needed: Look at TRACES (rare, 5% of time)
```

---

## Today's Focus

Today: **Part 1 (Why)** → **Part 2 (Prometheus/Metrics)** → **Part 3 (Grafana)** → **Part 4 (Lab)**

Traces are important but complex. You'll revisit them in a dedicated tracing day.

---

**Back to main content:** [../why-monitoring.md](../why-monitoring.md#-todays-strategy-metrics-first)

**Next part:** → [../../02-prometheus/](../../02-prometheus/)
