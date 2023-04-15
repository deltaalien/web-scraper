from abc import ABC, abstractmethod
from ws.conf.Config import Config
from ws.stop_condition.StopConditionFactory import StopConditionFactory


class AbstractPaginator(ABC):
    def __init__(self, config: Config):
        self._config = config
        self._stop_condition = StopConditionFactory.get(config.stop)

    @abstractmethod
    def get_data(self) -> list:
        pass
