import gzip
import json
from typing import Dict, Optional

import GlobalConstants
from cache.Cache import Cache
from cache.CacheEntry import CacheEntry, CacheEntryEncoder


class BasicCache(Cache):
    FILE_LOCATION = GlobalConstants.PROJECT_ROOT + "/cache/data/basic_cache.gz"

    def __init__(self):
        self._map: Dict[str, CacheEntry] = {}
        self.__load_data()

    def save(self):
        json_data = json.dumps(self._map, cls=CacheEntryEncoder)
        compressed_data = gzip.compress(json_data.encode())

        with gzip.open(BasicCache.FILE_LOCATION, 'wb') as f:
            f.write(compressed_data)

    def get(self, key) -> Optional[str]:
        if key in self._map:
            return self._map[key].data()
        else:
            return None

    def set(self, key: str, value: str):
        if key in self._map:
            self._map[key].update(value)
        else:
            self._map[key] = CacheEntry.from_string(value)

    def delete(self, key: str):
        if key in self._map:
            del self._map[key]

    def clear(self):
        self._map = {}
        self.save()

    def __load_data(self):
        with gzip.open(BasicCache.FILE_LOCATION) as f:
            content = f.read()
            if not content:
                return
            cache_data = gzip.decompress(content)
            json_data_dic = json.loads(cache_data)

            for key in json_data_dic:
                data = CacheEntry.from_json(json_data_dic[key])
                self._map[key] = data
