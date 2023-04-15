from abc import ABC, abstractmethod


class StopCondition(ABC):
    @abstractmethod
    def check(self, *args) -> bool:
        pass
