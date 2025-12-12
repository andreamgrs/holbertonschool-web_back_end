#!/usr/bin/env python3
""" Module for multiple coroutines at the same time with async"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async func that  that takes in 2 int arguments
    and spawn wait_random n times with the specified max_delay.
    """
    result = []
    num = 0
    while num < n:
        result.append(wait_random(max_delay))
        num = num + 1
    return await asyncio.gather(*result)
