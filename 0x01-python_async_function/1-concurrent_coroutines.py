#!/usr/bin/env python3
"""[wait_n]
"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """[wait_n async func]

    Args:
        n (int): [number]
        max_delay (int): [max delay]

    Returns:
        List[float]: [returned list]
    """
    delay_lst = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await item for item in asyncio.as_completed(delay_lst)]
