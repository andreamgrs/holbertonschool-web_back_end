#!/usr/bin/env python3
""" Module for  function named index_range that return a tuple """
import csv
from typing import Any, Dict, List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached Dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Docstring for get_page
        :param self: Description
        :param page: Description
        :type page: int
        :param page_size: Description
        :type page_size: int
        :return: Description
        :rtype: List[List]
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        database = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(database):
            []
        return database[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Docstring for get_hyper
        :param self: Description
        :param page: Description
        :type page: int
        :param page_size: Description
        :type page_size: int
        :return: Description
        :rtype: List[List]
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        database = self.dataset()
        total_items = len(database)
        start, end = index_range(page, page_size)

        if start >= total_items:
            data = []
        else:
            data = database[start:end]
        # division entera sin decimales
        total_pages = (total_items + page_size - 1) // page_size

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if end < total_items else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }


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
