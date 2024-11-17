#!/usr/bin/env python3
"""measure_runtime"""
import asyncio
from time import perf_counter
from typing import Any
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures executing async_comprehension 4 times in parallel."""
    start_time = perf_counter()  # Start the timer
    # Run 4 instances of async_comprehension concurrently
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = perf_counter()  # Stop the timer
    return end_time - start_time
