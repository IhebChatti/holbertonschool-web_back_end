#!/usr/bin/env python3
"""[web.py]"""

import requests


def get_page(url: str) -> str:
    """[get_page]
    """
    req = requests.get(url)
    return req.content
