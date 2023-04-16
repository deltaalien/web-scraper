import json

from metrics.BasicMetrics import BasicMetrics
from ws.conf.Config import Config
from ws.extractor.ExtractorFactory import ExtractorFactory
from ws.paginator.PaginatorFactory import PaginatorFactory


class WebScraper:
    def __init__(self, config: Config):
        self._config = config
        self._paginator = PaginatorFactory.get(config.pagination_type, config)
        self._extractor = ExtractorFactory.get(config.extraction, config)

    def scrap(self):
        print("Started scraping result page...")
        BasicMetrics.start_metric("scraping")
        result_data = self._paginator.get_data()
        BasicMetrics.stop_metric("scraping")

        print("\nRecords in result page: %d\n" % len(result_data))

        BasicMetrics.start_metric("extracting")
        extracted_data = self._extractor.extract_data(result_data)
        BasicMetrics.stop_metric("extracting")

        print("Extracted from results : %d\n" % len(extracted_data))

        with open("data_ce.json", "w") as f:
            BasicMetrics.start_metric("file")
            json.dump(extracted_data, f)
            BasicMetrics.stop_metric("file")

        BasicMetrics.get_metric_runtime("scraping")
        BasicMetrics.get_metric_runtime("extracting")
        BasicMetrics.get_metric_runtime("file")
