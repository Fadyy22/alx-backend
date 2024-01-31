#!/usr/bin/env python3

"""module containing LIFOCache class"""

from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class that uses LIFO caching system"""

    def __init__(self):
        """constructor function"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(list(self.cache_data.keys())) + 1 > self.MAX_ITEMS:
                    last_key = self.cache_data.popitem(True)
                    print(f"DISCARD: {last_key[0]}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, True)

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
