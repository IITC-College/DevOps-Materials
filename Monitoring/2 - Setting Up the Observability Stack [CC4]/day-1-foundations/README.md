# Day 1: Foundations of Monitoring

Welcome to Day 1 of the Observability Stack course! Today, you'll learn the fundamentals of monitoring and start building your first observability platform using **Prometheus** and **Grafana** on **Kubernetes**.

## 🎯 What You'll Learn Today

This day is structured in 4 main parts + a final exercise:

### Part 1: Why Do We Need Monitoring? (20–30 minutes)
Learn the business case for monitoring and understand the three pillars of observability:
- **Metrics** (focus of today)
- **Logs**
- **Traces**

We'll use a real-world scenario to understand why we need monitoring before diving into any tools.

**→ Start with:** [01-why-monitoring/](./01-why-monitoring/)

---

### Part 2: Prometheus Fundamentals (40–60 minutes)
Dive into Prometheus, the industry-standard metrics collection system:
- What is a Metric?
- Pull Model vs Push Model
- Exporters
- Service Discovery in Kubernetes
- Basic PromQL queries: `up`, `rate()`, `sum()`

**→ Start with:** [02-prometheus/](./02-prometheus/)

---

### Part 3: Grafana Basics (30–40 minutes)
Learn to visualize metrics and build dashboards:
- Adding Data Sources
- Creating Dashboards
- Understanding Panels
- Basic Query patterns
- Importing pre-built dashboards

**→ Start with:** [03-grafana/](./03-grafana/)

---

### Part 4: Hands-On Lab (60–90 minutes)
Get practical experience:
1. Deploy a Python Flask application to Minikube
2. Set up the monitoring stack with kube-prometheus-stack
3. View metrics in Grafana
4. Trigger failure scenarios and observe them through metrics only

**→ Start with:** [04-lab/](./04-lab/)

---

### Part 5: Final Exercise (30 minutes)
Test your understanding:
- Challenge: Debug pod failures using **only** Prometheus and Grafana (no logs!)
- This trains the metrics-first investigation mindset used by SRE teams

**→ Start with:** [final-exercise/](./final-exercise/)

---

## 📋 Prerequisites

Before starting, make sure you have:

- [ ] Minikube installed and running
- [ ] kubectl configured
- [ ] Helm 3.x installed
- [ ] Docker installed
- [ ] A text editor or IDE

Quick check:
```bash
minikube status
kubectl version --client
helm version
docker --version
```

---

## 🚀 Quick Start

The recommended flow:
1. **Read** Part 1 (Why Monitoring) — 20 min
2. **Read** Part 2 (Prometheus) — 45 min
3. **Read** Part 3 (Grafana) — 35 min
4. **Do** Part 4 (Lab) — 90 min
5. **Challenge** Final Exercise — 30 min

**Total estimated time: 3.5–4 hours**

---

## 💡 Key Principle

Today, we focus **exclusively on Metrics** to avoid information overload. We intentionally skip deep dives into Logs and Traces until later days. This narrow focus allows you to master one piece at a time and see quick wins.

---

## 📌 What This Day Teaches

By the end of Day 1, you'll:

✅ Understand why monitoring is critical  
✅ Know how Prometheus collects metrics  
✅ Be able to build dashboards in Grafana  
✅ Deploy a working monitoring stack on Kubernetes  
✅ Debug issues using metrics only (without logs)  
✅ Understand the metrics-first debugging mindset  

---

## 🔗 Quick Navigation

- [Part 1: Why Monitoring](./01-why-monitoring/)
- [Part 2: Prometheus](./02-prometheus/)
- [Part 3: Grafana](./03-grafana/)
- [Part 4: Lab](./04-lab/)
- [Final Exercise](./final-exercise/)

---

## ⚠️ Important Notes

- **This is hands-on**: You'll get the most value by doing the lab (Part 4), not just reading.
- **Metrics-first mindset**: Before looking at logs, try to understand issues through metrics only.
- **Day 2 preview**: Tomorrow you'll learn Alerts (using Prometheus rules) and Logs (using Loki).

---

Good luck! Let's get started! 🚀
