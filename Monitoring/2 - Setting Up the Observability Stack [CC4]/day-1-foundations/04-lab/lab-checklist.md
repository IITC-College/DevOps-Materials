# Lab Checklist

Track your progress through the lab.

## Setup & Deployment

- [ ] Minikube is running
- [ ] kubectl is configured
- [ ] Helm is installed
- [ ] Docker is working

## Part 1: Deploy Flask App

- [ ] Built Docker image (`flask-app:latest`)
- [ ] Loaded image into Minikube
- [ ] Created namespace `monitoring-lab`
- [ ] Deployed Flask app
- [ ] Verified pods are running
- [ ] Checked /metrics endpoint

## Part 2: Install Monitoring Stack

- [ ] Added Prometheus Helm repo
- [ ] Installed kube-prometheus-stack
- [ ] All pods are running (prometheus, grafana, alertmanager, etc.)

## Part 3: Access Grafana

- [ ] Port-forward to Grafana (3000)
- [ ] Logged in (admin / prom-operator)
- [ ] Prometheus data source is "working"
- [ ] Viewed Kubernetes dashboards

## Part 4: Generate Traffic & View Metrics

- [ ] Generated requests to Flask app
- [ ] Created custom dashboard with Flask metrics
- [ ] Saw request rate in Grafana

## Part 5: Failure Scenarios

### Scenario 1: High CPU
- [ ] Triggered CPU spike
- [ ] Observed in Grafana
- [ ] Used investigation guide to understand cause
- [ ] Used queries to confirm hypothesis
- [ ] Cleaned up

### Scenario 2: OOMKilled
- [ ] Triggered memory exhaustion
- [ ] Pod was killed and restarted
- [ ] Observed restart reason in metrics
- [ ] Identified the issue from metrics only
- [ ] Cleaned up

### Scenario 3: CrashLoopBackOff
- [ ] Triggered pod crash loop
- [ ] Observed rapid restarts
- [ ] Pod status showed CrashLoopBackOff
- [ ] Restart count increased
- [ ] Cleaned up

### Scenario 4: Pod Crashing
- [ ] Killed a pod
- [ ] Pod restarted automatically
- [ ] Metrics showed the gap
- [ ] Pod recovered
- [ ] Cleaned up

### Scenario 5: Scaling
- [ ] Scaled replicas up (3 pods)
- [ ] Observed in pod count metric
- [ ] Load distributed across pods
- [ ] Scaled down (2 pods)
- [ ] Observed in metrics
- [ ] Cleaned up

## Final Exercise

- [ ] Read final exercise: [../../final-exercise/](../../final-exercise/)
- [ ] Completed the challenge
- [ ] Debugged pod failures using metrics only

## Outcomes

- [ ] Understand how Prometheus collects metrics
- [ ] Can navigate Grafana dashboards
- [ ] Can write basic PromQL queries (up, rate, sum)
- [ ] Can debug Kubernetes issues using metrics
- [ ] Know metrics-first investigation approach
- [ ] Confident in Day 2 topics (Alerts, Logs)

---

## Questions to Ask Yourself

1. **For each scenario:**
   - What metric changed?
   - How did I know there was a problem?
   - What would an alert look like for this?

2. **General:**
   - How would I set up monitoring for my own app?
   - What metrics would I care most about?
   - How would I alert on these metrics?

---

**Great work!** You've completed Day 1. Ready for Day 2? 🚀
