from fastapi import FastAPI
from pydantic import BaseModel
from analyzer import analyze
app=FastAPI(title="AI Incident Analyzer")
class Incident(BaseModel):
    symptom:str; namespace:str="self-healing"; workload:str="demo-service"
@app.get("/health")
def health(): return {"status":"healthy"}
@app.post("/analyze")
def incident(i:Incident):
    d=analyze(i.symptom); return {"incident":i.model_dump(),"diagnosis":d.__dict__}
