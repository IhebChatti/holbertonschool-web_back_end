#!/usr/bin/env python3
"""[summary]
"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """[Cache]
    """
    def __init__(self):
        """[__init__]
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """[store]

        Args:
            data (Union[str, bytes, int, float]): [data]

        Returns:
            str: [returns a generated random key]
        """
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key
