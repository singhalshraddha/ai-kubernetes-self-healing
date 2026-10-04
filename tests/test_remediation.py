from remediation_engine.remediation import validate_action
def test_allowed(): assert validate_action("restart")
def test_rejected(): assert not validate_action("delete_cluster")
