#!/usr/bin/env python3
"""
Module for pagination of a database(popular_baby_names.csv).
"""
import csv
import math
from typing import List
from typing import Tuple
from typing import Dict


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
    Get a hypermedia representation for pagination.

    Args:
    - page (int): The page number (default is 1).
    - page_size (int): The number of items per page (default is 10).

    Returns:
    - Dict: A dictionary containing the hypermedia representation
            including page size, page number, data for the page,
            next page number (if available), previous page number
            (if available), and total number of pages.
    """
        size = len(self.dataset())
        total_pages = math.ceil(size / page_size)
        next_page = page + 1 if (page + 1) <= total_pages else None
        prev_page = page - 1 if (page - 1) > 0 else None
        data = self.get_page(page, page_size)

        return {"page_size": page_size,
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
                }
