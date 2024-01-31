#!/usr/bin/env python3

"""module containing LRUCache class"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class that uses LRU caching system"""

    def __init__(self):
        """constructor function"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(list(self.cache_data.keys())) > self.MAX_ITEMS:
                least_recently_used_key = self.cache_data.popitem(False)
                print(f"DISCARD: {least_recently_used_key[0]}")

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, True)
            return self.cache_data[key]
        else:
            return None
