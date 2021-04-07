#!/usr/bin/env python3
"""[Session Auth]
"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """[SessionAuth]
    """
    user_id_by_session_id = {}
    def create_session(self, user_id: str = None) -> str:
        """[create_session]

        Args:
            user_id (str, optional): [user id]. Defaults to None.

        Returns:
            str: [session_id]
        """
        if not user_id or isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
