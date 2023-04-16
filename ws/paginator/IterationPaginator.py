import GlobalConstants
from ws.conf.Config import Config
from ws.paginator.AbstractPaginator import AbstractPaginator
from ws.query.QueryExecutor import QueryExecutor


class IterationPaginator(AbstractPaginator):
    def __init__(self, config: Config):
        super().__init__(config)
        self._url_format = config.url + config.pagination_format
        self._data = []
        self._driver = GlobalConstants.WEBDRIVER

    def get_data(self):
        iteration = 1
        response_data = self.__send_request(iteration)
        while not self._stop_condition.check(response_data):
            self._data = self._data + response_data
            iteration = iteration + 1
            response_data = self.__send_request(iteration)

        return self._data

    def __send_request(self, iteration: int):
        self._driver.get(self._url_format % iteration)
        self._driver.implicitly_wait(10)
        html = self._driver.page_source

        return QueryExecutor.execute(html, self._config.item)

