#!/usr/bin/env python3

"""module containing LIFOCache class"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class that uses LIFO caching system"""

    def put(self, key, item):
        """puts a cache item in cache_data attribute using LIFO policy"""
        if key is not None and item is not None:
            if len(list(self.cache_data.keys())) > self.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-1]
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")
            self.cache_data[key] = item

    def get(self, key):
        """gets a cache item from cache_data by key"""
        if key is not None and key in list(self.cache_data.keys()):
            return self.cache_data[key]
        return None
