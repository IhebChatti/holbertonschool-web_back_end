#!/usr/bin/env python3
"""[encrypt pw]
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """[hash_password]

    Args:
        password ([type]): [pw]

    Returns:
        bytes: [byte string]
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())



def is_valid(hashed_password: bytes, password: str) -> bool:
    """[is_valid]

    Args:
        hashed_password (bytes): [hashed pw]
        password (str): [pw]

    Returns:
        bool: [either valid or not]
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
