import requests

from ws.conf.Config import Config
from ws.paginator.AbstractPaginator import AbstractPaginator
from ws.query.QueryExecutor import QueryExecutor


class IterationPaginator(AbstractPaginator):
    def __init__(self, config: Config):
        super().__init__(config)
        self._url_format = config.url + "?" + config.pagination_format
        self._data = []

    def get_data(self):
        iteration = 1
        response_data = self.__send_request(iteration)
        while not self._stop_condition.check(response_data):
            print(iteration)
            print(response_data)
            self._data.append(response_data)
            iteration = iteration + 1
            response_data = self.__send_request(iteration)

    def __send_request(self, iteration: int):
        response = requests.get(self._url_format % iteration)
        if response.status_code == 200:
            return QueryExecutor.execute(response, self._config.item)
        else:
            return []
