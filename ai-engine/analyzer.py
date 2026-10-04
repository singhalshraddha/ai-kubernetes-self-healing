from dataclasses import dataclass
@dataclass
class Diagnosis:
    category:str; confidence:float; reason:str; action:str
RULES={
"CrashLoopBackOff":Diagnosis("container_crash",.95,"Container is repeatedly restarting.","restart"),
"OOMKilled":Diagnosis("memory_exhaustion",.92,"Container exceeded its memory limit.","increase_memory"),
"Unhealthy":Diagnosis("health_check_failure",.90,"Health checks are failing.","restart")}
def analyze(symptom:str)->Diagnosis:
    for key,value in RULES.items():
        if key.lower() in symptom.lower(): return value
    return Diagnosis("unknown",.50,"No high-confidence rule matched.","observe")
