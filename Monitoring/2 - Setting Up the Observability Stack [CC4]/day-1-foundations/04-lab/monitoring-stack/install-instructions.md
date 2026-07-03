# Kube-Prometheus-Stack Installation

This file contains additional details about the Helm installation.

## Quick Install

See [../lab-setup-guide.md](../lab-setup-guide.md#part-2-install-prometheus-stack-15-minutes) for step-by-step instructions.

## What Gets Installed

The kube-prometheus-stack includes:

1. **Prometheus** — Metrics database and scraper
2. **Grafana** — Dashboards and visualization
3. **AlertManager** — Alert routing and notification
4. **Prometheus Operator** — Kubernetes operator for managing Prometheus
5. **kube-state-metrics** — Kubernetes cluster metrics
6. **node-exporter** — Node/server metrics
7. **Grafana dashboards** — Pre-built dashboards

## Configuration

The `kube-prometheus-stack-values.yaml` file:
- Reduces resource requests for Minikube
- Enables persistence for data
- Configures Grafana with default password
- Sets up automatic pod discovery

## Verify Installation

```bash
# Check all pods
kubectl get pods -n monitoring-lab

# Expected pods:
# - prometheus-kube-prometheus-prometheus-*
# - prometheus-grafana-*
# - prometheus-kube-state-metrics-*
# - prometheus-node-exporter-*
# - alertmanager-*
# - prometheus-kube-prometheus-operator-*
```

## Uninstall

```bash
helm uninstall prometheus -n monitoring-lab
```

## Troubleshooting

See [../lab-setup-guide.md](../lab-setup-guide.md#troubleshooting) for common issues.
