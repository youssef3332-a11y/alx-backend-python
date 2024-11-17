#!/usr/bin/env python3
"""takes a float a and a float b as arguments and returns their sum"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """wait for max_delay seconds"""
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
