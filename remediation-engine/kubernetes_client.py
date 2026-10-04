from kubernetes import client,config
from datetime import datetime

def load():
    try: config.load_incluster_config()
    except config.ConfigException: config.load_kube_config()
def restart_deployment(name,namespace):
    load(); api=client.AppsV1Api(); d=api.read_namespaced_deployment(name,namespace)
    a=d.spec.template.metadata.annotations or {}; a["self-healing/restarted-at"]=datetime.utcnow().isoformat(); d.spec.template.metadata.annotations=a
    api.patch_namespaced_deployment(name,namespace,d)
def scale_deployment(name,namespace,replicas):
    load(); client.AppsV1Api().patch_namespaced_deployment_scale(name,namespace,{"spec":{"replicas":max(1,min(replicas,10))}})
