#!/usr/bin/env python3
""" Module for  function named index_range that return a tuple """
import asyncio
import random
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Function should return a tuple of size two containing
    a start index and an end index corresponding to the range
    of indexes.
    """
    if page == 1:
        start = 0
    start = (page - 1)*page_size
    end = page * page_size
    return (start, end)
