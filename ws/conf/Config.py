from typing import Type, Dict

from ws.query.SearchQuery import SearchQuery


class Config:
    def __init__(self, url: str, pagination_format: str, pagination_type: str, stop: str, extraction: str,
                 enable_caching: bool, item: SearchQuery, data: Dict[str, SearchQuery]):
        self._url = url
        self._pagination_format = pagination_format
        self._pagination_type = pagination_type
        self._stop = stop
        self._item = item
        self._extraction = extraction
        self._data = data
        self._enable_caching = enable_caching

    @property
    def url(self):
        return self._url

    @property
    def pagination_format(self):
        return self._pagination_format

    @property
    def pagination_type(self):
        return self._pagination_type

    @property
    def stop(self):
        return self._stop

    @property
    def extraction(self):
        return self._extraction

    @property
    def item(self):
        return self._item

    @property
    def data(self):
        return self._data

    @property
    def enable_caching(self):
        return self._enable_caching

    def __str__(self):
        data_str = ""
        for key, value in self._data.items():
            data_str += f"\n  {key}: element='{value.element}', data_attribute='{value.data_attribute}', attributes={value.attributes}"

        return f"Config(url='{self._url}', pagination_format='{self._pagination_format}', pagination_type='{self._pagination_type}', stop='{self._stop}', extraction='{self._extraction}', item='{self._item}', data={data_str})"
