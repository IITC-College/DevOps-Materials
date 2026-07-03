# Part 4: Hands-On Lab

Build and observe a real monitoring stack on Kubernetes.

## 📌 What You'll Do

- Deploy a Python Flask app to Minikube
- Install kube-prometheus-stack
- Open Grafana dashboards
- Watch metrics in real-time
- Trigger failure scenarios
- Debug using metrics only

**Estimated time:** 60–90 minutes

---

## Files in This Section

1. **[lab-setup-guide.md](./lab-setup-guide.md)** — Complete setup instructions
2. **[app/](./app/)** — Python Flask app with metrics
3. **[monitoring-stack/](./monitoring-stack/)** — Prometheus/Grafana setup
4. **[failure-scenarios/](./failure-scenarios/)** — Problems to trigger and observe
5. **[investigation-guide.md](./investigation-guide.md)** — How to debug
6. **[lab-checklist.md](./lab-checklist.md)** — Progress tracker

---

## Prerequisites

✅ Minikube running (`minikube status`)  
✅ kubectl configured  
✅ Helm 3.x installed  
✅ Docker installed  

Quick check:
```bash
minikube status
kubectl cluster-info
helm version
docker --version
```

---

## Lab Flow

```
1. Deploy Flask App
   ↓
2. Deploy Prometheus + Grafana
   ↓
3. Open Grafana dashboard
   ↓
4. See metrics in real-time
   ↓
5. Trigger failure scenarios (one at a time)
   ↓
6. Observe each scenario in Grafana
   ↓
7. Move to next scenario
```

---

## Expected Outcomes

By the end of this lab, you'll:

✅ Have working Prometheus + Grafana on Kubernetes  
✅ See live metrics from a real application  
✅ Understand how to spot problems in dashboards  
✅ Know how to correlate infrastructure issues with metrics  
✅ Gain confidence in metric-based debugging  

---

**Let's start!** → [lab-setup-guide.md](./lab-setup-guide.md)
