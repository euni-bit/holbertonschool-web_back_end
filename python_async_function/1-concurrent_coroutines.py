#!/usr/bin/env python3
"""
Module for task 1-concurrent_coroutines.py
"""

import asyncio
from typing import List
from heapq import heappush, heappop

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawns `n` tasks to wait for random
    delays up to `max_delay` and returns a list of the
    delays in ascending order.
    """
    delays = []
    delay_queue = []

    async def wait_and_store_delay():
        """
        Asynchronously waits for a random
        delay and stores it in a priority queue.
        """
        delay = await wait_random(max_delay)
        heappush(delay_queue, delay)

    tasks = [wait_and_store_delay() for _ in range(n)]
    await asyncio.gather(*tasks)

    while delay_queue:
        delays.append(heappop(delay_queue))

    return delays
