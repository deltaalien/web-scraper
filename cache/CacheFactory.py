from cache.BasicCache import BasicCache
from cache.Cache import Cache


class CacheFactory:
    __instances = {}

    @staticmethod
    def get(cache_type: str) -> Cache:
        if not CacheFactory.__instances.get(cache_type):
            CacheFactory.__instances[cache_type] = CacheFactory.__create(cache_type)

        return CacheFactory.__instances.get(cache_type)

    @staticmethod
    def __create(cache_type: str) -> Cache:
        if "BASIC" == cache_type:
            return BasicCache()
