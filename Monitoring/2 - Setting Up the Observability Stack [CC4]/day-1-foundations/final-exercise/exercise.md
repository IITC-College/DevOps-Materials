# Final Exercise: Debugging Pod Failures

## The Setup

Your Flask app deployment is having problems. Three scenarios will test your ability to diagnose using metrics only.

**Rule:** No `kubectl describe`, no `kubectl logs`, no SSH. Only Grafana and Prometheus.

---

## Scenario 1: The Quiet Restart (Easy)

### Problem Statement

One of your replicas has restarted unexpectedly. The other replica is fine and serving traffic.

### Your Tasks

1. **Identify the restarted pod**
   - Which pod restarted?
   - How many times?

2. **Find the cause**
   - Did it run out of memory?
   - High CPU?
   - Something else?

3. **Write your findings**
   ```
   Pod name: _______________
   Restart count: _______________
   Reason: _______________
   Root cause: _______________
   ```

### Trigger Instructions

```bash
# In a terminal, delete one pod (it will restart automatically)
kubectl get pods -n monitoring-lab | grep flask-app
kubectl delete pod -n monitoring-lab <any-flask-app-pod>

# Now investigate using ONLY Grafana metrics
```

### Investigation Steps

1. Open Grafana
2. Look for a pod with low age and incremented restart counter
3. Check the termination reason
4. Look at resource usage at time of restart
5. Write your conclusions

### After Investigation

Once you've written your findings:
- **Read solution:** [solutions/solution-1.md](./solutions/solution-1.md)
- **Compare** your diagnosis with the expected answer

---

## Scenario 2: The Slow Spiral (Medium)

### Problem Statement

Your application's latency is increasing over time. It's not a traffic spike. Something is degrading.

### Your Tasks

1. **Spot the degradation**
   - When did latency start increasing?
   - Which metric changed?

2. **Correlate with resource usage**
   - Is CPU increasing?
   - Is memory increasing?
   - Both?

3. **Identify the problem**
   - Memory leak?
   - Resource contention?
   - Something else?

4. **Write your findings**
   ```
   Affected metric: _______________
   Start time: _______________
   Resource issue: _______________
   Suspected cause: _______________
   ```

### Trigger Instructions

```bash
# Generate traffic that causes memory issues
for i in {1..20}; do
  curl -s http://localhost:8080/memory-leak &
  sleep 2
done

# Watch Grafana as memory climbs
```

### Investigation Steps

1. Go to request latency graph
2. Identify when latency started climbing
3. Switch to memory usage graph for same time window
4. Correlate the two
5. Estimate when pod will crash
6. Write your analysis

### After Investigation

Once you've written your findings:
- **Read solution:** [solutions/solution-2.md](./solutions/solution-2.md)
- **Compare** your diagnosis

---

## Scenario 3: The Cascading Failure (Hard)

### Problem Statement

Multiple things are happening at once. Pod is crashing, causing traffic to shift, causing other pods to struggle.

### Your Tasks

1. **Identify the primary failure**
   - Which pod crashed first?
   - What was the restart reason?

2. **Identify the cascading effects**
   - What happened to the other pod?
   - How did its metrics change?
   - Did it eventually fail too?

3. **Trace the causality**
   - Event 1 → Event 2 → Event 3?
   - Or all independent?

4. **Write your findings**
   ```
   Primary failure:
     Pod: _______________
     Reason: _______________
     Time: _______________
   
   Cascading effect:
     Affected pod: _______________
     Impact: _______________
     Recovery time: _______________
   
   Lesson:
     What would you monitor to prevent this?
     _______________
   ```

### Trigger Instructions

```bash
# This is complex. Follow these steps in order:

# Step 1: Corrupt one deployment (makes it crash)
kubectl edit deployment flask-app -n monitoring-lab
# Change to: command: ["false"]
# Save and exit

# Step 2: Watch what happens
kubectl get pods -n monitoring-lab -w

# Step 3: Investigate in Grafana for 3-5 minutes
# (Don't fix yet!)

# Step 4: After investigation, undo the change
# Edit again, remove the "command: ["false"]" line
```

### Investigation Steps

1. Spot the restart spike
2. Check pod statuses
3. Look at available replicas
4. Monitor request rate (does it drop?)
5. Check error rate (does it spike?)
6. Watch as situation evolves
7. Note recovery time

### After Investigation

Once you've written your findings:
- **Read solution:** [solutions/solution-3.md](./solutions/solution-3.md)
- **Compare** your analysis

---

## Grading Yourself

For each scenario, score yourself:

### Perfect (10/10)
✅ Identified the problem correctly  
✅ Found supporting metrics  
✅ Understood the root cause  
✅ Could explain to a colleague  

### Good (7/10)
✅ Identified the problem  
⚠️ Found most metrics, missed some  
✅ Understood the general cause  

### Needs Work (5/10)
⚠️ Identified a symptom (not root cause)  
⚠️ Partial metric correlation  
❌ Unclear on root cause  

---

## Reflection Questions

After completing all three scenarios:

1. **What was your most effective query?**
   - The one that answered the question fastest

2. **What metrics do you use first?**
   - When you see a problem, where do you look?

3. **If you had to pick one dashboard for on-call duties, what would it show?**
   - What's the absolute minimum you need to see?

4. **How confident are you debugging production now?**
   - Be honest!

---

## Next Steps

### If You Scored Well (9+/10):
🎉 **Congratulations!** You're ready for Day 2 (Alerting).

Focus tomorrow on:
- Setting up alerts so you know BEFORE customers complain
- Automated responses (scale, restart, etc.)

### If You Scored Okay (7-8/10):
✅ **Good progress!** You have the fundamentals.

Before Day 2:
- Re-read [../02-prometheus/prometheus-guide.md](../02-prometheus/prometheus-guide.md)
- Practice more PromQL queries
- Get comfortable with Grafana navigation

### If You Scored Lower (< 7/10):
📚 **Keep practicing!**

Go back and:
1. Re-do the 5 failure scenarios
2. Write queries for each one
3. Build your own dashboard
4. Practice until it feels natural

---

## Bonus: Build Your Own Scenario

Once you've completed the three exercises, try building your own:

1. Think of a failure you want to catch
2. Trigger it (or simulate it with synthetic traffic)
3. Write down the metrics you'd alert on
4. Set up the alert (Day 2 topic)

---

**Great work completing Day 1!** 🚀

Tomorrow: **Day 2 — Alerts, Logs, and Automation**
