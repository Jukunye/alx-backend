#!/usr/bin/python3
""" LFUCache module
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Represents an object that stores and retrieves items from a dictionary
    with a LFU removal mechanism when the limit is reached.
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.access_count = {}

    def put(self, key, item):
        """ Add an item to the cache with the specified key.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.access_count[key] += 1
        else:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                min_accessed = min(self.access_count.values())
                least_accessed = [
                    key for key, value in self.access_count.items(
                    ) if value == min_accessed
                ]
                if len(least_accessed) > 1:
                    small_dict = OrderedDict(
                        (key, self.cache_data[key]) for key in least_accessed)
                    last_key, _ = small_dict.popitem(last=False)
                    print("DISCARD:", last_key)
                    del self.cache_data[last_key]
                    del self.access_count[last_key]
                else:
                    print("DISCARD:", least_accessed[0])
                    del self.access_count[least_accessed[0]]
                    del self.cache_data[least_accessed[0]]
            self.cache_data[key] = item
            self.access_count[key] = 0

    def get(self, key):
        """ Retrieve an item from the cache with the specified key.
        """
        if key in self.cache_data:
            self.access_count[key] += 1
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
