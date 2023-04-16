from ws.stop_condition.StopCondition import StopCondition


class ExistingDataStopCondition(StopCondition):

    def __init__(self):
        self._seen_data = set()

    def check(self, *args) -> bool:
        if len(args) != 1:
            return True

        len_before = len(self._seen_data)

        for i in args[0]:
            self._seen_data.add(hash(i.get_text()))

        print("len before: %d, len after: %d" % (len_before, len(self._seen_data)))
        return len_before == len(self._seen_data)
