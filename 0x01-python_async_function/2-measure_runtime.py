#!/usr/bin/env python3
"""Measure the runtime"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay)

    Args:
        n (int): spawn wait_random n times with the specified max_delay.
        max_delay (int):

    Returns:
        float: time_taken / n
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
