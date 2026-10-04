#!/usr/bin/env bash
set -euo pipefail
eval "$(minikube docker-env)"
docker build -t self-healing/demo-service:1.0 app/demo-service
docker build -t self-healing/ai-engine:1.0 ai-engine
docker build -t self-healing/remediation-engine:1.0 remediation-engine
kubectl apply -f kubernetes/demo-app/
kubectl apply -f kubernetes/ai-engine/
kubectl apply -f kubernetes/remediation-engine/
