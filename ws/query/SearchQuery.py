from typing import Dict, Any


class SearchQuery:
    def __init__(self, query: str, data_attribute: str):
        self._query = query
        self._data_attribute = data_attribute

    @property
    def query(self):
        return self._query

    @property
    def data_attribute(self):
        return self._data_attribute

    def __str__(self):
        return f"SearchQuery(query='{self.query}', data_attribute='{self.data_attribute}'"
