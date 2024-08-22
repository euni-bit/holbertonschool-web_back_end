#!/usr/bin/env python3 
"""
Module with the measure_runtime coroutine.
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for number in range(4)))
    end = time.time()
    return end - start
