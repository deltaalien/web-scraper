import json

import requests

from ws.conf.ConfigLoader import ConfigLoader
import GlobalConstants
from ws.extractor.HtmlExtractor import HtmlExtractor
from ws.paginator.IterationPaginator import IterationPaginator

if __name__ == '__main__':
    config = ConfigLoader.load_from_file(GlobalConstants.PROJECT_ROOT + "/config/halo_oglasi.json")

    paginator = IterationPaginator(config)
    result = paginator.get_data()

    print("\nResults in iteration: %d\n" % len(result))

    json_result = HtmlExtractor(config).extract_data(result)
    print("json_result : %d\n" % len(json_result))

    print(len(json_result))

    with open("data.json", "w") as f:
        json.dump(json_result, f)
