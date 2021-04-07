#!/usr/bin/env python3
"""[Auth]
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """[Auth]
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """[require_auth]
        """
        if not path or not excluded_paths or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        for ex_path in excluded_paths:
            if ex_path[-1] == "*" and path.startswith(ex_path[:-1]):
                return False
        if path in excluded_paths:
            return False
        else:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """[authorization_header]
        """
        if request:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """[current_user]
        """
        return None

    def session_cookie(self, request=None):
        """[session_cookie]

        Args:
            request ([type], optional): [request module]. Defaults to None.

        Returns:
            [type]: [cookie by session name]
        """
        if request:
            session_name = getenv("SESSION_NAME")
            return request.cookies.get(session_name, None)
