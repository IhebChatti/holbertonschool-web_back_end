#!/usr/bin/python3
"""[Rain]
"""


def rain(walls):
    """[rain function]

    Args:
        walls ([list]): [non-negative integers]

    Returns:
        [int]: [how much water will be retained after it rains]
    """
    n = len(walls)
    res = 0
    for i in range(1, n - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])
        right = walls[i]
        for j in range(i + 1, n):
            right = max(right, walls[j])
        res = res + (min(left, right) - walls[i])
    return res
