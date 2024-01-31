#!/usr/bin/env python3

"""module containing LIFOCache class"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class that uses LIFO caching system"""

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(list(self.cache_data.keys())) == self.MAX_ITEMS:
                    last_key = self.cache_data.popitem()
                    print(f"DISCARD: {last_key[0]}")
            else:
                del self.cache_data[key]
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
