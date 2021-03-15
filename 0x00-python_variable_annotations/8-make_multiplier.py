#!/usr/bin/env python3
"""[summary]
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda x: x * multiplier
