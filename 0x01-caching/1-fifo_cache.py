#!/usr/bin/env python3

"""module containing FIFOCache class"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class that uses FIFO caching system"""

    def put(self, key, item):
        """puts a cache item in cache_data attribute using FIFO policy"""
        if key is not None and item is not None:
            if len(list(self.cache_data.keys())) > self.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")
            self.cache_data[key] = item

    def get(self, key):
        """gets a cache item from cache_data by key"""
        if key is not None and key in list(self.cache_data.keys()):
            return self.cache_data[key]
        return None
