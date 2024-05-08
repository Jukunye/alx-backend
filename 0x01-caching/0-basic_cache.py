#!/usr/bin/python3
""" BaseCaching module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Provides a simple implementation of a cache.
    """

    def put(self, key, item):
        """ Add an item to the cache with the specified key.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache with the specified key.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
