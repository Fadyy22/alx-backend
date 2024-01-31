#!/usr/bin/env python3

"""module containing FIFOCache class"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class that uses FIFO caching system"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(list(self.cache_data.keys())) > self.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

    def get(self, key):
        if key is not None and key in list(self.cache_data.keys()):
            return self.cache_data[key]
        return None
