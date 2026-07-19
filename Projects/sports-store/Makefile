NAMESPACE  := sports-store
RELEASE    := mongo
CHART      := oci://registry-1.docker.io/bitnamicharts/mongodb
VALUES     := k8s/mongodb/values.yaml
LOCAL_PORT ?= 8080

.PHONY: apply namespace secret mongo configmap services gateway seed url destroy rebuild

# Apply K8s configs (idempotent, safe to re-run)
apply: namespace secret mongo configmap services gateway seed url

namespace:
	kubectl apply -f k8s/00-namespace.yaml

secret:
	kubectl apply -f k8s/01-secret.yaml

# Helm chart needs app-secrets (auth.existingSecret) to already exist
mongo: secret
	helm upgrade --install $(RELEASE) $(CHART) \
		-n $(NAMESPACE) \
		-f $(VALUES) \
		--wait

configmap:
	kubectl apply -f k8s/02-configmap.yaml

services: configmap mongo
	kubectl apply -f k8s/services/

gateway: services
	kubectl apply -f k8s/03-gateway.yaml

seed: services
	kubectl apply -f k8s/04-seed-job.yaml

# Expose the gateway on a fixed local port (override with LOCAL_PORT=<port>)
url: gateway
	@kubectl -n $(NAMESPACE) rollout status deployment/gateway
	@echo "Gateway available at http://localhost:$(LOCAL_PORT)"
	kubectl -n $(NAMESPACE) port-forward svc/gateway $(LOCAL_PORT):80

# Tear down everything: Helm release + whole namespace (cascades secrets,
# configmap, deployments, services, PVCs, the seed job).
destroy:
	-helm uninstall $(RELEASE) -n $(NAMESPACE)
	-kubectl delete namespace $(NAMESPACE) --wait=true

# One-shot: nuke and rebuild the entire stack from scratch.
rebuild: destroy apply
