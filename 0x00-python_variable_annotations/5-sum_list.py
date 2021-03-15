#!/usr/bin/env python3
"""[sum of a list of floats]
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """[a function to compute the sum of a list of floats]

    Args:
        input_list (float): [list of floats]

    Returns:
        float: [sum of list items]
    """
    return sum(input_list)
