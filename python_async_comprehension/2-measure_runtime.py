#!/usr/bin/env python3
""" Module for coroutine that will execute async_comprehension
four times in parallel using asyncio.gather. """
import asyncio
from typing import List
import time
async_comprehension = __import__('1-async_comprehension').async_generator


async def measure_runtime() -> float:
    """ Measure_runtime should measure the total runtime and return it. """
    start = time.time()

    tasks = async_comprehension()
    for i in range(4):
        await asyncio.sleep(2.5)
    end = time.time()
    return end - start
