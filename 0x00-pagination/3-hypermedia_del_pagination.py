#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List
from typing import Dict


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
        Get a hyper index of data from the dataset starting from the specified index.

        Args:
            index (int, optional): The starting index. If not specified, defaults to 0.
            page_size (int, optional): The number of items per page. Defaults to 10.

        Returns:
            Dict: A dictionary containing the 'index', 'data', 'page_size', and 'next_index'.
                - 'index' (int): The starting index of the returned data.
                - 'data' (List): A list of data items from the dataset.
                - 'page_size' (int): The number of items returned in this page.
                - 'next_index' (int or None): The index to start the next page from,
                or None if there are no more pages.
        """
        dataset = self.indexed_dataset()
        data_length = len(dataset)
        index = index or 0
        assert isinstance(index, int) and index >= 0

        dictionary = {}
        dictionary['index'] = index
        dictionary['data'] = [dataset[i] for i in range(index, min(
            index + page_size, data_length)) if dataset.get(i) is not None]
        dictionary['page_size'] = len(dictionary['data'])
        dictionary['next_index'] = index + dictionary['page_size'] if index + \
            dictionary['page_size'] < data_length else None

        return dictionary
