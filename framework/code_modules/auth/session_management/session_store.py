class SessionStore:

    def __init__(self):
        self.sessions = {}

    def create_session(
        self,
        user_id: str
    ):
        self.sessions[user_id] = {}

    def get_session(
        self,
        user_id: str
    ):
        return self.sessions.get(user_id)
