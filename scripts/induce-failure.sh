#!/usr/bin/env bash
set -euo pipefail
kubectl set env deployment/demo-service FORCE_UNHEALTHY=true -n self-healing
echo "Failure injected: health checks will fail."
