NAMESPACE  := sports-store
RELEASE    := mongo
CHART      := oci://registry-1.docker.io/bitnamicharts/mongodb
VALUES     := k8s/mongodb/values.yaml
LOCAL_PORT ?= 8080
BUILD_FLAGS ?=

.PHONY: apply images build-images push-images load-images namespace secret mongo-init mongo configmap services gateway url destroy rebuild

# Build every application image with the exact tags used by the manifests.
build-images:
	docker build $(BUILD_FLAGS) -t lironefitoussi/sports-store-auth-service:latest services/auth-service
	docker build $(BUILD_FLAGS) -t lironefitoussi/sports-store-catalog-service:latest services/catalog-service
	docker build $(BUILD_FLAGS) -t lironefitoussi/sports-store-cart-service:latest services/cart-service
	docker build $(BUILD_FLAGS) -t lironefitoussi/sports-store-order-service:latest services/order-service
	docker build $(BUILD_FLAGS) -t lironefitoussi/sports-store-payment-service:latest services/payment-service
	docker build $(BUILD_FLAGS) -f gateway/Dockerfile -t lironefitoussi/sports-store-gateway:latest .

# Publish every application image using the tags referenced by Kubernetes.
push-images:
	docker push lironefitoussi/sports-store-auth-service:latest
	docker push lironefitoussi/sports-store-catalog-service:latest
	docker push lironefitoussi/sports-store-cart-service:latest
	docker push lironefitoussi/sports-store-order-service:latest
	docker push lironefitoussi/sports-store-payment-service:latest
	docker push lironefitoussi/sports-store-gateway:latest

# Minikube has its own image store. --overwrite prevents IfNotPresent from
# retaining an older image that happens to have the same :latest tag.
load-images:
	minikube status
	docker save lironefitoussi/sports-store-auth-service:latest | minikube image load --overwrite=true -
	docker save lironefitoussi/sports-store-catalog-service:latest | minikube image load --overwrite=true -
	docker save lironefitoussi/sports-store-cart-service:latest | minikube image load --overwrite=true -
	docker save lironefitoussi/sports-store-order-service:latest | minikube image load --overwrite=true -
	docker save lironefitoussi/sports-store-payment-service:latest | minikube image load --overwrite=true -
	docker save lironefitoussi/sports-store-gateway:latest | minikube image load --overwrite=true -

images:
	$(MAKE) build-images
	$(MAKE) push-images
	$(MAKE) load-images

# Apply K8s configs (idempotent, safe to re-run)
apply: namespace secret mongo configmap services gateway url

namespace:
	kubectl apply -f k8s/00-namespace.yaml

secret: namespace
	kubectl apply -f k8s/01-secret.yaml

# Generate the Mongo first-boot scripts ConfigMap from the shared Compose source.
mongo-init: namespace
	kubectl create configmap mongo-init-scripts \
		-n $(NAMESPACE) \
		--from-file=init-mongo.js=seed/init-mongo.js \
		--dry-run=client -o yaml | kubectl apply -f -

# Helm chart needs app-secrets and mongo-init-scripts to already exist.
mongo: secret mongo-init
	helm upgrade --install $(RELEASE) $(CHART) \
		-n $(NAMESPACE) \
		-f $(VALUES) \
		--wait

configmap: namespace
	kubectl apply -f k8s/02-configmap.yaml

services: configmap mongo
	kubectl apply -f k8s/services/

gateway: services
	kubectl apply -f k8s/03-gateway.yaml

# Expose the gateway on a fixed local port (override with LOCAL_PORT=<port>)
url: gateway
	@kubectl -n $(NAMESPACE) rollout status deployment/gateway
	@echo "Gateway available at http://localhost:$(LOCAL_PORT)"
	kubectl -n $(NAMESPACE) port-forward svc/gateway $(LOCAL_PORT):80

# Tear down everything: Helm release + whole namespace (cascades secrets,
# configmap, deployments, services, and PVCs).
destroy:
	-helm uninstall $(RELEASE) -n $(NAMESPACE)
	-kubectl delete namespace $(NAMESPACE) --wait=true

# Build, publish, and load first so a failure does not tear down the running
# stack. Only recreate Kubernetes after every image operation succeeds.
rebuild:
	$(MAKE) build-images BUILD_FLAGS="--pull --no-cache"
	$(MAKE) push-images
	$(MAKE) load-images
	$(MAKE) destroy
	$(MAKE) apply
