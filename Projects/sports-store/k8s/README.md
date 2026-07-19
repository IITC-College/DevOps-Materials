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
  services/               # auth, catalog, cart, order, payment — Deployment + Service each
  mongodb/values.yaml    # Helm values for the Bitnami mongodb chart
```

The shared first-boot data script lives at `seed/init-mongo.js` in the project
root. Docker Compose mounts it directly; Kubernetes generates a
`mongo-init-scripts` ConfigMap from the same file.

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
docker build -f gateway/Dockerfile -t lironefitoussi/sports-store-gateway:latest .
```

```bash
docker login
for img in auth-service catalog-service cart-service order-service payment-service gateway; do
  docker push lironefitoussi/sports-store-$img:latest
done
```

### Local dev (minikube) — skip the push

Load images straight into minikube's node instead of pushing to Docker Hub:

```bash
docker save lironefitoussi/sports-store-auth-service:latest | minikube image load --overwrite=true -
docker save lironefitoussi/sports-store-catalog-service:latest | minikube image load --overwrite=true -
docker save lironefitoussi/sports-store-cart-service:latest | minikube image load --overwrite=true -
docker save lironefitoussi/sports-store-order-service:latest | minikube image load --overwrite=true -
docker save lironefitoussi/sports-store-payment-service:latest | minikube image load --overwrite=true -
docker save lironefitoussi/sports-store-gateway:latest | minikube image load --overwrite=true -
```

The explicit `docker save` stream guarantees Minikube receives the locally
built image bytes instead of resolving the same `:latest` tag from a registry
or retaining an older runtime image.

Or build straight against minikube's Docker daemon (no load step needed):

```bash
eval $(minikube docker-env)
# re-run the docker build commands above with that shell
```

The Makefile wraps the local workflow:

```bash
make build-images  # build all six images locally
make push-images   # push all six images to Docker Hub
make load-images   # overwrite Minikube's cached copies
make images        # build, push, and load all six images
make rebuild       # force-build, push, load, and recreate the entire stack
```

`make rebuild` completes every image build, registry push, and Minikube load
before deleting the current namespace. This prevents a build, authentication,
network, or registry failure from taking down a working local deployment. Run
`docker login` first when the Docker client is not already authenticated.

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
kubectl create configmap mongo-init-scripts \
  -n sports-store \
  --from-file=init-mongo.js=seed/init-mongo.js \
  --dry-run=client -o yaml | kubectl apply -f -

helm install mongo oci://registry-1.docker.io/bitnamicharts/mongodb \
  -n sports-store \
  -f k8s/mongodb/values.yaml
```

`fullnameOverride: mongo` in values.yaml makes the Service resolve at
`mongo.sports-store.svc.cluster.local` (short name `mongo` in-namespace) —
matches the `mongo` hostname used in `MONGO_URI` (`k8s/01-secret.yaml`),
same as the `mongo` service name in docker-compose. Auth is on
(`auth.enabled: true`), root credentials come from `app-secrets`.

`initdbScriptsConfigMap: mongo-init-scripts` tells the chart to mount the seed
script through a ConfigMap. MongoDB runs it only when initializing an empty
data directory; upgrades and pod restarts do not overwrite existing catalog or
user data.

## 4. Apply the app manifests

```bash
kubectl apply -f k8s/02-configmap.yaml
kubectl apply -f k8s/services/
kubectl apply -f k8s/03-gateway.yaml
```

Wait for `auth`/`catalog`/`cart`/`order`/`payment` pods Ready (they gate on
Mongo the same way compose's `depends_on: condition: service_healthy` did,
via readiness probes on `/health`). The initial catalog and admin user are
created as part of MongoDB's first startup.

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
