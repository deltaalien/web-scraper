from typing import Optional

from ws.stop_condition.NoDataStopCondition import NoDataStopCondition
from ws.stop_condition.StopCondition import StopCondition


class StopConditionFactory:
    @staticmethod
    def get(condition_type: str) -> Optional[StopCondition]:
        if not condition_type:
            return None

        if "NO_DATA" == condition_type:
            return NoDataStopCondition()