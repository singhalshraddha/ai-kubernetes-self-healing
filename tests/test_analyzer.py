from ai_engine.analyzer import analyze
def test_crashloop():
    r=analyze("CrashLoopBackOff")
    assert r.action=="restart"
    assert r.confidence>.9
def test_unknown():
    assert analyze("unknown").action=="observe"
