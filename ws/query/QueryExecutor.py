from bs4 import BeautifulSoup, Tag
from requests import Response

from ws.query.SearchQuery import SearchQuery


class QueryExecutor:
    @staticmethod
    def execute(response: Response, query: SearchQuery):
        soup = BeautifulSoup(response.content, 'html.parser')
        return QueryExecutor.__execute(soup, query)

    @staticmethod
    def execute_tag(tag: Tag, query: SearchQuery):
        soup = BeautifulSoup(tag.prettify(), 'html.parser')
        return QueryExecutor.__execute(soup, query)

    @staticmethod
    def __execute(soup: BeautifulSoup, query: SearchQuery):
        elements = soup.find_all(query.element, attrs=query.attributes)

        if len(query.data_attribute) != 0:
            data = [element.get(query.data_attribute) for element in elements]
        else:
            data = elements
        return data
