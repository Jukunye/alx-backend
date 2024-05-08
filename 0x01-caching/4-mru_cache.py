#!/usr/bin/python3
""" MRUCache module
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Represents an object that stores and retrieves items from a dictionary
    with a MRU removal mechanism when the limit is reached.
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache with the specified key.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem()
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """ Retrieve an item from the cache with the specified key.
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
