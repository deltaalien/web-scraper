from typing import Optional

from ws.conf.Config import Config
from ws.extractor.AbstractExtractor import AbstractExtractor
from ws.extractor.HtmlExtractor import HtmlExtractor
from ws.extractor.LinkExtractor import LinkExtractor


class ExtractorFactory:
    @staticmethod
    def get(extractor: str, config: Config) -> Optional[AbstractExtractor]:
        if not extractor:
            return None

        if "HTML_EXTRACTOR" == extractor:
            return HtmlExtractor(config)
        if "LINK_EXTRACTOR" == extractor:
            return LinkExtractor(config)

        return None
