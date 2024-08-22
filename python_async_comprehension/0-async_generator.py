#!/usr/bin/env python3
"""
This module provides utility functions for handling asynchronous tasks.
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates a sequence of random numbers between 0 and 10.

    Yields:
        A random float between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
