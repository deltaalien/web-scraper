import time


class MetricData:
    def __init__(self, name: str):
        self._start_time = time.time_ns() / 1000_000
        self._end_time = -1
        self._name = name
        print("%s - start at: %d" % (self._name, self._start_time))

    def end(self):
        self._end_time = time.time_ns() / 1000_000
        print("%s - end at: %d" % (self._name, self._end_time))

    def get_runtime(self):
        if self._end_time == -1:
            return -1
        runtime = self._end_time - self._start_time
        print("%s - runtime: %d ms" % (self._name, runtime))

        return runtime


class BasicMetrics:
    __metrics_map = {}

    @staticmethod
    def start_metric(metrics_name: str):
        if metrics_name in BasicMetrics.__metrics_map:
            return
        BasicMetrics.__metrics_map[metrics_name] = MetricData(metrics_name)

    @staticmethod
    def stop_metric(metrics_name: str):
        if metrics_name in BasicMetrics.__metrics_map:
            BasicMetrics.__metrics_map[metrics_name].end()

    @staticmethod
    def get_metric_runtime(metrics_name: str):
        if metrics_name in BasicMetrics.__metrics_map:
            BasicMetrics.__metrics_map[metrics_name].get_runtime()
