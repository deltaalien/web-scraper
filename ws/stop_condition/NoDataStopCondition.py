from ws.stop_condition.StopCondition import StopCondition


class NoDataStopCondition(StopCondition):
    def check(self, *args):
        if len(args) != 1:
            return True

        return len(args[0]) == 0
