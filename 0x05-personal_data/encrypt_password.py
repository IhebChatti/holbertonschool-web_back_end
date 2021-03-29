#!/usr/bin/env python3
"""[encrypt pw]
"""

import bcrypt


def hash_password(password) -> bytes:
    """[hash_password]

    Args:
        password ([type]): [pw]

    Returns:
        bytes: [byte string]
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
