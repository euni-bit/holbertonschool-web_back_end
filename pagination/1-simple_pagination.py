#!/usr/bin/env python3
"""Simple Pagination."""
import csv
import math
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate the start and end indexes for a given page and page size."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


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
        """Get page."""
        self.dataset()
        for i in [page, page_size]:
            assert isinstance(i, int) and page > 0
        assert page_size > 0
        range_i = index_range(page, page_size)
        return self.__dataset[range_i[0]:range_i[1]]
