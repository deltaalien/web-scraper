import GlobalConstants
from ws.conf.Config import Config
from ws.extractor.AbstractExtractor import AbstractExtractor
from ws.query.QueryExecutor import QueryExecutor


class LinkExtractor(AbstractExtractor):
    def __init__(self, config: Config):
        super().__init__(config)
        self._driver = GlobalConstants.WEBDRIVER

    def extract_data(self, data: list):
        return_data = []
        for i in data:
            result = {}
            html = self.__send_request(self._config.url + i)
            for key in self._config.data.keys():
                tmp = QueryExecutor.execute(html, self._config.data[key])
                if len(tmp) == 0:
                    result[key] = ""
                else:
                    result[key] = self.__process_result(tmp, key)

            return_data.append(result)

        return return_data

    def __send_request(self, url: str):
        self._driver.get(url)
        self._driver.implicitly_wait(10)
        return self._driver.page_source

    def __process_result(self, results, key: str):
        if self._config.data[key].data_attribute == "":
            if len(results) == 1:
                return results[0].get_text().strip()
            else:
                return [result.get_text().strip() for result in results]
        else:
            if len(results) == 1:
                return results[0]
            else:
                return results
