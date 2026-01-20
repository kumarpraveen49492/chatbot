SESSIONS = {}

def get_session(user_id):
    return SESSIONS.get(user_id)

def create_session(user_id, stage):
    SESSIONS[user_id] = {
        "stage": stage,
        "data": {}
    }

def update_stage(user_id, stage):
    if user_id in SESSIONS:
        SESSIONS[user_id]["stage"] = stage

def clear_session(user_id):
    SESSIONS.pop(user_id, None)
