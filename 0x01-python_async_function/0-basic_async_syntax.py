#!/usr/bin/env python3
"""[wait_random]
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """[wait_random async funtion]

    Args:
        max_delay (int, optional): [max delay]. Defaults to 10.

    Returns:
        float: [returns random number]
    """
    rand = random.random() * max_delay
    await asyncio.sleep(rand)
    return rand
