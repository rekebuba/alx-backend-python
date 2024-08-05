#!/usr/bin/env python3
"""multiple coroutines at the same time with async"""
import asyncio
import heapq
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """multiple coroutines at the same time with async

    Args:
        n (int): spawn wait_random n times with the specified max_delay.
        max_delay (int):

    Returns:
        List[float]: return the list of all the delays (float values).
        The list of the delays should be in ascending order
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delay = await asyncio.gather(*tasks)
    return list(heapq.nsmallest(n, delay))
