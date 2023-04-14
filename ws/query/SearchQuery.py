from typing import Dict, Any


class SearchQuery:
    def __init__(self, element: str, data_attribute: str, attributes: Dict[str, Any]):
        self._element = element
        self._data_attribute = data_attribute
        self._attributes = attributes

    @property
    def element(self):
        return self._element

    @property
    def data_attribute(self):
        return self._data_attribute

    @property
    def attributes(self):
        return self._attributes.items()

    def __str__(self):
        return f"SearchQuery(element='{self.element}', data_attribute='{self.data_attribute}', " \
               f"attributes={self.attributes})"
