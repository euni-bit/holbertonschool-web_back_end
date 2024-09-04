#!/usr/bin/env python3
"""
Module for task 4-tasks.py
"""

import asyncio
from typing import List
from heapq import heappush, heappop

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
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
        delay = await task_wait_random(max_delay)
        heappush(delay_queue, delay)

    tasks = [wait_and_store_delay() for _ in range(n)]
    await asyncio.gather(*tasks)

    while delay_queue:
        delays.append(heappop(delay_queue))

    return delays
