#!/usr/bin/env python3
"""[task_wait_n]
"""

import asyncio
import random
from typing import List

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """[task_wait_n async func]

    Args:
        n (int): [number]
        max_delay (int): [max delay]

    Returns:
        List[float]: [returned list]
    """
    delay_lst = [task_wait_random(max_delay) for _ in range(n)]
    return [await item for item in asyncio.as_completed(delay_lst)]
