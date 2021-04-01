#!/usr/bin/env python3
"""[Basic Auth]
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """[BasicAuth]
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """[extract_base64_authorization_header]

        Args:
            authorization_header (str): [auth header]

        Returns:
            str: [Base64 part of the Authorization header]
        """
        if not authorization_header or not isinstance(authorization_header,
                                                      str):
            return None
        if authorization_header.split(' ')[0] != 'Basic':
            return None
        return authorization_header.split(' ')[1]
