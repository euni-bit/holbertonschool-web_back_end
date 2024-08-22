#!/usr/bin/env python3
"""
Module containing the async_comprehension coroutine.
"""


import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Returns:
        list[float]: A list of 10 random float numbers.
    """
    return [number async for number in async_generator()]
