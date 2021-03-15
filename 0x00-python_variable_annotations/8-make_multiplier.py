#!/usr/bin/env python3
"""[make multiplier]
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """[make multiplier funtion]

    Args:
        multiplier (float): [multiplier]

    Returns:
        Callable[[float], float]: [a function that multiplies a
        float by multiplier]
    """
    return lambda x: x * multiplier
