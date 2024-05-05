#!/usr/bin/env python3
"""
Module for pagination of a database(popular_baby_names.csv).
"""
import csv
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a given page and page size.

    Args:
    - page (int): The page number.
    - page_size (int): The number of items per page.

    Returns:
    - tuple[int, int]: A tuple containing the start and end indices.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


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
        """
        Retrieve a page of data with specified page number and page size.

        Args:
        - page (int): The page number (default is 1).
        - page_size (int): The number of items per page (default is 10).

        Returns:
        - List[List]: A list of lists representing the data
                        on the specified page.

        Raises:
        - IndexError: If the page number or page size is out of range.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        try:
            start, end = index_range(page, page_size)
            return self.dataset()[start:end]
        except IndexError:
            return []
