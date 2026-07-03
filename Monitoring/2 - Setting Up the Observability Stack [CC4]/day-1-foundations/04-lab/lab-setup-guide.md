# Lab Setup Guide: Step-by-Step

## Prerequisites Check

Before starting, verify everything is ready:

```bash
# Minikube
minikube status
# Should show: minikube: Running, kubelet: Running, apiserver: Running

# kubectl
kubectl cluster-info
# Should connect to your Minikube cluster

# Helm
helm version
# Should show version 3.x

# Docker
docker --version
# Any recent version is fine
```

If any are missing, install them before continuing.

---

## Part 1: Deploy Flask Application (10 minutes)

### Step 1.1: Create Namespace

```bash
kubectl create namespace monitoring-lab
```

### Step 1.2: Build Docker Image

Navigate to the app folder:
```bash
cd ./04-lab/app
```

Build the Flask app image:
```bash
docker build -t flask-app:latest .
```

Load it into Minikube:
```bash
minikube image load flask-app:latest
```

Verify:
```bash
minikube image ls | grep flask-app
```

### Step 1.3: Deploy Application

```bash
kubectl apply -f kubernetes-deployment.yaml -n monitoring-lab
```

### Step 1.4: Verify Deployment

```bash
kubectl get pods -n monitoring-lab
# Should show: flask-app-xxxxx RUNNING

kubectl get svc -n monitoring-lab
# Should show: flask-app service
```

### Step 1.5: Check Metrics Endpoint

```bash
# Port-forward to the app
kubectl port-forward -n monitoring-lab svc/flask-app 8080:8080 &

# In another terminal, check metrics
curl http://localhost:8080/metrics

# You should see output like:
# # HELP flask_http_requests_total Total HTTP requests
# # TYPE flask_http_requests_total counter
# flask_http_requests_total{method="GET",status="200"} 42
```

Stop the port-forward (or let it run):
```bash
kill %1
```

---

## Part 2: Install Prometheus Stack (15 minutes)

### Step 2.1: Add Helm Repository

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

### Step 2.2: Install kube-prometheus-stack

```bash
helm install prometheus prometheus-community/kube-prometheus-stack \
  -n monitoring-lab \
  -f monitoring-stack/kube-prometheus-stack-values.yaml
```

### Step 2.3: Wait for Components

```bash
kubectl get pods -n monitoring-lab
# Wait until all pods show RUNNING (1-2 minutes)

# Check specifically:
kubectl get pods -n monitoring-lab | grep prometheus
kubectl get pods -n monitoring-lab | grep grafana
```

Full check:
```bash
kubectl get all -n monitoring-lab
```

---

## Part 3: Access Grafana (5 minutes)

### Step 3.1: Port-Forward to Grafana

```bash
kubectl port-forward -n monitoring-lab svc/prometheus-grafana 3000:80 &
```

### Step 3.2: Open Grafana

Open your browser and go to:
```
http://localhost:3000
```

### Step 3.3: Login

- Username: `admin`
- Password: `prom-operator` (default from Helm chart)

### Step 3.4: Verify Prometheus Data Source

1. Go to: Configuration → Data Sources
2. You should see: "Prometheus" listed
3. Click on it
4. Click: "Test" button
5. Should show: "Data source is working"

---

## Part 4: Generate Traffic (5 minutes)

### Step 4.1: Generate Some Requests

```bash
# Keep sending requests to generate metrics
for i in {1..100}; do 
  curl -s http://localhost:8080/ > /dev/null
  sleep 1
done
```

Or in a separate terminal:
```bash
# Continuous traffic
while true; do
  curl -s http://localhost:8080/ > /dev/null
  sleep 1
done
```

---

## Part 5: View Dashboards (10 minutes)

### Step 5.1: Open Grafana Home

Go to: http://localhost:3000/d/overview

You should see pre-built dashboards for:
- Kubernetes Cluster
- Nodes
- Pods
- etc.

### Step 5.2: Check Kubernetes Cluster Dashboard

1. Go to: Dashboards → Browse
2. Look for: "Kubernetes / Cluster"
3. Open it
4. Observe:
   - Pod count
   - CPU usage
   - Memory usage
   - Network I/O

### Step 5.3: Create a Custom Dashboard

1. Go to: Create → Dashboard
2. Click: Add panel
3. Paste this query:
   ```
   rate(flask_http_requests_total[5m])
   ```
4. Click: Visualizations → Graph
5. Click: Save

You're now viewing your Flask app's request rate!

---

## Part 6: Trigger Failure Scenarios (60 minutes)

Now for the interesting part. Navigate to [failure-scenarios/](./failure-scenarios/):

- [scenario-1-high-cpu.md](./failure-scenarios/scenario-1-high-cpu.md)
- [scenario-2-oomkilled.md](./failure-scenarios/scenario-2-oomkilled.md)
- [scenario-3-crashloopbackoff.md](./failure-scenarios/scenario-3-crashloopbackoff.md)
- [scenario-4-pod-crashing.md](./failure-scenarios/scenario-4-pod-crashing.md)
- [scenario-5-scaling.md](./failure-scenarios/scenario-5-scaling.md)

For each scenario:

1. Read the scenario description
2. Follow the steps to trigger it
3. Open Grafana
4. Observe the impact in metrics
5. Use [investigation-guide.md](./investigation-guide.md) to understand what to look for

---

## Troubleshooting

### Grafana not accessible

```bash
# Check if port-forward is running
ps aux | grep port-forward

# Restart it
kubectl port-forward -n monitoring-lab svc/prometheus-grafana 3000:80 &
```

### Pods not running

```bash
# Check pod status
kubectl describe pod <pod-name> -n monitoring-lab

# Check logs
kubectl logs <pod-name> -n monitoring-lab
```

### No metrics appearing

```bash
# Check Prometheus is scraping targets
kubectl port-forward -n monitoring-lab svc/prometheus-kube-prometheus-prometheus 9090:9090 &

# Open: http://localhost:9090/targets
# All targets should be "UP"
```

### Flask app metrics not appearing

```bash
# Check if Flask app is exposing metrics
kubectl port-forward -n monitoring-lab svc/flask-app 8080:8080 &
curl http://localhost:8080/metrics
# Should show Flask metrics
```

---

## Cleanup (After Lab)

If you want to delete everything:

```bash
# Delete the namespace (removes all resources)
kubectl delete namespace monitoring-lab

# Remove port-forwards
kill %1 %2 %3  # Kill background jobs
```

---

## Next Steps

1. Complete all failure scenarios
2. Read [investigation-guide.md](./investigation-guide.md)
3. Use the lab checklist: [lab-checklist.md](./lab-checklist.md)
4. Move to final exercise: [../../final-exercise/](../../final-exercise/)

---

**Happy monitoring!** 🚀
