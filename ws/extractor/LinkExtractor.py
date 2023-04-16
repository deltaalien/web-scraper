from selenium import webdriver

from ws.conf.Config import Config
from ws.extractor.AbstractExtractor import AbstractExtractor
from ws.query.QueryExecutor import QueryExecutor
from ws.query.SearchQuery import SearchQuery


class LinkExtractor(AbstractExtractor):
    def __init__(self, config: Config):
        super().__init__(config)
        self._driver = webdriver.Chrome()

    def extract_data(self, data: list):
        return_data = []
        for i in data:
            result = {}
            html = self.__send_request(self._config.url+i)
            for key in self._config.data.keys():
                tmp = QueryExecutor.execute(html, self._config.data[key])
                if len(tmp) == 0:
                    result[key] = ""
                else:
                    if self._config.data[key].data_attribute == "":
                        result[key] = tmp[0].get_text().strip()
                    else:
                        result[key] = tmp[0]
            return_data.append(result)

        return return_data

    def __send_request(self, url: str):
        self._driver.get(url)
        self._driver.implicitly_wait(10)
        return self._driver.page_source
