from abc import ABC, abstractmethod

from ws.conf.Config import Config


class AbstractExtractor(ABC):
    def __init__(self, config: Config):
        self._config = config

    @abstractmethod
    def extract_data(self, data: list):
        pass
