#!/usr/bin/env python3

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """[async_generator function]

    Yields:
        Generator[float, None, None]: [generator from typing module]
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
