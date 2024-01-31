#!/usr/bin/env python3

"""module containing LRUCache class"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class that uses LRU caching system"""

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(list(self.cache_data.keys())) > self.MAX_ITEMS:
                least_recenyl_used_key = list(self.cache_data.keys())[0]
                del self.cache_data[least_recenyl_used_key]
                print(f"DISCARD: {least_recenyl_used_key}")

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return self.cache_data[key]
        else:
            return None
