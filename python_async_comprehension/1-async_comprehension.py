#!/usr/bin/env python3
""" Module for coroutine called async_comprehension
that takes no arguments.. """
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:  # type: ignore
    """ Coroutine will collect 10 random numbers using an async
    comprehensing over async_generator, then return the 10 random numbers. """
    result = [x async for x in async_generator()]
    return result
