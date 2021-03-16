#!/usr/bin/env python3
"""[measure_time]
"""

import asyncio
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """[measure_time function]

    Args:
        n (int): [number]
        max_delay (int): [max delay]

    Returns:
        float: [returned value]
    """
    pc = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = perf_counter() - pc
    return elapsed_time
