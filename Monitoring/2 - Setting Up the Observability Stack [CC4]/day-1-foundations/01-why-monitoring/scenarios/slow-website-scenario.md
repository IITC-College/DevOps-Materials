# Real-World Scenario: The Slow Website

## Timeline: Tuesday, 2:15 AM

### 2:15 AM — The Problem

Slack explodes. A customer reports: *"The checkout page is taking 30 seconds to load!"*

Normally, it loads in under 1 second.

### 2:16 AM — Without Monitoring

**You:** (panic mode)  
- SSH into the web server
- Check `top`: CPU looks OK
- Check disk: 60% full, but normal for us
- Check network: No obvious issues
- "Is the database down?" → No, it's running
- Restart the web service (hoping it helps)
- **Nothing changes**

**By 2:45 AM:**
- 15 customers affected
- Still no idea what's wrong
- Waking up the database team at 2:45 AM
- DM the CTO: "We have a production issue"

**By 3:30 AM:**
- Database team finds it: One of 5 database replicas is down
- The other 4 replicas are handling all traffic
- One crashed 30 minutes ago due to OOM (out of memory)
- Root cause: A recent code deploy introduced a memory leak

**By 4:00 AM:**
- Restarted the crashed replica
- Service recovers
- Everyone goes back to bed (angry)

**Total impact: ~2 hours of downtime, 50+ customers affected, damaged trust**

---

### 2:15 AM — With Monitoring

**You:** (open Grafana)

**[Dashboard at a glance]**
```
┌─────────────────────────────────────┐
│ Database Memory Usage               │
│ ████████████████████████░░░░ 90%   │  ← Getting high
│                                     │
│ Active Database Replicas            │
│ ●●●●◯ (4 of 5 replicas)            │  ← One is DOWN!
│                                     │
│ Replication Lag                     │
│ ┌─────────────────────────┐         │
│ │ ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔│  
│ │         ↑ Spike 2h ago │         │
│ └─────────────────────────┘         │
│                                     │
│ Checkout Page Latency               │
│ ┌─────────────────────────┐         │
│ │          ▁▂▃▄▅█▅▄▃▂▁   │  
│ │         ↑ Degrading    │         │
│ └─────────────────────────┘         │
└─────────────────────────────────────┘
```

**You immediately see:**
1. ✅ 4 of 5 database replicas are running (1 crashed)
2. ✅ Replica memory is at 90% (memory leak suspected)
3. ✅ Checkout latency increased with the crash
4. ✅ Replication lag shows the spike happened ~30 min ago

**2:16 AM — Actions:**
- Restart the crashed database replica
- Increase resource limits for remaining replicas
- Alert the dev team: "Memory leak in recent deploy"

**2:18 AM:**
- Database recovering
- Checkout latency dropping

**2:22 AM:**
- All metrics green ✅
- Service fully recovered
- Crisis averted

**2:23 AM:**
- Sleep. Peaceful sleep. No angry messages.

**Total impact: ~8 minutes, 5 customers briefly affected, root cause identified immediately**

---

## Key Differences

| Without Monitoring | With Monitoring |
|---|---|
| 2 hours to diagnose | 2 minutes to diagnose |
| 50+ customers impacted | 5 customers slightly impacted |
| Reactive (respond to complaints) | Proactive (detected via alerts) |
| Panic, guessing | Calm, data-driven |
| Team wakeups | Just you, just on-call |
| Trust damaged | Trust maintained |

---

## The Real Lesson

> The database didn't fail at 2:15 AM. It failed at ~1:45 AM, but nobody noticed for 30 minutes because **there was no monitoring**.

With monitoring:
- The alert fires at 1:45 AM (as soon as 1 replica crashes)
- You fix it at 1:47 AM
- Customers never notice

---

## What This Teaches Us

1. **Observability saves time** — Quick diagnosis
2. **Observability saves money** — Fewer customers lost
3. **Observability saves stress** — Less on-call drama
4. **Observability is essential** — Not optional

By the end of today, you'll build the exact monitoring stack that prevents this scenario.

---

**Next:** → [../concepts/metrics-101.md](../concepts/metrics-101.md)
