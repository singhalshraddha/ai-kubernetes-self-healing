ALLOWED_ACTIONS={"restart","scale","observe"}
def validate_action(action:str)->bool: return action in ALLOWED_ACTIONS
