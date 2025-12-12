#!/usr/bin/env python3
""" Module for  function named index_range that return a tuple """
import asyncio
import random


def index_range(max_delay: int = 10) -> float:
    """
    Async func that waits for a random delay between
    0 and max_delay (included and float value) seconds
    and eventually returns it.
    """
    delay = random.uniform(0.0, max_delay)
    await asyncio.sleep(delay)
    return delay
