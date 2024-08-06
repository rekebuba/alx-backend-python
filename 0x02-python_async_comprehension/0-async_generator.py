#!/usr/bin/env python3
"""Async Generator"""

import random
import asyncio


async def async_generator():
    """Async Generator

    Returns:
        Generator[float, None, None]

    Yields:
        Iterator[Generator[float, None, None]]
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
