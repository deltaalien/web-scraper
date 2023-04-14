from bs4 import BeautifulSoup
from requests import Response

from ws.query.SearchQuery import SearchQuery


class QueryExecutor:
    @staticmethod
    def execute(response: Response, query: SearchQuery):
        soup = BeautifulSoup(response.content, 'html.parser')
        elements = soup.find_all(query.element, attrs=query.attributes)

        if query.data_attribute:
            data = [element.get(query.data_attribute) for element in elements]
        else:
            data = elements
        return data
