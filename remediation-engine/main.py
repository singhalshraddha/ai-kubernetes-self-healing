from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from remediation import validate_action
from kubernetes_client import restart_deployment,scale_deployment
app=FastAPI(title="Kubernetes Remediation Engine")
class Remediation(BaseModel):
    action:str; workload:str; namespace:str="self-healing"; replicas:int=2
@app.get("/health")
def health(): return {"status":"healthy"}
@app.post("/remediate")
def remediate(r:Remediation):
    if not validate_action(r.action): raise HTTPException(400,"Unsupported remediation action")
    if r.namespace!="self-healing": raise HTTPException(403,"Namespace outside safety boundary")
    if r.action=="restart": restart_deployment(r.workload,r.namespace)
    elif r.action=="scale": scale_deployment(r.workload,r.namespace,r.replicas)
    return {"status":"accepted","action":r.action,"workload":r.workload}
