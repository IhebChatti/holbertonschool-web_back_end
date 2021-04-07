#!/usr/bin/env python3
"""[Session Auth]
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


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
        if not user_id or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """[user_id_for_session_id]

        Args:
            session_id (str, optional): [session id]. Defaults to None.

        Returns:
            str: [user by session id]
        """
        if not session_id or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None):
        """[current_user]

        Args:
            request ([type], optional): [request module]. Defaults to None.

        Returns:
            [type]: [current user]
        """
        session_id = self.session_cookie(request)
        return User.get(self.user_id_for_session_id(session_id))
