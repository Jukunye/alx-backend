#!/usr/bin/python3
""" FIFOCache module
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Represents an object that stores and retrieves items from a dictionary
    with a FIFO removal mechanism when the limit is reached.
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

        self.cache_data[key] = item
        if len(self.cache_data.items()) > self.MAX_ITEMS:
            result, _ = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(result))

    def get(self, key):
        """ Retrieve an item from the cache with the specified key.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
