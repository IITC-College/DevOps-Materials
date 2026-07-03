# Final Exercise: Debugging Pod Failures Using Metrics Only

Welcome to the final exercise! This is where you put everything together.

## 🎯 The Challenge

A pod has failed. Using **only Prometheus and Grafana** (no kubectl describe, no logs), you must:

1. Identify that a pod is unhealthy
2. Determine what went wrong
3. Describe the issue using only metrics

## 📋 Prerequisites

- ✅ Completed all 5 failure scenarios
- ✅ Understand how to navigate Grafana
- ✅ Can write basic PromQL queries
- ✅ Familiar with [../04-lab/investigation-guide.md](../04-lab/investigation-guide.md)

---

## 📖 Files

1. **[exercise.md](./exercise.md)** — The challenge with 3 scenarios
2. **[scenarios/](./scenarios/)** — Detailed scenario descriptions
3. **[solutions/](./solutions/)** — Step-by-step solutions

---

## How It Works

### For Each Scenario:

1. **Read the scenario** — Understand what problem to trigger
2. **Trigger it** — Follow the commands to create the failure
3. **Investigate** — Use Grafana + Prometheus queries (no logs!)
4. **Diagnose** — Write down what you found
5. **Compare** — Read the solution and see how you did

---

## Time

**Estimated: 30 minutes**

- ~10 minutes per scenario
- Includes investigation time

---

## Success Criteria

For each scenario, you should be able to:

✅ State the problem (in one sentence)  
✅ Identify which pod is affected  
✅ Describe what metric changed  
✅ Explain the root cause  
✅ Suggest how to fix it  

---

## Difficulty Levels

**Easy:** Scenario 1 (similar to lab scenarios)  
**Medium:** Scenario 2 (requires more investigation)  
**Hard:** Scenario 3 (tricky! combines multiple issues)  

---

**Ready?** → [exercise.md](./exercise.md)

---

## Tips

1. **Start broad** — Look at the full picture first
2. **Then zoom in** — Drill down to specific pods
3. **Look for timing** — When did the issue start?
4. **Use queries** — Write 2-3 queries to confirm your hypothesis
5. **Compare to baseline** — What was normal before?

---

## Metrics to Remember

| Metric | Use Case |
|--------|----------|
| `kube_pod_status_phase` | Is pod running? |
| `kube_pod_container_status_restarts_total` | Is it crashing? |
| `container_cpu_usage_seconds_total` | High CPU? |
| `container_memory_usage_bytes` | Memory issue? |
| `kube_pod_status_ready` | Ready to serve? |
| `kube_pod_container_status_last_terminated_reason` | Why did it crash? |

---

**Let's go!** → [exercise.md](./exercise.md)
