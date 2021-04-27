#!/usr/bin/env python3
"""[summary]
"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable


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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """[convert the data back to the desired format]

        Args:
            key (str): [key]
            fn (Optional[Callable], optional): [Callable]. Defaults to None.

        Returns:
            Union[str, bytes, int, float]: [data returned]
        """
        result = self._redis.get(key)
        if fn:
            return fn(result)
        return result

    def get_str(self, data: bytes) -> str:
        """[get_str]

        Args:
            data (bytes): [data to convert to str]

        Returns:
            str: [converted data]
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """[get_int]

        Args:
            data (bytes): [data to be converted to int]

        Returns:
            int: [converted data]
        """
        return int.from_bytes(data, sys.byteorder)
