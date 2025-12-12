#!/usr/bin/env python3
""" Module for multiple coroutines at the same time with async"""
import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async func that  that takes in 2 int arguments
    and spawn wait_random n times with the specified max_delay.
    """
    result = []
    tasks = []
    num = 0
    while num < n:
        tasks.append(task_wait_random(max_delay))
        num = num + 1
    for task in asyncio.as_completed(tasks):
        result_task = await task
        result.append(result_task)
    return result
