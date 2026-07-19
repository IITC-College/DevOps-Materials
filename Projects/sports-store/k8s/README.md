# k8s

Kubernetes manifests for the sports-store stack, mirroring `docker-compose.yml`.
MongoDB is deployed via Helm instead of a raw manifest.

## Layout

```
k8s/
  00-namespace.yaml     # sports-store namespace
  01-secret.yaml        # JWT_SECRET, mongo root password, full MONGO_URI
  02-configmap.yaml      # shared non-secret env (service URLs, ...)
  03-gateway.yaml        # nginx + built frontend, exposed via NodePort
  04-seed-job.yaml       # one-shot data seed (Job, restartPolicy: Never)
  services/               # auth, catalog, cart, order, payment — Deployment + Service each
  mongodb/values.yaml    # Helm values for the Bitnami mongodb chart
```

## 1. Build & push images

Images are tagged under the `lironefitoussi` Docker Hub namespace (already
set in every manifest's `image:` field). Each service builds from its own
directory; the gateway builds from repo root (it needs `frontend/` too):

```bash
docker build -t lironefitoussi/sports-store-auth-service:latest    services/auth-service
docker build -t lironefitoussi/sports-store-catalog-service:latest services/catalog-service
docker build -t lironefitoussi/sports-store-cart-service:latest    services/cart-service
docker build -t lironefitoussi/sports-store-order-service:latest   services/order-service
docker build -t lironefitoussi/sports-store-payment-service:latest services/payment-service
docker build -t lironefitoussi/sports-store-seed:latest            seed
docker build -f gateway/Dockerfile -t lironefitoussi/sports-store-gateway:latest .
```

```bash
docker login
for img in auth-service catalog-service cart-service order-service payment-service seed gateway; do
  docker push lironefitoussi/sports-store-$img:latest
done
```

### Local dev (minikube) — skip the push

Load images straight into minikube's node instead of pushing to Docker Hub:

```bash
minikube image load lironefitoussi/sports-store-auth-service:latest
minikube image load lironefitoussi/sports-store-catalog-service:latest
minikube image load lironefitoussi/sports-store-cart-service:latest
minikube image load lironefitoussi/sports-store-order-service:latest
minikube image load lironefitoussi/sports-store-payment-service:latest
minikube image load lironefitoussi/sports-store-seed:latest
minikube image load lironefitoussi/sports-store-gateway:latest
```

Or build straight against minikube's Docker daemon (no load step needed):

```bash
eval $(minikube docker-env)
# re-run the docker build commands above with that shell
```

## 2. Namespace + Secret

The Helm release reads the mongo root password from `app-secrets`
(`auth.existingSecret: app-secrets` in `k8s/mongodb/values.yaml`), so the
Secret must exist first:

```bash
kubectl apply -f k8s/00-namespace.yaml
kubectl apply -f k8s/01-secret.yaml
```

## 3. Install MongoDB via Helm

```bash
helm install mongo oci://registry-1.docker.io/bitnamicharts/mongodb \
  -n sports-store \
  -f k8s/mongodb/values.yaml
```

`fullnameOverride: mongo` in values.yaml makes the Service resolve at
`mongo.sports-store.svc.cluster.local` (short name `mongo` in-namespace) —
matches the `mongo` hostname used in `MONGO_URI` (`k8s/01-secret.yaml`),
same as the `mongo` service name in docker-compose. Auth is on
(`auth.enabled: true`), root credentials come from `app-secrets`.

## 4. Apply the app manifests

```bash
kubectl apply -f k8s/02-configmap.yaml
kubectl apply -f k8s/services/
kubectl apply -f k8s/03-gateway.yaml
kubectl apply -f k8s/04-seed-job.yaml
```

Wait for `auth`/`catalog`/`cart`/`order`/`payment` pods Ready (they gate on
Mongo the same way compose's `depends_on: condition: service_healthy` did,
via readiness probes on `/health`), then the seed Job runs once.

## 5. Reach the app

**minikube (recommended for dev)** — resolves node IP/port for you:

```bash
minikube service gateway -n sports-store --url
```

**Manual NodePort:**

```bash
kubectl -n sports-store get svc gateway   # note the NodePort, e.g. 31234
minikube ip                                # node IP
# open http://<minikube-ip>:<nodeport>
```

**Port-forward (works anywhere, no NodePort needed):**

```bash
kubectl -n sports-store port-forward svc/gateway 8080:80
# open http://localhost:8080
```

## Notes

- `gateway/nginx.conf` hardcodes upstream hostnames (`auth`, `catalog`,
  `cart`, `order`, `payment`) — the Service names in `k8s/services/*.yaml`
  must keep matching those, same constraint as in docker-compose.
- Secret/ConfigMap values are dev defaults from `.env.example`. Override
  `JWT_SECRET` and `mongodb-root-password`/`MONGO_URI` for anything beyond
  local/course use — see the override snippet at the top of
  `k8s/01-secret.yaml`.
- `mongodb-root-password` and `MONGO_URI` in `k8s/01-secret.yaml` must
  embed the same password (the chart reads the former, services read the
  latter) — nothing derives one from the other automatically.
- Uninstalling/reinstalling the Helm release: if you change the password
  after the first install, `helm upgrade` won't rotate an existing mongo
  user — either `helm uninstall mongo` and reinstall (drops data unless
  the PVC is kept) or update the password inside mongo directly.
