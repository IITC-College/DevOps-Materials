# Why Do We Need Monitoring?

## The Scenario

It's 2 AM on a Tuesday. Your Slack channel lights up:

> 🚨 **User**: "The website is really slow right now!"  
> 🚨 **User**: "I can't place my order!"  
> 🚨 **Manager**: "What's happening??"

You're on-call. You have **5 minutes** to respond.

### Without Monitoring

You:
1. SSH into random servers
2. Check CPU usage: Looks OK
3. Check disk space: Looks OK
4. Check memory: Looks OK
5. Restart services randomly hoping it fixes it
6. Still no idea what the real problem is
7. Call the team in the middle of the night
8. Waste 2 hours diagnosing manually

### With Monitoring

You:
1. Open your monitoring dashboard (Grafana)
2. See **immediately**: Pod memory usage spiked to 100%
3. See **immediately**: One of your 5 database replicas is down
4. Understand: A memory leak in code + resource contention
5. Fix: Restart the leaky pod, scale up the database
6. **Back to sleep in 15 minutes**

---

## The Core Problem

You can't observe what's happening inside your systems without **data**.

Data about your systems comes in three flavors:

### 🟢 The Three Pillars of Observability

```
┌──────────────────────────────────────────────────┐
│         OBSERVABILITY STACK                       │
├──────────────────────────────────────────────────┤
│                                                   │
│  📊 METRICS        📝 LOGS         🔗 TRACES     │
│  ─────────────     ─────────       ──────────    │
│  • CPU usage       • Error stacks  • Latency    │
│  • Memory          • Events        • Path taken │
│  • Request count   • Timestamps    • Errors     │
│  • Latency         • Context       • Dependencies│
│                                                   │
│  Used for: Quick   Used for:       Used for:    │
│  diagnosis &       Deep dive &     End-to-end   │
│  alerting          debugging       request flow │
│                                                   │
└──────────────────────────────────────────────────┘
```

---

## 📊 METRICS (Today's Focus)

**Metrics** are numbers that change over time.

### Examples:
- CPU usage: `42%`
- Memory usage: `512 MB`
- Requests per second: `100 req/s`
- Error rate: `0.5%`
- Pod count: `3 pods`

### Why Metrics?
- **Fast to query** — Instant answers
- **Easy to alert on** — "Alert when CPU > 80%"
- **Low storage** — Compact over time
- **Business insight** — "We're getting 1000 requests/sec"

### When to use Metrics:
- "How many requests are we handling?"
- "Is the database slow?"
- "Are pods crashing?"
- "What's the memory trend?"

---

## 📝 LOGS (Tomorrow's Focus)

**Logs** are text records of events.

### Examples:
```
2026-07-03T02:14:22Z ERROR: Database connection timeout after 30s
2026-07-03T02:14:23Z INFO: Retrying connection (attempt 2/5)
2026-07-03T02:14:25Z ERROR: Connection failed, moving to replica
```

### Why Logs?
- **Details** — Full context of what happened
- **Searchable** — Find specific errors by pattern
- **Human-readable** — Easy to understand

### When to use Logs:
- "What was the exact error message?"
- "When did this pod crash?"
- "Show me all requests from user XYZ"

---

## 🔗 TRACES (Future Focus)

**Traces** follow a single request through your entire system.

### Example:
```
User Request
  ├─ Load Balancer (1ms)
  ├─ API Gateway (2ms)
  ├─ Auth Service (50ms)  ← SLOW!
  │   └─ Database query (45ms)
  ├─ Business Logic (100ms)
  └─ Response (153ms total)
```

### Why Traces?
- **End-to-end visibility** — See the whole journey
- **Bottleneck identification** — Where is the slowness?
- **Distributed systems** — Understand multi-service calls

### When to use Traces:
- "Why is this user's request slow?"
- "Which service is the bottleneck?"
- "Did the database cause the delay?"

---

## 🎯 Today's Strategy: Metrics First

Here's the debugging mindset of professional SRE teams:

```
1. See a problem
   ↓
2. Open dashboard (METRICS) → "Is it a resource issue?"
   ↓
3. If needed: Search logs (LOGS) → "What's the error?"
   ↓
4. If needed: Trace request (TRACES) → "What's the path?"
```

**Most problems are solved at step 2.** Metrics give you the quick answer.

---

## 💡 Key Insight

> **You can't fix what you can't see.**

Without monitoring:
- Problems surprise you
- Outages take hours to diagnose
- You're always reactive

With monitoring:
- Problems are detected automatically
- You understand issues in minutes
- You're proactive and confident

---

## What's Next?

Today, we'll:

1. ✅ Understand why monitoring matters ← You're here
2. Learn **Prometheus** → How to collect metrics
3. Learn **Grafana** → How to visualize metrics
4. Build a working monitoring stack on Kubernetes
5. Practice debugging with metrics only

By the end of today, you'll have:
- A working Prometheus + Grafana setup
- Live metrics from your cluster
- The skills to debug using metrics-first approach

---

## Real-World Scenario

→ Read: [scenarios/slow-website-scenario.md](./scenarios/slow-website-scenario.md)

This walks through a real outage and how monitoring would have helped.

---

## Next: Learn the Pillars

- [concepts/metrics-101.md](./concepts/metrics-101.md)
- [concepts/logs-intro.md](./concepts/logs-intro.md)
- [concepts/traces-intro.md](./concepts/traces-intro.md)

Then, move to **Part 2: Prometheus** → [../02-prometheus/](../02-prometheus/)
