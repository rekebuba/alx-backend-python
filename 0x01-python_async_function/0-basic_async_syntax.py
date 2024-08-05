#!/usr/bin/env python3
"""The basics of async"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay

    Args:
        max_delay (int, optional): Defaults to 10.

    Returns:
        float: the random value
    """
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
