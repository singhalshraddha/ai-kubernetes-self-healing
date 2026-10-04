# AI Kubernetes Self-Healing Platform

An end-to-end DevOps project that detects Kubernetes application failures with Prometheus, analyzes incidents with an AI-ready Python engine, and applies safe automated remediation through the Kubernetes API.

## Architecture
Prometheus -> Alerting -> AI Engine -> Remediation Engine -> Kubernetes API -> Recovery -> Metrics

## Features
- FastAPI demo workload with health and metrics endpoints
- Prometheus monitoring and alert rules
- AI-ready incident analyzer with deterministic fallback rules
- Kubernetes remediation engine with guardrails
- Helm deployment
- Docker images
- Pytest unit tests
- GitHub Actions CI and Trivy security scan
- Failure injection and recovery scripts

## Quick start
Prerequisites: Docker, kubectl, Minikube, Helm, Python 3.11+.

```bash
minikube start
./scripts/setup.sh
./scripts/deploy.sh
kubectl get pods -n self-healing
minikube service demo-service -n self-healing
```

Induce a health failure:
```bash
./scripts/induce-failure.sh
```

## Resume bullet
Built an AI-assisted Kubernetes self-healing platform using Python, Docker, Kubernetes, Prometheus, Helm and CI/CD to detect failures, diagnose incidents and automatically remediate unhealthy workloads.
