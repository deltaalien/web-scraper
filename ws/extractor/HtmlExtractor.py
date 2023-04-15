from ws.conf.Config import Config
from ws.extractor.AbstractExtractor import AbstractExtractor
from ws.query.QueryExecutor import QueryExecutor


class HtmlExtractor(AbstractExtractor):
    def __init__(self, config: Config):
        super().__init__(config)
    
    def extract_data(self, data: list):
        return_data = []
        for i in data:
            result = {}
            for key in self._config.data.keys():
                tmp = QueryExecutor.execute_tag(i, self._config.data[key])
                if len(tmp) == 0:
                    result[key] = ""
                else:
                    if self._config.data[key].data_attribute == "":
                        result[key] = tmp[0].get_text().strip()
                    else:
                        result[key] = tmp[0]

            return_data.append(result)

        return return_data
