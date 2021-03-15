#!/usr/bin/env python3
"""[to_kv]
"""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """[a function that takes a str and union to return a tuple]

    Args:
        k (str): [first item of tuple]
        v (Union[int, float]): [second item of tuple]

    Returns:
        tuple: [result]
    """
    return (k, v**2)
