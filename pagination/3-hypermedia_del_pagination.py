#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dict with hypermedia-style pagination
        using index-based access.
        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.indexed_dataset()  # dict: {original_index: row}
        max_index = max(dataset.keys())

        # Filtrar las filas logic index  >= index
        sorted_keys = sorted(dataset.keys())
        valid_keys = [key for key in sorted_keys if key >= index]

        # Obtener los primeros page_size elem
        page_keys = valid_keys[:page_size]
        data = [dataset[key] for key in page_keys]

        # Calcular next_index
        if len(page_keys) == 0:
            next_index = None
        else:
            last_key = page_keys[-1]
            # Buscar el siguiente index logic available
            remaining_keys = [k for k in sorted_keys if k > last_key]
            next_index = remaining_keys[0] if remaining_keys else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
