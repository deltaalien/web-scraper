import json
import time
from datetime import datetime


class CacheEntry:
    def __init__(self, data: str, timestamp: int):
        self._data = data
        self._timestamp = timestamp

    def __getstate__(self):
        return {'data': self._data, 'timestamp': self._timestamp}

    def __setstate__(self, state):
        self._data = state['data']
        self._timestamp = state['timestamp']

    @classmethod
    def from_json(cls, json_data):
        return cls(json_data['data'], int(json_data['timestamp']))

    @classmethod
    def from_string(cls, data: str):
        timestamp = int(time.time_ns() / 1000)

        return cls(data, timestamp)

    def validate(self, data: str):
        return self._data == data

    def update(self, data: str):
        if len(data) == 0:
            return

        self._data = data
        self._timestamp = int(time.time_ns() / 1000)

    def timestamp(self):
        return self._timestamp

    def data(self):
        return self._data

    def __str__(self):
        return f"CacheEntry(data='{self._data}', timestamp={self._timestamp})"


class CacheEntryEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, CacheEntry):
            return {'data': o.data(), 'timestamp': o.timestamp()}
        elif isinstance(o, datetime):
            return o.isoformat()
        else:
            return super().default(o)
