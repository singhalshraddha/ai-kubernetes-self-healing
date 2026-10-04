import os
import time
from fastapi import FastAPI, Response
from prometheus_client import Counter, generate_latest
app=FastAPI(title="Self-Healing Demo Service")
requests_total=Counter("demo_requests_total","Total demo requests")
@app.get("/")
def root():
    requests_total.inc(); return {"service":"demo-api","status":"healthy","timestamp":time.time()}
@app.get("/health")
def health():
    if os.getenv("FORCE_UNHEALTHY","false").lower()=="true":
        return Response(content='{"status":"unhealthy"}',status_code=503,media_type="application/json")
    return {"status":"healthy"}
@app.get("/metrics")
def metrics(): return Response(generate_latest(),media_type="text/plain")
@app.get("/version")
def version(): return {"version":os.getenv("APP_VERSION","1.0.0")}
