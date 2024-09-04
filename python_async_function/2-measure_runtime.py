#!/usr/bin/env python3
"""
Module for task 2-measure_runtime.py
"""

import asyncio
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for
    wait_n(n, max_delay), and returns total_time / n
    """
    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time() - start_time
    return end_time / n
