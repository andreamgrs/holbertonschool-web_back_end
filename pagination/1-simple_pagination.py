#!/usr/bin/env python3
""" Module for  function named index_range that return a tuple """
import asyncio
import random
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            assert page > 0
            assert page_size > 0
            
            
            start, end = index_range(page, page_size)


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
