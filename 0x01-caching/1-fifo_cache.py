#!/usr/bin/env python3

"""module containing FIFOCache class"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class that uses FIFO caching system"""

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(list(self.cache_data.keys())) > self.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
