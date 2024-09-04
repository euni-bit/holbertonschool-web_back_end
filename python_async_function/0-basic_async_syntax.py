#!/usr/bin/env python3
"""
Module for task 0-basic_async_syntax.py
"""

import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay
    """
    random_float = __import__('random').uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
